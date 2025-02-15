import os
import ollama
import warnings

warnings.filterwarnings("ignore", message="missing ScriptRunContext!")

class ChatBot():
    def __init__(self, model = "llama3" ):
        self.model = model

    def generate_response(self, query):
        response = ollama.chat(model = self.model, messages=[{"role": "user", "content": query}])
        return response['message']['content']
    
if __name__ == "__main__":
    pass


