# latin_crylic
# 🇺🇿 Uzbek Transliteration Telegram Bot 🤖

This is a simple Telegram bot that automatically converts text between **Latin** and **Cyrillic** alphabets used in the Uzbek language.

Built using:
- 🐍 Python
- 📦 [py-transliterate](https://pypi.org/project/transliterate/)
- 🤖 [python-telegram-bot (telebot)](https://pypi.org/project/pyTelegramBotAPI/)

---

## 🚀 Features

✅ Converts **Latin → Cyrillic** if the message is in Latin  
✅ Converts **Cyrillic → Latin** if the message is in Cyrillic  
✅ Replies instantly with the converted text  
✅ Fully automated with infinite polling  

---

## ▶️ How to Use

1. **Start the bot** on Telegram by sending `/start`.
2. Send any message in Uzbek (Latin or Cyrillic).
3. The bot will reply with the transliterated version.

---

## 🛠 How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/uzbek-transliterator-bot.git
   cd uzbek-transliterator-bot
Install dependencies:

bash
Copy
Edit
pip install pyTelegramBotAPI transliterate
Replace the bot token with your own from @BotFather:

python
Copy
Edit
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
Run the bot:

bash
Copy
Edit
python bot.py
📎 Example
User: Salom, do'stim!
Bot: Салом, до`стим!

User: Яхшимисиз?
Bot: Yaxshimisiz?

📌 Author
Oxunjonov Nasimjon

GitHub: github.com/Nasimjon05

Telegram Design Portfolio: t.me/+YLj0BIcTL55iNjcy

🧠 Future Plans
Add support for voice messages

Web interface with Flask

Word-level error checking

⚠️ Disclaimer
Do not share your real bot token publicly. Regenerate it using BotFather if it's been exposed.

🏁 License
MIT License — free for personal or commercial use.
