# Simple Discord Bot

A basic Discord bot template using Python and the `discord.py` library.

## Features

- Responds to the `!ping` command with "Pong!"
- Can be easily extended with additional commands and functionality

## Installation

1. Clone the repository:
   https://github.com/anshuxx/simple-discord-bot-template/
2. Navigate to the project directory:
   cd simple-discord-bot-template
3. Install the required dependencies
4. Obtain a Discord bot token from the [Discord Developer Portal](https://discord.com/developers/applications).

5. Replace `'bot_ka_token'` in the `main.py` file with your bot token.

6. Run the bot:
   python main.py
## Usage

1. Invite the bot to your Discord server by generating an OAuth2 URL and selecting the appropriate permissions.

2. Once the bot is added to your server, you can use the `$ping` command to test its functionality.

## Extending the Bot

To add more commands or functionality to the bot, follow these steps:

1. Open the `main.py` file.

2. Define a new command function using the `@client.command()` decorator:

```python
@bot.command(name='hello')
async def hello(ctx):
    await ctx.send('Hello, world!')
```

This README.md file provides a basic structure for your simple Discord bot project on GitHub. It includes sections for features, installation, usage, extending the bot, contributing, and the license. You can customize the content as needed to match your specific project details.
