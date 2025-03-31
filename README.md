# buscaEmpleo

👷👷‍♀️ Pequeño sistema multiagente diseñado para buscar automáticamente ofertas laborales en internet, especialmente para personas con discapacidad.

![buscaEmpleo-git-corto](https://github.com/user-attachments/assets/ce96b339-b407-4f0a-8da8-312d0d84833d)

## Requisitos

Para ejecutar este proyecto, necesitarás tener instalados los siguientes requisitos:

- **Python >= 3.11**
- Una **API Key** gratuita de **Gemini-1.5-Flash** de Google Cloud.


## Inicio rápido

Con pip (Python>=3.11):

```bash
git clone https://github.com/capbility/buscaEmpleo.git
```

Instala las dependencias en requirements.txt

```bash
pip install requirements.txt
```

Preparamos playwright para controlar el navegador

```bash
playwright install chromium
```

En la carpeta raíz del repositorio, crea un archivo `.env` y agrega lo siguiente:

```bash
GEMINI_API_KEY = TuApiKey
MODEL='gemini-1.5-flash'
```

Ejecuta el archivo main.py

```bash
python main.py
```

Los resultados de la búsqueda se almacenarán en un archivo llamado `jobs.csv`, con la siguiente estructura:

```csv
Título del Puesto,Empresa,Enlace,Ubicación
```

## ⚠️ Limitaciones Actuales

- 🔍 **Búsqueda restringida**: Por ahora, solo se buscan empleos para personas con discapacidad en el área de marketing.  
- 📋 **Número de resultados**: Solo se seleccionan las **primeras 3 ofertas** encontradas.  
- 🛠️ **En desarrollo**: Planeamos expandir las funcionalidades en futuras versiones.

