from app.chatbot.rag.semantic_retriever import build_vector_store, semantic_search


services_db = build_vector_store("app/chatbot/data/services.txt")
pricing_db = build_vector_store("app/chatbot/data/pricing.txt")


def services_content(query: str):
    return semantic_search(services_db, query)


def pricing_content(query: str):
    return semantic_search(pricing_db, query)


intent_mapper = {
    "services": services_content,
    "pricing": pricing_content,
}