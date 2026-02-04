import os
import json
import time
from pathlib import Path
from google import genai

# Create a Gemini client, passing in the API key from environment variables
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
