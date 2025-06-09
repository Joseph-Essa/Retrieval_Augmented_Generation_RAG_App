from ...LLMInterface import LLMInterface
from ...LLMEnums import GeminiEnum

# For Now we can use same implementation for OpenAIProvider class but use
# base_URL for Gemini (https://generativelanguage.googleapis.com/v1beta/openai/)
# due to Gemini Docs (https://ai.google.dev/gemini-api/docs/openai#streaming)