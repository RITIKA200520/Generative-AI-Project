from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
)
messages=[]

print("-------------- welcome type 0 to exit the application ------------")

while True:

    prompt = input("you: ")

    messages.append(prompt)

    if prompt == "0":
        break

    try:
        response = model.invoke(messages)
        print("bot:", response.text)
        messages.append(response.text)
    except Exception as e:
        print("Something went wrong. Please try again.")