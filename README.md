# Auto Telegram Liker
This program is a Python Selenium based automation bot using [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver).<br/>
It reacts to all sent messages in a Telegram Group with a specified emoji reply.<br/>
Any occuring errors combined with additional information (screenshots, etc.) will be sent to you via a Telegram Bot.<br/>


## Installing
1. Download the source code<br/>
2. Make sure Python is installed and ready<br/>
3. Install Google-Chrome and download a suitable chromedriver (Move the chromedriver into the driver/ directory)<br/>
4. Install missing dependencies:<br/>
    - pyTelegramBotAPI (telebot)<br/>
    - selenium<br/>
	- undetected-chromedriver<br/>
5. Change neccessary code parts to your own values. See Necessary Changes<br/>
6. Run python main.py<br/>
7. This program is best run by my other project [script-restarter](https://github.com/Bastieisendick/script-restarter), also available on Github<br/>

**Attention: This program requires at least _20 MB_ of space on your hard disk (Including status screenshots and chromedriver, may vary in the future...)**


## Necessary Changes
In the messageLiker.py file you will have to adapt some values to your own needs:<br/><br/>
**chatIdTG**: This is the Id of your Telegram Chat, in which the built in Telegram Bot will inform you over occuring errors.<br/>*Example value*: "-1234567890"<br/><br/>
**botTokenTG**: This is the Telegram Bot Token, obtainable via Telegram BotFather.<br/>*Example value*: "3938944536986873498389:awiudhawiudhoiehfe-wdawdw"<br/><br/>
**browserProfileName**: This is the name of your Chrome Profile (enter chrome://version into the search bar to get your paths). The profile has to have Telegram Web already authenticated. It is recommended to create a new profile specifically for this bot.<br/>*Example value*: "Profile 1"<br/><br/>
**browserProfilePath**: This is the path of your Chrome Profile parent folder (enter chrome://version into the search bar to get your paths). The profile has to have Telegram Web already authenticated. It is recommended to create a new profile specifically for this bot.<br/>*Example value*: "C:/Users/YOU/AppData/Local/Google/Chrome/User Data/"<br/><br/>
**browserLanguage**: This sets your browser language in which websites will be viewed. Unfortunately, this doesnt work as expected, so its best to set the language preferences in your chrome settings for the profile manually.<br/>*Example value*: "de-DE"<br/><br/>
**browserUserAgent**: This sets your browser user agent.<br/>*Example value*: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"<br/><br/>
**chatURLTG**: This is the URL to the Telegram Web Chat which you want this bot to react on. To obtain it, copy the URL from your browser whilst the Chat is open.<br/>*Example value*: "https://web.telegram.org/k/#-1234567890"<br/><br/>
**emojiDataDocId**: This is the DataDocId of your preferred emoji reaction. You can get it by using the browser-console and opening the reaction menu (right click on message). It will be an attribute of the reaction-elements element.<br/>*Example value*: "5051019936827179425" is Thumbs up<br/><br/>
**whiteListedText**: This is the text which will not be reacted upon.*Important*: Messages have to be sent by you and must only contain this text for it to not be reacted on. Example: whiteListedText=Hello; MsgsentbyPete=Hello(*reaction*), MsgsentbyPete=Hi! Hello World(*reaction*), MsgsentbyPete=Banana(*reaction*), MsgsentbyYou=Hi! Hello World(*no reaction*), MsgsentbyYou=Hello(*no reaction*), MsgsentbyYou=Banana(*reaction*).<br/>*Example value*: "Hello"<br/><br/>


The Telegram Chat in which the bot shall react has to have atleast around 20 (depending on the message loading behaviour) previously self reacted messages for the bot to work.<br/>


## Usage
Start the main.py file by entering python main.py into your console.<br/>
The Bot will then start and work on the reactions.<br/>
The general procedure is as follows:<br/>
	- Work for a randomly specified workTime:<br/>
		1. Open the browser, and go to **chatURLTG** (https://web.telegram.org/k/#YOURCHATID)<br/>
		2. Scroll up a few times, so old messages will be loaded<br/>
		3. Get messages and react to them until the workTime is over<br/>
		4. Close the browser<br/>
		
		
	- Sleep for a randomly specified sleepTime<br/>
	- Go back to step 1. and repeat until stopped<br/>

 If any error occurs, it will be sent via Telegram to inform the User and the browser will be closed and reopened<br/>	
	
	
You can define your own specific rules to when a message should not be reacted on by writing into the messageLiker.isWhiteListed() function.<br/>
There is currently a feature implemented, which lets the bot scroll up endlessly, until it finds around 20 (depending on the message loading behaviour) self reacted messages. This way you wont ever miss any reactions.<br/>
To disable this I wrote a function called messageLiker.removeOverStartMessages(), which is currently non functional because of a missing unique message Identifier. If you want, you can help by implementing a working solution.<br/>

	
	
## Working environments
This program works on Windows, Armbian and Ubuntu.<br/>
It should also work on every other Python, Chrome, Selenium capable system.<br/>
Telegram Group chats work, Broadcasts, single chats etc. have not been tested yet.<br/>


## Developing Time
Developing of this bot took around 3 Days.<br/>
Funny enough, the implementation on a Ubuntu virtual machine took nearly the same amount of time because of corrupted locales, autostarting behaviours and monitoring setups ;)<br/>




Using this may result in bans and other desastrous actions regarding for example your Telegram Account. Hereby no guarantees or responsibilities are taken.
