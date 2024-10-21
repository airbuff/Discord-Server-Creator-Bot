import discord
from discord.ext import commands
import logging

logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

TOKEN = 'YOUR_BOT_TOKEN_HERE'  # Replace with your actual token, preferably from an environment variable

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    logging.info(f'Bot is ready: {bot.user.name}')

@bot.command()
@commands.has_permissions(administrator=True)
async def setup_server(ctx):
    guild = ctx.guild

    # Create Roles with Permissions
    roles = {
        '🛗 Elevator Operator': discord.Permissions(administrator=True),
        '🎮 Game Floor Supervisor': discord.Permissions(manage_messages=True, kick_members=True, mute_members=True),
        '🔧 Basement Engineer': discord.Permissions(manage_messages=True, kick_members=True, mute_members=True),
        '🕵️ Back Alley Bouncer': discord.Permissions(manage_messages=True, kick_members=True, mute_members=True),
        '🎟️ VIP Pass Holder': discord.Permissions(read_messages=True, send_messages=True, connect=True, speak=True),
        '🚶 Elevator Rider': discord.Permissions(read_messages=True, send_messages=True, connect=True, speak=True),
        '💤 Idle Rider (AFK)': discord.Permissions(read_messages=True, connect=True)
    }

    created_roles = {}
    for role_name, permissions in roles.items():
        role = await guild.create_role(name=role_name, permissions=permissions)
        created_roles[role_name] = role
        logging.info(f'Created role: {role_name} with permissions')

    # Create Categories and Channels
    categories_and_channels = {
        "🛗 The Elevator": [],
        "🏢 Lobby (General)": [
            ("💬 Chiddy Chats", discord.ChannelType.text),
            ("🙈 Underbelly", discord.ChannelType.text, True),  # NSFW
            ("🕶️ Back Alley", discord.ChannelType.text, True),  # NSFW
            ("🗣️ Small Talk", discord.ChannelType.voice),
            ("🍹 Hookah Lounge", discord.ChannelType.voice)
        ],
        "🎮 Game Floors (Gaming)": [
            ("🔫 CS:GO Penthouse", discord.ChannelType.text),
            ("🏚️ Rust Roof", discord.ChannelType.text),
            ("⛏️ Blockworks", discord.ChannelType.text),
            ("🦖 Dino Den", discord.ChannelType.text),
            ("🎙️ CS:GO Arena", discord.ChannelType.voice),
            ("🏕️ Rust Outpost", discord.ChannelType.voice),
            ("🌳 Minecraft Village", discord.ChannelType.voice),
            ("🦕 ARK Wilderness", discord.ChannelType.voice)
        ],
        "💻 Tech Basement (Cybersecurity & Development)": [
            ("🔐 Cyber Deck", discord.ChannelType.text),
            ("🌐 Network Nook", discord.ChannelType.text),
            ("👨‍💻 Dev Den", discord.ChannelType.text),
            ("🕹️ Cyber Control Room", discord.ChannelType.voice),
            ("🖥️ Code Cubicle", discord.ChannelType.voice)
        ],
        "🛠️ Elevator Control Room (Admin and Support)": [
            ("📜 Elevator Rules", discord.ChannelType.text),
            ("🎟️ Join the Ride", discord.ChannelType.text),
            ("🆘 Support Booth", discord.ChannelType.text)
        ],
        "💤 AFK Shaft (Idle users)": [
            ("😴 AFK", discord.ChannelType.voice)
        ]
    }

    for category_name, channels in categories_and_channels.items():
        category = await guild.create_category(category_name)
        logging.info(f'Created category: {category_name}')

        # Set up category permissions
        await category.set_permissions(created_roles['🛗 Elevator Operator'], overwrite=discord.PermissionOverwrite(administrator=True))
        await category.set_permissions(created_roles['🚶 Elevator Rider'], overwrite=discord.PermissionOverwrite(read_messages=True, send_messages=True, connect=True, speak=True))

        for channel_info in channels:
            if len(channel_info) == 2:
                channel_name, channel_type = channel_info
                is_nsfw = False
            else:
                channel_name, channel_type, is_nsfw = channel_info

            if channel_type == discord.ChannelType.text:
                channel = await category.create_text_channel(channel_name, nsfw=is_nsfw)
            else:
                channel = await category.create_voice_channel(channel_name)

            # Set up channel-specific permissions
            if "🎮 Game Floors" in category_name:
                await channel.set_permissions(created_roles['🎮 Game Floor Supervisor'], overwrite=discord.PermissionOverwrite(manage_messages=True, mute_members=True))
            elif "💻 Tech Basement" in category_name:
                await channel.set_permissions(created_roles['🔧 Basement Engineer'], overwrite=discord.PermissionOverwrite(manage_messages=True, mute_members=True))
            elif channel_name in ["🙈 Underbelly", "🕶️ Back Alley"]:
                await channel.set_permissions(created_roles['🕵️ Back Alley Bouncer'], overwrite=discord.PermissionOverwrite(manage_messages=True, mute_members=True))
                await channel.set_permissions(created_roles['🚶 Elevator Rider'], overwrite=discord.PermissionOverwrite(read_messages=False))
            elif channel_name == "🍹 Hookah Lounge":
                await channel.set_permissions(created_roles['🎟️ VIP Pass Holder'], overwrite=discord.PermissionOverwrite(read_messages=True, send_messages=True, connect=True, speak=True))
                await channel.set_permissions(created_roles['🚶 Elevator Rider'], overwrite=discord.PermissionOverwrite(read_messages=False, connect=False))

            logging.info(f'Created channel: {channel_name} ({"NSFW" if is_nsfw else "SFW"})')

    # Set up AFK channel
    afk_channel = discord.utils.get(guild.voice_channels, name="😴 AFK")
    if afk_channel:
        await guild.edit(afk_channel=afk_channel, afk_timeout=300)  # 5 minutes timeout
        logging.info('Set up AFK channel')

    await ctx.send("Server setup complete with roles, permissions, and emojis! 🎉")
    logging.info(f'Server setup completed for guild: {guild.name}')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.MissingPermissions):
        await ctx.send("You don't have the required permissions to use this command. 🚫")
    elif isinstance(error, commands.errors.CommandNotFound):
        await ctx.send("Command not found. Please check the command and try again. 🔍")
    else:
        print(f"An error occurred: {error}")
        await ctx.send(f"An error occurred: {error} ❌")
    logging.error(f'Command error: {error}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! 🏓')
    logging.info(f'Ping command used by {ctx.author} in {ctx.guild.name}')

@bot.event
async def on_message(message):
    logging.info(f"Message received: {message.content}")
    await bot.process_commands(message)

# Start the bot
try:
    bot.run(TOKEN)
except Exception as e:
    print(f"Failed to start bot: {e}")
    logging.error(f"Failed to start bot: {e}")
