import time
import telebot
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc


from sleepRandomTime import sleepRand



chatIdTG = "ENTER YOUR TELEGRAM CHAT ID HERE"
botTokenTG = """ENTER YOUR TELEGRAM BOT API TOKEN HERE"""
browserProfileName = "ENTER YOUR BROWSER PROFILE NAME HERE"
browserProfilePath = "ENTER YOUR BROWSER PROFILE PATH HERE"
browserLanguage = "ENTER YOUR BROWSER LANGUAGE HERE"
browserUserAgent = "ENTER YOUR BROWSER USER AGENT HERE"
driverExecutablePath = "driver/chromedriver"

chatURLTG = "ENTER YOUR TELEGRAM WEB CHAT URL HERE"
emojiDataDocId = "ENTER YOUR REACTION EMOJI ID HERE"
whiteListedText = "ENTER YOUR WHITELISTED TEXT HERE"





def work(workTime):

    bot = telebot.TeleBot(botTokenTG)
    endTime = time.time() + workTime

    browserPointer = [None,]
    while time.time() < endTime:

        try:
            procedure(browserPointer, endTime)
            closeBrowser(browserPointer)

        except Exception as e:
            closeBrowser(browserPointer)
            try:
                bot.send_message(chatIdTG, "Error in work loop\n\n" + str(e))
                print("Error in work loop\n\n" + str(e))

                try:
                    lastStatusText = ""
                    with open("last_status.txt") as statusFile:
                        lastStatusText = statusFile.read()

                    bot.send_photo(chatIdTG, photo = open("last_status.png", 'rb'), caption = lastStatusText)

                except Exception as eee:
                    print("Error while sending last status screenshot\n\n" + str(eee))

            except Exception as ee:
                print("Internet error?")
                print(ee)

            sleepRand(187.372, 230.184)

        closeBrowser(browserPointer)



def closeBrowser(browserPointer):
    try:
        browserPointer[0].quit()            #the browserPointer was added to being able to quit the browser in the procedure loop, as all errors are caught here 
    except:
        pass
    browserPointer[0] = None


def procedure(browserPointer, endTime):

    options = uc.ChromeOptions()
    options.add_argument('--user-agent="' + browserUserAgent + '"')

    prefs = {
        "intl.accept_languages": browserLanguage,           #Also change the language in the settings of your used Chrome profile
        "intl.selected_languages": browserLanguage
    }

    options.add_experimental_option("prefs", prefs)

    options.add_argument("--user-data-dir=" + browserProfilePath)
    options.add_argument("--profile-directory=" + browserProfileName)

    browserPointer[0] = uc.Chrome(options=options, driver_executable_path=driverExecutablePath)
    browser = browserPointer[0]

    sleepRand(10.365, 12.426)

    browser.set_window_size(820,1180)

    login(browser)
    saveStatus(browser, "Logged in...")

    scrollUp(browser)
    saveStatus(browser, "Scrolled up...")

    while time.time() < endTime:

        messageElements = getMessages(browser)

        unlikedMessages = getUnlikedMessages(browser, messageElements)

        if(len(unlikedMessages) > 0):
            likeMessage(browser, unlikedMessages[0])
            saveStatus(browser, "Liked Message...")

        else:
            browser.execute_script("arguments[0].scrollIntoView(true);", messageElements[-1])

        sleepRand(22.526, 44.184)






def getMessages(browser):

    messageElements = []

    messagesParentGroups = browser.find_elements(By.CLASS_NAME, "bubbles-date-group")

    for _messagesParentGroup in messagesParentGroups:

        messagesContainerGroup = _messagesParentGroup.find_elements(By.CLASS_NAME, "bubbles-group")

        for messageContainer in messagesContainerGroup:

            messageElements.extend(messageContainer.find_elements(By.XPATH, "./div[@data-mid]"))

    return messageElements




def login(browser):

    browser.get(chatURLTG)

    sleepRand(20.231, 25.949)



def scrollUp(browser):

    for i in range(3):

        messageElements = getMessages(browser)

        browser.execute_script("arguments[0].scrollIntoView(true);", messageElements[0])

        sleepRand(11.262, 18.376)

        saveStatus(browser, f"Scrolled up for {i}. time...")



def likeMessage(browser, message):

    browser.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", message)

    sleepRand(1.253, 2.35)
    saveStatus(browser, "Liking Message scrollIntoView1...")
    
    actions = ActionChains(browser)
    actions.context_click(message).perform()

    sleepRand(1.534, 2.78)
    saveStatus(browser, "Liking Message performed right click...")

    emojiReactionDiv = browser.find_element(By.CSS_SELECTOR, '.btn-menu-reactions-reaction-select[data-doc-id="' + emojiDataDocId + '"]')
    emojiReactionDivParent = emojiReactionDiv.find_element(By.XPATH, '..')
    emojiReactionElement = emojiReactionDivParent.find_element(By.XPATH, '..')

    browser.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", emojiReactionElement)
    
    sleepRand(1.769, 2.903)
    saveStatus(browser, "Liking Message scrollIntoView2...")

    emojiReactionElement.click()

    sleepRand(7.467, 9.778)
    saveStatus(browser, "Liking Message performed left click...")




def getUnlikedMessages(browser, messageElements):

    unlikedMessages = []

    for msg in messageElements:
        try:
            if(not isWhiteListed(msg)):

                reactions_element = msg.find_element(By.CSS_SELECTOR,"reactions-element")

                if(reactions_element):

                    chosenReactionElement = reactions_element.find_element(By.XPATH, ".//reaction-element[contains(concat(' ', @class, ' '), ' is-chosen ')]")

                    if(not chosenReactionElement):
                        unlikedMessages.append(msg)

                else:
                    unlikedMessages.append(msg)

        except NoSuchElementException:
            unlikedMessages.append(msg)

    return unlikedMessages





def isWhiteListed(msgElement):

    try:

        ownMessage = msgElement.find_element(By.XPATH, ".//*[contains(text(), '" + whiteListedText + "')]")        #check if trigger text is in message
        elementClasses = msgElement.get_attribute("class")

        if("hide-name" in elementClasses and "is-out" in elementClasses):           #check if message was sent by me
            return True

    except NoSuchElementException:
        pass

    return False





def saveStatus(browser, text):

    browser.save_screenshot("last_status.png")
    with open("last_status.txt", "w") as f: f.write(text)




#Possible endless scrolling prevention (not working):


#in procedure:
#startMessageDataMid = getMessages(browser)[0].get_attribute("data-mid")

#in getUnlikedMessages: 
#unlikedMessages = removeOverStartMessages(startMessageDataMid, unlikedMessages)

#def removeOverStartMessages(startMessageDataMid, messageElements):                             #This function should delete/clean the unlikedMessages list from messages that were sent higher than the highest scrolled message. This prevents endless scrolling until the last liked messages were found

#    Option 1:
#    beforeStart = []
#    afterStart = []

#    found = False
#    for element in messageElements:

#        if(found == False):
#            if(element.get_attribute("data-mid") == startMessageDataMid):
#                found = True
#                afterStart.append(element)
            
#            else:
#                beforeStart.append(element)
                                                                                #Both of these versions currently do not work, if you want to try it:) (A unique message Identifier is needed, data-mid attribute is not persistent...)
#        else:
#            afterStart.append(element)

#    if(len(afterStart) > 0):
#        messageElements = afterStart

#    else:
#        messageElements = beforeStart

#    return messageElements

#    Option 2: return messageElements[messageElements.index(startMessage):] if startMessage in messageElements else messageElements





