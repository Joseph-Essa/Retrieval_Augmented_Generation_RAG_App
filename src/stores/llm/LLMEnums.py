from enum import Enum

class LLMEnums (Enum) : 
    
    OPENAI = "OPENAI"
    COHERE = "COHERE"
    GEMINI = "GEMINI"
    
    
class DocumentTypeEnum (Enum) : 
    DOCUMENT = "document"
    QUERY = "query"


class OpenAIEnum (Enum) : 
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    
class CoHereEnum (Enum) : 
    SYSTEM = "SYSTEM"
    USER = "USER"
    ASSISTANT = "CHATBOT"
    
    DOCUMENT = "search_document"
    QUERY = "search_query"
    
class GeminiEnum (Enum) : 
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

    