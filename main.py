from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser # Definir uma classe em Python que será o output da LLM
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool

# Caso quisesse usar chatgpt
# from langchain_openai import ChatOpenAI
# llm = ChatAnthropic(model="gpt-4o-mini")

load_dotenv()

# Importante passar como parâmetro para todas propriedades herdarem o BaseModel do Pydantic
class ResearchResponse(BaseModel):
    topic: str 
    summary: str 
    source: list[str]
    tools_used: list[str]

llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system", # Esse parâmetro é passado para a llm para ela saber o que ela estará fazendo
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use the neccessary tools.
            Wrap the output in this format and provide no other text \n{format_instructions}
            """, # Importante ter esse 'format_instructions' para manter o Output padronizado
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions()) # Instruções de formatação vão seguir o padrão da classe ResearchResponse, feito isso com ajuda do Pydantic

tools = [search_tool, wiki_tool, save_tool]
agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

agent_executer = AgentExecutor(agent=agent, tools=tools, verbose=True) # verbose é usado para printar o "pensamento" da llm
query = input("What can I help you research? ")
raw_response = agent_executer.invoke({"query": query})

try:
    # ResearchResponse
    structured_response = parser.parse(raw_response.get("output")[0]["text"])
except Exception as e:
    print("Error parsing response", e, "Raw Response - ", raw_response)

print(structured_response)