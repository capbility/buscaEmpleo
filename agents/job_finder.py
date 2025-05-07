from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContextConfig
from controllers.job_controller import controller
import asyncio

from config.settings import PROVIDER, API_KEY, MODEL

if PROVIDER == "gemini":
    from langchain_google_genai import ChatGoogleGenerativeAI
    llm = ChatGoogleGenerativeAI(model=MODEL, api_key=API_KEY)
elif PROVIDER == "openai":
    from langchain_openai import ChatOpenAI
    llm = ChatOpenAI(model=MODEL)
else:
    raise ValueError("Proveedor no válido. Usa 'gemini' o 'openai'.")

browser = Browser(
    config=BrowserConfig(
        new_context_config=BrowserContextConfig(viewport_expansion=0)
    )
)

async def run_job_finder(palabra_clave, es_discapacidad, cantidad_ofertas):
    
    diccionario = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five"
    }

    if cantidad_ofertas in diccionario:
        cantidad_ofertas =  diccionario[cantidad_ofertas]
    else:
        cantidad_ofertas = diccionario[5]

    ground_task = (
        'You are a professional job finder.'
        'find "empleo ' + palabra_clave + (' postulantes con discapacidad' if es_discapacidad else '') + '"'
        'go to first result of:'
    )

    #ground_task = (
    #    'You are a professional job finder.'
    #    'find "empleo marketing personas con discapacidad"'
    #    'got to first result of:'
    #)
    
    tasks = [
        ground_task + '\n' + 'bumeran.com.pe'
        + ' Open the first '+ cantidad_ofertas +' and save jobs with save_jobs'
    ]

    agents = [] 
    for task in tasks:
        agent = Agent(task=task, llm=llm, controller=controller, browser=browser)
        agents.append(agent)
	
    await asyncio.gather(*[agent.run() for agent in agents])

    browser.close()

