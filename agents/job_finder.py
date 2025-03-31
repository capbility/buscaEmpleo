from browser_use import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContextConfig
from config.settings import GEMINI_API_KEY, MODEL
from controllers.job_controller import controller
import asyncio

browser = Browser(
    config=BrowserConfig(
        new_context_config=BrowserContextConfig(viewport_expansion=0)
    )
)

async def run_job_finder():
    llm = ChatGoogleGenerativeAI(model=MODEL, api_key=GEMINI_API_KEY)
    ground_task = (
        'You are a professional job finder.'
        'find "empleo marketing personas con discapacidad"'
        'got to first result of:'
    )
    tasks = [
        ground_task + '\n' + 'bumeran.com.pe'
        + 'Save the first three jobs with save_jobs'
    ]

    agents = [] 
    for task in tasks:
        agent = Agent(task=task, llm=llm, controller=controller, browser=browser)
        agents.append(agent)
	
    await asyncio.gather(*[agent.run() for agent in agents])


