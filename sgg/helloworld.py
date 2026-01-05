from langchain_core.tools import create_retriever_tool

# 检索器工具
# retriever_tool = create_retriever_tool(
#     null,
#     "CivilCodeRetriever",
#     "搜索有关中华人民共和国民法典的信息。关于中华人民共和国民法典的任何问题，您必须使用此工具!",
# )
# tools = [retriever_tool]

import langchainhub as hub
from langgraph.prebuilt import create_react_agent

# https://smith.langchain.com/hub
# prompt = hub.pull("hwchase17/openai-functions-agent")
# agent = create_openai_functions_agent(llm, tools, prompt)
# agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
#
# 运行代理
# agent_executor.invoke({"input": "建设用地使用权是什么"})


from langchain_classic.agents import create_openai_functions_agent, AgentExecutor
