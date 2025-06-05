from abc import ABC, abstractmethod

class LLMIterface(ABC) : 
    @abstractmethod
    def set_generation_model (self , model_id : str) : 
        pass
    
    @abstractmethod
    def set_embedding_model (self , model_id : str , embedding_size : int) : 
        pass
    
    # temperature ->  indicator for the creativity level for the generated answers (0.0 -> low creativity)
    @abstractmethod
    def generate_text (self , prompt : str , chat_history : list =[] , 
                       max_output_tokens : int=None , temperature : float=None ) : 
        pass
    
    # document_type -> some providers take it as indicator to know the type of text if it query from user or
    # larger text , it improves the way that the model use for embedding 
    @abstractmethod
    def embed_text (self, text: str, document_type: str = None): 
        pass
    
    @abstractmethod
    def constaract_prompt (self , prompt : str , role : str):
        pass 