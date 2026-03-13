import re
from fastapi import Request
from langchain_core.prompts import PromptTemplate
from app.chatbot.rag.intent_mapper import intent_mapper


intent_classification_prompt = PromptTemplate(
    input_variables=["query"],
    template="""
            Classify the user query into one of the following intents:

            greeting
            services
            pricing
            project
            general

            Rules:
            - Return ONLY the intent name
            - Do not explain anything
            - If unsure return general

            User Query:
            {query}

            Intent:
        """
    )


bot_response_prompt = PromptTemplate(
    input_variables=["query", "context"],
    template="""
            You are an AI assistant for our company.

            Answer the user ONLY using the provided context.

            Rules:
            - Response must be short, simple and helpful
            - Do NOT use your own knowledge
            - If the answer is not in the context say:
            "I don't have much information about this. Please connect with our management."

            Context:
            {context}

            User Query:
            {query}

            Answer:
        """
    )


INTENTS = ["greeting", "services", "pricing", "project", "general"]



def preprocess_query(query: str) -> str:

    query = query.lower()

    query = re.sub(r'[^\w\s]', '', query)

    query = re.sub(r'\s+', ' ', query).strip()

    return query



def detect_intent(query: str, request: Request):
    
    llm = request.app.state.llm_manager.get_llm()
    
    formatted_prompt = intent_classification_prompt.format(query=query)

    response = llm.invoke(formatted_prompt)

    intent = response.content.strip().lower()

    if intent not in INTENTS:
        intent = "general"

    return intent



def handle_query(query, request: Request):
    
    query = preprocess_query(query=query)

    intent = detect_intent(query, request)

    print("Intent: ", intent)

    if intent in intent_mapper:

        results = intent_mapper[intent](query)

        context = "\n".join(results)

        llm = request.app.state.llm_manager.get_llm()

        chain = bot_response_prompt | llm

        response = chain.invoke({
            "query": query,
            "context": context
        })

        return response.content.strip()


    return "Sorry, I couldn't understand your request."

