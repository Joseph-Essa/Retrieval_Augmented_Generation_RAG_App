from ..LLMInterface import LLMInterface
from ..LLMEnums import OpenAIEnum
from openai import OpenAI
import logging 

class OpenAIProvider(LLMInterface):
    def __init__(self, api_key: str ,api_url:str = None ,
                 default_input_max_characters:int=1000 ,
                 default_generation_max_output_tokens:int=1000 , 
                 default_generation_temperature:float=0.1):
        self.api_key = api_key
        self.api_url = api_url
        
        self.default_input_max_characters = default_input_max_characters
        self.default_generation_max_output_tokens = default_generation_max_output_tokens
        self.default_generation_temperature = default_generation_temperature
        
        self.generation_model_id = None
        
        self.embedding_model_id = None
        self.embedding_size = None
        
        self.client = OpenAI(api_key=self.api_key ,
                            base_url=self.api_url if self.api_url and len(self.api_url) else None
                            )
        self.enums = OpenAIEnum
        
        self.logger = logging.getLogger(__name__)
        

    def set_generation_model(self, model_id: str):
        self.generation_model_id = model_id

    def set_embedding_model(self, model_id: str , embedding_size:int):
        self.embedding_model_id = model_id
        self.embedding_size = embedding_size

    def process_text (self , text : str):
        return text[:self.default_input_max_characters].strip()
    
    
    def generate_text (self , prompt : str , chat_history : list =[] , 
                       max_output_tokens : int=None , temperature : float=None ) :
        if not self.client : 
            self.logger.error (f"OpenAI Client Was Not Set ")
            return None
        if not self.generation_model_id : 
            self.logger.error (f"Generation Model For OpenAI Was Not Set ")
            return None
        max_output_tokens = max_output_tokens if max_output_tokens  else self .default_generation_max_output_tokens
        temperature = temperature if temperature else self.default_generation_temperature
        
        chat_history.append(
            self.constaract_prompt(prompt=prompt , role=OpenAIEnum.USER.value)
            )
        
        response = self.client.chat.completions.create(
            model = self.generation_model_id,
            messages = chat_history,
            max_tokens = max_output_tokens,
            temperature = temperature
        )
        
        if not response or not response.choices or len (response.choices) == 0 or not response.choices[0].message :
            self.logger.error ("Error While Generating Text With OpenAI")
            return None
        return response.choices[0].message.content



    def embed_text(self, text: str, document_type: str = None):
        
        if not self.client : 
            self.logger.error ("OpenAI Client Was Not Set ")
            return None
        if not self.embedding_model_id : 
            self.logger.error ("Embedding Model For OpenAI Was Not Set ")
            return None
        responss = self.client.embeddings.create(
            model = self.embedding_model_id,
            input = text
        )
        if not responss or not responss.data or len (responss.data) == 0 or not responss.data[0].embedding :
            self.logger.error ("Error While Embedding text with OpenAI") 
            return None
        return responss.data[0].embedding

    def constaract_prompt(self, prompt: str, role: str):
        # Due to OpenAI Docs
        return {
            
            "role": role, 
            "content": prompt
        }
