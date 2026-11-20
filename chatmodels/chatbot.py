from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage

model = ChatGoogleGenerativeAI(
      model="gemini-3.5-flash-lite",
    temperature=0
)

print("choose your ai mode")
print("press 1 for Angry mode")
print("press 2 for Funny mode")
print("press 3 for Sad mode")

choice=int(input("tell you response:-"))
if choice ==1:
    mode="you are a angry ai agent.you respond aggresively and impatiently."
elif choice==2:
    mode="you are a funny ai agent.you respond with jokes and humor."
elif choice==3:
    mode="you are a sad ai agent.you respond with aggressively and impatiently"       


messages=[
    SystemMessage(content=mode)
]

print("-------------- welcome type 0 to exit the application ------------")

while True:

    prompt = input("you: ")

    messages.append(HumanMessage(content=prompt))

    if prompt == "0":
       
        break

    try:
        response = model.invoke(messages)
        print("bot:", response.text)
        messages.append(AIMessage(content=response.text))
    except Exception as e:
        print("Something went wrong. Please try again.")

    print(messages)   