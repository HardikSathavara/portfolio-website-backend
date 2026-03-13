from langchain_groq import ChatGroq


class LLMManager:

    def __init__(self):

        self.llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0
        )

    def get_llm(self):
        return self.llm