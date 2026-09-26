language = input("Choice language (1.ru/2.en):")
if language == "2.en" or language == "2" or language == "en":
    name = input("Please enter your name: ")
    while not name:
        name = input("Enter your NAME: ")
elif language == "1.ru" or language == "ru" or language == "1":
    name_ru = input("Пожалуйста введите своё имя: ")
    while not name_ru:
        name_ru = input("введите своё ИМЯ: ")

sites_programming = """
        Programming
VS Code 
Site - https://code.visualstudio.com/
Github - https://github.com/microsoft/vscode

Python
Site - https://www.python.org/
Documentation - https://docs.python.org/3/
Github - https://github.com/python

Java
Site - https://www.java.com
Documentation (Oracle) - https://docs.oracle.com/en/java/
Github - https://github.com/topics/java-programming

C++
Site - https://learn.microsoft.com/en-us/cpp/cpp/?view=msvc-170
Github - https://github.com/topics/cpp

Git 
SIte - https://git-scm.com/
Documentation - https://git-scm.com/docs

Github - https://github.com/
Documentation - https://docs.github.com/
"""

sites_ai = """
        AI
ChatGPT - https://chatgpt.com/
Gemini - https://gemini.google.com/
Claude - https://claude.ai/
Grok - https://grok.com/
Perplexity - https://www.perplexity.ai/
Kimi - https://www.kimi.com

Hugging Face - https://huggingface.co/
Google AI Studio - https://aistudio.google.com/

Ollama - https://ollama.com/
LM Studio - https://lmstudio.ai/

GitHub Copilot - https://github.com/features/copilot
Claude Code - https://claude.com/product/claude-code

Removal AI - https://removal.ai/

ElevenLabs - https://elevenlabs.io/
Runway - https://runwayml.com/
PixVerse - https://pixverse.ai/
Suno - https://suno.com
"""