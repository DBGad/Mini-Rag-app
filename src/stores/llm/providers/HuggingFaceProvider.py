from ..LLMInterface import LLMInterface
from sentence_transformers import SentenceTransformer
import logging

class HuggingFaceProvider(LLMInterface):

    def __init__(self,api_key:str, default_input_max_characters: int=1000):
        
        self.default_input_max_characters = default_input_max_characters

        self.generation_model_id = None

        self.embedding_model_id = None
        self.embedding_size = None
        self.embedding_model = None

        self.logger = logging.getLogger(__name__)

    def set_generation_model(self, model_id: str):
        self.logger.warning("HuggingFace provider does not support text generation in this implementation")
        self.generation_model_id = model_id

    def set_embedding_model(self, model_id: str, embedding_size: int):
        self.embedding_model_id = model_id
        self.embedding_size = embedding_size
        
        try:
            self.embedding_model = SentenceTransformer(model_id)
            self.logger.info(f"Loaded HuggingFace embedding model: {model_id}")
        except Exception as e:
            self.logger.error(f"Error loading HuggingFace model: {e}")
            self.embedding_model = None

    def process_text(self, text: str):
        return text[:self.default_input_max_characters].strip()

    def generate_text(self, prompt: str, chat_history: list=[], max_output_tokens: int=None,
                            temperature: float = None):
        self.logger.warning("HuggingFace provider does not support text generation in this implementation")
        return None

    def embed_text(self, text: str, document_type: str = None):
        
        if not self.embedding_model:
            self.logger.error("HuggingFace embedding model was not loaded")
            return None

        if not self.embedding_model_id:
            self.logger.error("Embedding model for HuggingFace was not set")
            return None
        
        try:
            processed_text = self.process_text(text)
            embedding = self.embedding_model.encode(processed_text, convert_to_numpy=True)
            return embedding.tolist()
        except Exception as e:
            self.logger.error(f"Error while embedding text with HuggingFace: {e}")
            return None

    def construct_prompt(self, prompt: str, role: str):
        return {
            "role": role,
            "content": self.process_text(prompt)
        }