
import asyncio
from agents.job_finder import run_job_finder

if __name__ == '__main__':
    palabra_clave = input("¿Qué tipo de empleo buscas? (ej. marketing, IT, diseño): ").strip()
    es_discapacidad = input("¿Es para personas con discapacidad? (si/no): ").lower().strip() == "si"
    cantidad_ofertas = int(input("Ingresa la cantidad de ofertas laborales que quieres guardar en formato de número (1, 2, 3, 4 o 5): "))

    asyncio.run(run_job_finder(palabra_clave, es_discapacidad, cantidad_ofertas))








