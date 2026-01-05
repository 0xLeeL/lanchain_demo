
import os

from langchain.chains import llm
from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    api_key="sk-13d5adbc17b44dce9691813cbc3c362d", # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)


prompt = ChatPromptTemplate.from_template("请用中文回答：{question}")
chain = prompt

response = chain.invoke({"question": "什么是 LangChain？"})
print(response.)