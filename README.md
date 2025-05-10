# buscaEmpleo

👷👷‍♀️ Pequeño sistema de agente diseñado para buscar automáticamente ofertas laborales en internet, especialmente para personas con discapacidad.

![buscaEmpleo-ui](https://github.com/user-attachments/assets/648a9aec-81a7-4af5-89b5-55288e2d0718)

## Requisitos

Para ejecutar este proyecto, necesitarás tener instalados los siguientes requisitos:

- **Python >= 3.11**
- Una **API Key** gratuita de **Gemini** u **OpenAI**
- Modelos probados:  
   - **GPT-4o**: recomendado.
   - **Gemini-1.5-Flash**. 


## Inicio rápido

Con pip (Python>=3.11):

```bash
git clone https://github.com/capbility/buscaEmpleo.git
```

Instala las dependencias en requirements.txt

```bash
pip install -r requirements.txt
```

Preparamos playwright para controlar la navegación usando una versión de chromium

```bash
playwright install chromium
```

En la carpeta raíz del repositorio tienes un archivo .env.example, modificarlo y crea un archivo `.env`, elimina los # del modelo que quieres usar:

```bash
OPENAI_API_KEY=TuApiKey
MODEL_OPENAI='TuModelo'
```

Ejecuta desde terminal

```bash
python web/app.py
```

Se abrirá una aplicación web hecha en Flask, completa el formulario y presiona el botón de Enviar.

Los resultados se mostrarán en una tabla y se guardarán en un archivo llamado `jobs_TIMESTAMP.csv`, con la siguiente estructura:

```csv
Título del Puesto,Empresa,Enlace,Ubicación
```

## ⚠️ Limitaciones Actuales

- 🔍 **Única búsqueda**: Si deseas buscar por segunda vez, necesitas reiniciar la aplicación web. 
- 🔍 **Búsqueda en una sola plataforma**: Solo busca en la web de Bumeran Perú. 
- 🔍 **Búsqueda sin salario**: Los resultados no muestran el salario.
- 📋 **Número de resultados**: Solo se seleccionan como máximo las **primeras 5 ofertas** encontradas.  
- 🛠️ **En desarrollo**: Planeamos expandir las funcionalidades en futuras versiones.

