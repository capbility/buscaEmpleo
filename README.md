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

Se mostrará un menú en el que el usuario debe ingresar palabras clave relacionadas con el empleo que está buscando. Luego, se le pedirá que indique si tiene alguna discapacidad, respondiendo 'sí' o 'no'. Finalmente, el usuario podrá seleccionar cuántas ofertas de empleo desea guardar. Si ingresa un número mayor a 5, el programa automáticamente ajustará este valor a 5.

Los resultados de la búsqueda se almacenarán en un archivo llamado `jobs.csv`, con la siguiente estructura:

```csv
Título del Puesto,Empresa,Enlace,Ubicación
```

## ⚠️ Limitaciones Actuales

- 🔍 **Búsqueda en una sola plataforma**: Solo busca en la web de Bumeran Perú. 
- 🔍 **Búsqueda sin salario**: Los resultados no muestran el salario.
- 📋 **Número de resultados**: Solo se seleccionan como máximo las **primeras 5 ofertas** encontradas.  
- 🛠️ **En desarrollo**: Planeamos expandir las funcionalidades en futuras versiones.

