import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv("/mnt/d/lancers/NLP HW 2/Gentopia-Mason/GentPool/.env")

# Retrieve the API key
api_key = os.getenv('OPENAI_API_KEY')

# Print the API key to verify it's loaded
print(f"API Key: {api_key}")
