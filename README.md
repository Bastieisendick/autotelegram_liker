# Auto Telegram Liker
This program is a Python Selenium based automation bot.
It reacts to all sent messages in a Telegram Group with a specified emoji reply.
Any occuring errors combined with additional information (screenshots, etc.) will be sent to you via a Telegram Bot.


## Installing
1. Download the source code
2. Make sure Python is installed and ready
3. Install Firefox and download a suitable Geckodriver
4. Install missing dependencies:
    - pyTelegramBotApi (telebot)
	- selenium
5. Change neccessary code parts to your own values. See Neccessary Changes
6. Run python main.py
7. This program is best run by my other project "script-restarter", also available on Github

**Attention: This program requires at least _5 MB_ of space on your hard disk (Including status screenshots, may vary in the future...)**


## Neccessary Changes
In the messageLiker.py file you will have to adapt some values to your own needs:
**chatIdTG**: This is the Id of your Telegram Chat, in which the built in Telegram Bot will inform you over occuring errors. *Example value*: "-1234567890"
**botTokenTG**: This is the Telegram Bot Token, obtainable via Telegram BotFather. *Example value*: "3938944536986873498389:awiudhawiudhoiehfe-wdawdw"
**firefoxProfilePath**: This is the path to your Firefox Profile (enter about:profiles into the search bar to get your paths). The profile has to have Telegram Web already authenticated. It is recommended to create a new profile specifically for this bot. *Example value*: "C:\Users\myPC\AppData\Roaming\Mozilla\Firefox\Profiles\abcdefg.default-release"
**chatURLTG**: This is the URL to the Telegram Web Chat which you want this bot to react on. To obtain it, copy the URL from your browser whilst the Chat is open. *Example value*: "https://web.telegram.org/k/#-1234567890"
**emojiDataDocId**: This is the DataDocId of your preferred emoji reaction. You can get it by using the browser-console and opening the reaction menu (right click on message). It will be an attribute of the reaction-elements element. *Example value*: "12345678901234567890"
**whiteListedText**: This is the text which will not be reacted upon.*Important*: Messages have to be sent by you and must only contain this text for it to not be reacted on. Example: whiteListedText=Hello; MsgsentbyPete=Hello(*reaction*), MsgsentbyPete=Hi! Hello World(*reaction*), MsgsentbyPete=Banana(*reaction*), MsgsentbyYou=Hi! Hello World(*no reaction*), MsgsentbyYou=Hello(*no reaction*), MsgsentbyYou=Banana(*reaction*). *Example value*: "Hello"
**geckoDriverPath**: This is the path to your Firefox geckodriver binary/executable. For browsers installed by snap (Ubuntu for example), most of the time its located in "/snap/bin/geckodriver". *Example value*: "/myPath/geckodriver.exe"

The Telegram Chat in which the bot shall react has to have atleast around 20 (depending on the message loading behaviour) previously self reacted messages for the bot to work.

*Example emojiDataDocId*: "5051019936827179425" is Thumbs up

## Usage
Start the main.py file by entering python main.py into your console.
The Bot will then start and work on the reactions.
The general procedure is as follows:
	1. Work for a randomly specified workTime
		1. Open the browser, and go to **chatURLTG** (https://web.telegram.org/k/#YOURCHATID)
		2. Scroll up a few times, so old messages will be loaded
		3. Get messages and react to them until the workTime is over
		4. Close the browser
		
		If any error occurs, it will be sent via Telegram to inform the User and the browser will be closed and reopened
	
	2. Sleep for a randomly specified sleepTime
	3. Go back to step 1. and repeat until stopped
	
	
You can define your own specific rules to when a message should not be reacted on by writing into the messageLiker.isWhiteListed() function.
There is currently a feature implemented, which lets the bot scroll up endlessly, until it finds around 20 (depending on the message loading behaviour) self reacted messages. This way you wont ever miss any reactions. To disable this I wrote a function called messageLiker.removeOverStartMessages(), which is currently non functional because of a missing unique message Identifier. If you want, you can help by implementing a working solution.

	
	
## Working environments
This program works on Windows and Ubuntu.
It should also work on every other Python, Firefox, Selenium capable system.
Telegram Group chats work, Broadcasts, single chats etc. have not been tested yet.


## Developing Time
Developing of this bot took around 3 Days.
Funny enough, the implementation on a Ubuntu virtual machine took nearly the same amount of time because of corrupted locales, autostarting behaviours and monitoring setups ;)




Using this may result in bans and other desastrous actions regarding for example your Telegram Account. Hereby no guarantees or responsibilities are taken.
