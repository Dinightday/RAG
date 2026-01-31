from langchain_core.prompts import PromptTemplate

def prompt():
    prompt_template = PromptTemplate.from_template("""Você irá fazer um resumo e explicar sobre o assunto: {documento}. 
                                                   Da pergunta: {question}""")
    return prompt_template