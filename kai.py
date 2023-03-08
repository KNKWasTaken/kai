import openai
import sys

#Defining Functions
def textgen(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=4000,
        temperature=0.5
    )

    return response.choices[0].text.strip()

def savechathistory(chathistory, filepath):
    with open(filepath, "w") as f:
        for line in chathistory:
            f.write(line + "\n")

def loadchathistory(filepath):
    chathistory = []
    try:
        with open(filepath, "r") as f:
            for line in f.readlines():
                chathistory.append(line.strip())
    except:
        pass
    return chathistory

# Set OpenAI API key as a string
api_key = "yourapikey"
openai.api_key = api_key

# Test authentication (not neccessary but suggested)
try:
    response = openai.Completion.create(engine="davinci", prompt="Hello, world!", max_tokens=3)
    print("Authentication test passed!")
except Exception as e:
    print("Authentication test failed:", e)

#Loading of Chat History
chathistoryfile = "chathistory.txt"

# Looped Chat Experience
while True:
    chathistory = loadchathistory(chathistoryfile)
    chatinput = input("You: ")
    chathistory.append("User: " + chatinput)
    savechathistory(chathistory, chathistoryfile)
    if chatinput.lower() == "e":
        sys.exit()
    else:
        response = textgen(chatinput)
    chathistory.append("Bot: " + response)
    savechathistory(chathistory, chathistoryfile)
    print("Bot: " + response)
