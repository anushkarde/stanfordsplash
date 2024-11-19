from openai import OpenAI

OPENAI_API_KEY = "sk-"
client = OpenAI(api_key=OPENAI_API_KEY)

# Create an empty list that will store the instructions we're giving 
# to our chatbot. We prompt the user to add to this
messages = []
system_msg = input("What type of chatbot would you like to create?\n")

# Send the user's preference of the type of chatbot to OpenAI
messages.append({"role": "system", "content": system_msg})

print("Say hello to your new assistant!")

# Until the user types in quit(), run the indented code over and over again
while input != "quit()":
    message = input("")
     # Store the user's question. We store the question and answers so that
     # our chatbot remembers what the user has asked in the past. 
    messages.append({"role": "user", "content": message})
    response = client.chat.completions.create(
        # Pick
        model="gpt-4o-mini", 
        # Instructions that we're sending to the AI.
        messages=messages
    )

    # Capture the AI's repsonse, store it, and print it out. 
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")