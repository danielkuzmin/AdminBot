# This is the main bot file, contains the code of all of the commands
import random
import discord

# Array of user objects, imported from users.json
from parseData import userArray
# This file contains the token
from credentials import TOKEN

print(f'AdminBot is connecting to servers...')

# GUILD - The name of the server
GUILD = discord.guild
# Version Number
VERSION = "v0.9 - ALPHA BUILD"

helpBlock = "```-------------------------adminBot HELP-------------------------" \
            "\n$adminHello - Prints one of your custom messages at random" \
            "\n$echo - Sends a message in a channel on a server, Ex: $echo Hi everyone!" \
            "\n$mute - Mutes the tagged user and prevents them from talking in VC for the given " \
            "amount of time in minutes Ex: $mute @Holland Oates#3521 5" \
            "\n$about - Prints information about the current version of the bot" \
            "\n$help - Prints this help block" \
            "```"
# This string is sent when a user tries to DM the bot a command that can't be used from DMs
noDM = "```This command cannot be used from DMs. Try it from a channel in a server. ```"
# This string is sent when someone without admin permissions attempts to use an admin command
noAdmin = "```You do not have the proper permissions to invoke this command. ```"

client = discord.Client()


# Returns true if the user is an admin, false if they aren't
def is_admin(user):
    return user.admin

# Initial bot joining Discord (only prints to console)
@client.event
async def on_ready():
    # Show: playing "say $help"
    game = discord.Game("say $help")
    await client.change_presence(status=discord.Status.online, activity=game)

    servers = list(client.guilds)
    print("Connected to", str(len(client.guilds)) + " servers:")
    for x in range(len(servers)):
        print(' ', servers[x-1].name)


# Server join message
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to the server!')

# Listens for commands
@client.event
async def on_message(message):
    # -----ADMINHELLO COMMAND-----
    if message.content == '$adminHello':
        print("$adminHello command invoked")
        for x in userArray:
            if message.author.id == x.ID:
                response = "```" + random.choice(x.phrases) + "\nIs Admin: " + str(is_admin(x)) + \
                           "\nDiscord Account ID: " + str(x.ID) + "\nName: " + x.name + "```"
                await message.channel.send(response)
                break

    # -----HELP COMMAND-----
    # Prints the help block to the channel it was invoked in
    if message.content == '$help':
        print("$help command invoked, printing help block")
        await message.channel.send(helpBlock)

    # -----ABOUT COMMAND-----
    if message.content == '$about':
        print("&about command invoked")
        message = "AdminBot" + VERSION + " https://github.com/danielkuzmin"
        await message.channel.send(message)

    # -----ECHO COMMAND-----
    # Echos a message given by a user into another channel (checks for admin rights first)
    if message.content.startswith("$echo") and not message.author == client.user:
        # If message came from a DM
        if message.guild is None:
            await message.channel.send(noDM)
        # If the message came from a server's channel
        else:
            print("Echo command invoked")
            for x in userArray:
                if message.author.id == x.ID:
                    # Checks if the user is an administrator
                    if not is_admin(x):
                        await message.channel.send(noAdmin)
                    else:
                        try:
                            echo_message = message.content.split(' ')[1]
                        except:
                            await message.channel.send("```Usage: $echo followed by the message you'd like to send ```")
                            break
                        # Create the final string to echo into the channel
                        final_message = ''
                        iter_words = iter(message.content.split(' '))
                        next(iter_words)
                        for word in iter_words:
                            final_message = final_message + word + ' '

                        await message.channel.send("Which channel would you like to send this message to?")
                        this_guild = message.guild
                        text_channel_count = 1
                        text_channels = []
                        for channel in this_guild.channels:
                            if str(channel.type) == "text":
                                c_name = "```" + str(text_channel_count) + ' - ' + str(channel.name) + "```"
                                await message.channel.send(c_name)
                                text_channels.append([text_channel_count, channel])
                                text_channel_count = text_channel_count + 1

                        # Function to find the channel given the key
                        def find_channel(channels, key):
                            index = 0
                            for c in channels:
                                if channels[index][0] == key:
                                    return channels[index][1]
                                else:
                                    index += 1

                        # Checks to make sure the second message was sent by the same author and in the same channel
                        def check(m):
                            return m.channel == channel and m.author == message.author

                        # Waits for a message
                        msg = await client.wait_for('message', check=check)
                        if msg:
                            try:
                                selected_channel = find_channel(text_channels, int(msg.content))
                                print("Sending message:", final_message)
                                await selected_channel.send(final_message)
                            except:
                                print('Invalid input')
                                m = "```Invalid usage, please enter the number of a text channel.```"
                                await message.channel.send(m)

    # -----MUTE COMMAND-----
    # Adds a "muted" role to the target for a specified amount of time (checks for admin rights first)
    if message.content.startswith("$mute") and not message.author == client.user:
        # If message came from a DM
        if message.guild is None:
            await message.channel.send(noDM)
        # If the message came from a server's channel
        else:
            for x in userArray:
                if message.author.id == x.ID:
                    # Checks if the user is an administrator
                    if not is_admin(x):
                        await message.channel.send(noAdmin)
                    else:
                        try:
                            mute_target = message.content.split(' ')[1]
                            mute_time = message.content.split(' ')[2]
                        except:
                            await message.channel.send("```Usage: $mute followed by the person you'd "
                                                       "like to mute followed by the number of minutes"
                                                       " you want to mute them for.\n"
                                                       "Ex: $mute @Holland Oates#3521 1 ```")
                            break

client.run(TOKEN)
