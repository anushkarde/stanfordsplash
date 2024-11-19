from openai import OpenAI

# Your API key is like a password to use OpenAI. Keep it secret!
# Get your API key from the environment instead of hardcoding it.
import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# "client" is your personal helper that will connect 
# to OpenAI's system using your unique API key.
client = OpenAI(api_key=OPENAI_API_KEY)

response = client.chat.completions.create(
    # Pick a model
    model="gpt-4o-mini", 

    messages=[
        {
            # Telling OpenAI how we want our chatbot to act
            "role": "system", 
            "content": "You are a really mean assistant."},

        {   
            # Sending a request to our chatbot 
            "role": "user", 
            "content": "Write a poem about Thanksgiving."
        }
    ]
)

# response contains the AI's response
# This is a list of possible responses from the AI. By default, 
# it usually contains just one.
print(response.choices[0].message.content)