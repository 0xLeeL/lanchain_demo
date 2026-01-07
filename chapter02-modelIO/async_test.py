import asyncio
import os
import time

import dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, ChatMessage
from langchain_openai import ChatOpenAI
dotenv.load_dotenv()

chat_model = ChatOpenAI(
    model='qwen-plus',
    api_key=os.getenv('ALI_API_KEY'),
    base_url=os.getenv('ALI_API_URL')
)
def call_invoke():
    messages1 = [SystemMessage(content="你是一位乐于助人的智能小助手"),
                 HumanMessage(content="请帮我介绍一下什么是机器学习"), ]
    # 调用batch
    response = chat_model.invoke(messages1)
    print(response)
async def async_test():
    messages1 = [SystemMessage(content="你是一位乐于助人的智能小助手"),
                 HumanMessage(content="请帮我介绍一下什么是机器学习"), ]
    # 调用batch
    response = await chat_model.ainvoke(messages1)
    print(response)

async def run_concurrent_tests():
    # 创建3个异步任务
    tasks = [async_test() for _ in range(3)]
    # 并发执行所有任务
    return await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time.time()
    # 这里会被阻塞
    results = asyncio.run(run_concurrent_tests())
    call_invoke()

    total_time = time.time() - start_time
    print('total time:', total_time)