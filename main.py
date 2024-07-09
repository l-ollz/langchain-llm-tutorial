from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

# モデルを直接使用してみましょう。ChatModelsはLangChainの「Runnables」のインスタンスであり、
# これはそれらと対話するための標準インターフェースを提供することを意味します。
# 単にモデルを呼び出すには、.invokeメソッドにメッセージのリストを渡すことができます。
model = ChatGroq(model="llama3-8b-8192")

parser = StrOutputParser()

messages = [
    SystemMessage(content="Translate the following from English into French"),
    HumanMessage(content="hi!"),
]

# モデルの呼び出し
response = model.invoke(messages)
# 出力内容の表示
print(parser.invoke(response))

## チェーン
chain = model | parser
print(chain.invoke(messages))


from langchain_core.prompts import ChatPromptTemplate

system_template = "Translate the following into {language}:"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

result = prompt_template.invoke({"language": "french", "text": "hi"})

print(result.to_messages())

# Chaining together components with LCEL

chain = prompt_template | model | parser
print(chain.invoke({"language": "french", "text": "hi"}))