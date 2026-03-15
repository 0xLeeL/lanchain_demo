from langchain_classic.memory import ConversationSummaryBufferMemory
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_classic.chains.llm import LLMChain

import os

import dotenv
from langchain_classic.chains.llm import LLMChain
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, ChatMessage
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder

from langchain_openai import ChatOpenAI
dotenv.load_dotenv()

llm = ChatOpenAI(
    model='qwen-plus',
    api_key=os.getenv('ALI_API_KEY'),
    base_url=os.getenv('ALI_API_URL'),
)

prompt_template = PromptTemplate(template="你是一个{role},你的名字叫{name}",input_variables=["role", "name"])



# 2、定义提示模板
prompt = ChatPromptTemplate.from_messages([
("system", "你是电商客服助手，用中文友好回复用户问题。保持专业但亲切的语气。"),
MessagesPlaceholder(variable_name="chat_history"),
("human", "{input}")
])
# 3、创建带摘要缓冲的记忆系统
memory = ConversationSummaryBufferMemory(
llm=llm,
max_token_limit=400,
memory_key="chat_history",
return_messages=True
)
# 4、创建对话链
chain = LLMChain(
llm=llm,
prompt=prompt,
memory=memory,
)
# 5、模拟多轮对话
dialogue = [
("你好，我想查询订单12345的状态", None),
("这个订单是上周五下的", None),
("我现在急着用，能加急处理吗", None),
("等等，我可能记错订单号了，应该是12346", None),
("对了，你们退货政策是怎样的", None)
]
# 6、执行对话
for user_input, _ in dialogue:
    response = chain({"input": user_input})
    print(f"用户: {user_input}")
    print(f"客服: {response['text']}\n")
# 7、查看当前记忆状态
print("\n=== 当前记忆内容 ===")
print(memory.load_memory_variables({}))
