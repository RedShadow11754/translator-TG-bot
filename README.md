Telegram Translator Bot

A simple Telegram bot that translates messages into Amharic using TranslatorBot.

Features:
- Translate messages in private chats.
- Works in group chats when mentioned.
- Async handling for fast responses.
- /start command to begin.

Requirements:
- Python 3.10+
- python-telegram-bot v20+
- python-dotenv
- Your TranslatorBot module

Setup:
1. Clone the repository and go to the project folder.
2. Install dependencies:
   pip install python-telegram-bot python-dotenv
3. Create a .env file:
   TOKEN=your_telegram_bot_token
   BOT_USERNAME=@YourBotUsername
4. Run the bot:
   python main.py

Usage:
- Use /start to initiate.
- In private chat: send a message → bot translates.
- In group chat: mention the bot → it translates the message.

Notes:
- Default language is Amharic (am).
- Ensure TranslatorBot supports async.