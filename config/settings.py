import os
from dotenv import load_dotenv
from pydantic import SecretStr

load_dotenv()

required_env_vars = ['OPENAI_API_KEY']
for var in required_env_vars:
    if not os.getenv(var):
        raise ValueError(f'{var} is not set. Please add it to your environment variables.')

#GEMINI_API_KEY = SecretStr(os.getenv('GEMINI_API_KEY'))
#MODEL = os.getenv('MODEL', 'gemini-1.5-flash')
OPENAI_API_KEY = SecretStr(os.getenv('OPENAI_API_KEY'))
MODEL = os.getenv('MODEL', 'gpt-4o-2024-08-06')
