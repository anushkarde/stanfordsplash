from openai import OpenAI
import gradio

OPENAI_API_KEY = "sk-"
client = OpenAI(api_key=OPENAI_API_KEY)

# Start by creating a list that keeps track of our chatbot's "memory."
# This includes all the messages you've sent and the AI's responses.
messages = [
    {
        "role": "system", 
        "content": "You are a super sassy personal assistant, and you always respond to me in rhymes."
    }
]
# This function is where the chatbot does its work.
# When the user types something, the chatbot reads it, thinks, and then replies.
def CustomChatGPT(input):
    # Add the user's message to the chatbot's memory.
    messages.append({"role": "user", "content": input})
    # Ask OpenAI to come up with a response based on the messages so far.
    response = client.chat.completions.create(
        model = "gpt-4o-mini", # the version of the AI we are using
        messages = messages    # all the past messages (chat history)
    )

    # Save the AI's response to the ChatBot's memory
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return reply

# Create a simple website where people can chat with the sassy assistant.
# "inputs" is where the user types, and "outputs" is where the chatbot replies.
demo = gradio.Interface(
    fn=CustomChatGPT, 
    inputs = "text", 
    outputs = "text", 
    title = "SassyBot",
    flagging_mode="never" 
)

# Launch the chatbot app! The "share=True" makes it so you can share the app link.
demo.launch(share=True)