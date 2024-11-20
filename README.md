# 🎓 Stanford Splash: Build Your Own Chatbot!

Hi everyone! 👋 I hope you had an awesome time at Splash! 🚀 Below, you'll find all the information about the code we wrote in class and tips for taking it to the next level. Let’s dive in! 🌟

---

## 📂 What's in This Repository?

This repo contains **three files** to help you build your chatbot step by step:
- `chatbot1.py`
- `chatbot2.py`
- `chatbot3.py`

✨ **Work through these files in order!** Start with `chatbot1.py`, then move on to the others.

---

## ⚙️ How to Run the Code

You can run the code either on:
1. **A Local IDE** (e.g., VSCode, PyCharm, Sublime Text)
2. **An Online Editor** (e.g., [Replit](https://replit.com), which works great!)

### 🖥️ Local IDE Instructions
1. Install your favorite IDE.
2. Create a folder for your project.
3. Open the folder in your IDE.
4. Install Python in your IDE.
5. Open the **terminal/shell** in your IDE.
6. Set up a **virtual environment** with the following commands:
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   pip install openai
   pip install gradio
   ```
   If `pip` doesn’t work, try `pip3`.

### 🌐 Replit Instructions
1. Log in or create an account with Google at [Replit](https://replit.com).
2. Create a new Python Repl.
3. Open the **Terminal/Shell** tab.
4. Install the required packages by running:
   ```bash
   pip install openai
   pip install gradio
   ```
   If `pip` doesn’t work, try `pip3`.

---

## 🔑 Setting Up Your OpenAI API Key

To run the chatbot, you’ll need an **OpenAI API Key**, which acts like a password to access the AI model.

1. Create an OpenAI developer account: [OpenAI Platform](https://platform.openai.com/).
2. Go to **API Keys** (search for it on the left).
3. Click **Create New Secret Key** (green button).
4. **Copy and save** the key somewhere secure.
5. Paste the key into the `OPENAI_API_KEY` variable in each file (replace the empty quotes with your key).

💡 **Note**: You may need to purchase credits, but $5 should be more than enough to explore and test your chatbot.

---

## ▶️ Running the Code in Your IDE

If you’re having trouble with package compatibility, ensure you’re running the code **inside the virtual environment** where you installed the packages. To do so:
1. Replace `<#>` with the relevant chatbot file number (`1`, `2`, or `3`).
2. Run:
   ```bash
   .venv/bin/python3 chatbot<#>.py
   ```

---

## 🎉 Next Steps

Congratulations on building your own chatbot web app with `chatbot3.py`! 🎊 Here are some ideas to extend and customize it further:
1. **Study Buddy**: Build a bot that explains homework approaches without giving answers. It can ask guiding questions to help you think critically.
2. **Wordle Bot**: Turn it into a game where it picks a random word, and you guess letters until you find the right word.
3. **Voice-Enabled Chatbot**: Experiment with text-to-speech models to make your chatbot "talk" back to you.

For inspiration, check out **GPT wrapper apps** on YouTube to explore more creative ideas! 🎥

---

## 📚 Slides & Support

- **Class Slides**: [Splash Chatbot Presentation](https://docs.google.com/presentation/d/1ZM79GJkN4pBIY4dxcIIHISf2NNOaWCQ1CE50FEeuA54/edit#slide=id.p)
- **Questions?** Feel free to reach out to me at 📧 **anushkad@stanford.edu**.

---

## 🚀 Remember

YOU have the power to build amazing things with AI! Keep experimenting, stay curious, and have fun. 🧠💻🎨
