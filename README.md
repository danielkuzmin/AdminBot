# AdminBot
This bot provides quality of life features for Discord mod admins. Written in Python.
## Getting Started
If you'd like to host the bot yourself, these instructions will show you how to get it running on a Linux machine in the background.
### Prerequisites
You will need a machine running Linux, preferably something that can be used as a server, such as a raspberry Pi. You'll need Python 3 on this machine. To check if you already have Python3, run the following command:
```
$ python3 --version
```
If this does not come back with a version number, you will have to install it yourself. Run the following command:
```
$ sudo apt-get install python3.6
```
After this, create a directory and put all the source files from this repository into it.
### Adding Users
To add users with their own phrases and permissions, you'll need to edit the users.json file. Open it with your text editor of choice, and add a user into the users array as such:
```
{
      "name": "Firstname Lastname",
      "ID": IDNumber,
      "admin": true (or false),
      "phrases": ["Test1","You're cool"]
},
```
To get a user's ID number, go to your Discord settings, click on apperance, and enable developer mode. This whill let you right-click on a user to get their ID.
Setting admin to true will give this user access to various admin commands, such as $echo and $mute. Setting it to false will restrict these commands.
### Adding a Token
Create a file called credentials.py in the same directory as the rest of the source files. Generate a bot token from the Discord Developer Portal. Finally, edit credentials.py and paste the following:
```
token = 'YOURUNIQUETOKENGOESHERE'
```
Save the file.
### Running the Bot as a Background Task
In a terminal window, navigate to the directory you put the source files in. Run the following command:
```
$ nohup python3 main.py&
```
This will start the bot. You can close the terminal window, or the SSH window, and the bot will keep running as long as the machine doesn't shut down or lose connection to the internet.
## Using the Bot
This bot uses the prefix '$' and comes with the following commands:
### $adminHello
Prints one of your custom messages at random, as well as your discord ID, name, and whether or not you're an admin.
### $echo
Sends a message into the selected text channel.
Usage example:
```
$echo your message here
```
### $mute
Mutes a user for the given amount of minutes. Usage:
```
$mute @Holland Oates 2
```
### $help
Sends a message containing the bot's command list and a short description with usages of each command to the channel it was invoked in.
