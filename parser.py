from langchain.chains.qa_with_sources.stuff_prompt import template
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

templates = (
"You are tasked with extracting specific information from the following text content: {content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {humanPrompt}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

model = OllamaLLM(model="llama3.2:1b")


def parseChunks(chunks, prompt):
    prompt = ChatPromptTemplate.from_template(templates)
    chain = prompt | model

    parsedResult = []
    for i, chunk in enumerate(chunks, start=1):
        response = chain.invoke(
            {"content": chunk, "humanPrompt": prompt}
        )
        print(f"Chunk {i} of {len(chunks)}")
        parsedResult.append(response)

    return "\n".join(parsedResult)