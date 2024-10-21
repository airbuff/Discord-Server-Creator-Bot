# Elevator Discord Bot

## Overview

**Elevator Discord Bot** is a custom Discord bot built to automate the setup of a game-centric Discord server with a humorous theme. The bot creates roles, categories, and text/voice channels for games such as CS:GO, Rust, Minecraft, ARK, and more. It also incorporates spaces for cybersecurity, development, and general server management. The bot allows for easy server setup with predefined categories and roles, while also setting up channels for rules, general chats, and voice lounges.

The main purpose of the bot is to streamline server setup, allowing admins to quickly establish a well-organized server with game-themed channels, moderator roles, and a friendly community layout.

## Features

- Automated server setup: Creates roles, categories, and channels based on predefined settings.
- Game-themed channels: Set up game-specific text and voice channels for popular titles like CS:GO, Rust, Minecraft, and ARK.
- Humorous, thematic structure: Themed roles and categories to match the "Elevator" concept of the server.
- Moderation roles: Automatically sets up roles for moderators to manage specific games or parts of the server.
- Cybersecurity and development spaces: Provides sections for tech enthusiasts to discuss cybersecurity, development, and network security.
- Channels for rules and server info: Automatically creates channels to display rules and server information to members.

## Prerequisites

- **Python 3.10+**
- **discord.py library** (version 2.0 or higher)
- **Admin access** to the Discord server
- A valid **Discord bot token** from the [Discord Developer Portal](https://discord.com/developers/applications).

## Step-by-Step Guide

###

1. Clone the Repository

```git clone https://github.com/yourusername/elevator-discord-bot.git
cd elevator-discord-bot```

2. Set Up Virtual Environment (optional)
Setting up a virtual environment is recommended to manage dependencies.

```python -m venv env
source env/bin/activate   # On Windows use `env\Scripts\activate````

3. Install Dependencies
Install the required Python libraries.

```pip install -r requirements.txt```

4. Configure the Bot Token
Go to the Discord Developer Portal and create a new application.

Under the "Bot" section, create a bot and copy the token.

In your local environment, set up a .env file or directly insert your bot token into the code (ensure not to commit this file to GitHub).

For .env file setup:

```DISCORD_TOKEN=your-bot-token-here```

5. Run the Bot
Run the bot locally with:

```python bot_script.py```

6. Invite the Bot to Your Server
Go back to the Discord Developer Portal.
Under the "OAuth2" tab, select "URL Generator."
In scopes, select bot.
In bot permissions, select:
Administrator or customize your own permissions.
Copy the generated URL and open it in your browser.
Select the server you want to invite the bot to and authorize it.

7. Use the Bot
Once the bot is added to your server, type the following command in a text channel where the bot has permission:

```!setup_server```

The bot will then automatically create the roles, channels, and categories for you.

File Structure

├── bot_script.py            # Main bot script
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation (this file)

Troubleshooting
If you encounter any issues:

Ensure you have the correct bot token.
Verify the bot has permissions to create roles and channels.
Check your Python version and ensure all dependencies are installed correctly.
Contributing
If you’d like to contribute, feel free to fork this repository and submit a pull request!

This bot is designed to be easily expandable. Feel free to modify the bot to suit your own server needs, add more roles, or adjust permissions as required.


### Additional Notes: ###
- Before pushing to GitHub, ensure you **do not** commit sensitive files such as `.env` containing your bot token.
- The `requirements.txt` file should list the necessary dependencies (like `discord.py`).

Let me know if you need any additional features in the `README.md` or the bot itself!
