from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

gemini = init_chat_model(model="gemini-3-flash-preview", model_provider="google_genai")
answer_gemini = gemini.invoke("Hello world")
print(answer_gemini.content)
