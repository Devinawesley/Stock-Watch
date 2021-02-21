from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox import webelement
from selenium.common.exceptions import NoSuchElementException
from twilio.rest import Client
import time
from datetime import datetime

firefoxLocation = Options()


#full URL of item to watch
itemURL = ""

#API key and secret provided by twilio
twilioKey = ""
twilioSecret = ""

#phone numbers as strings in format "+55555555555"
twilioNumber = ""
textToNumber = ""

#full path to geckodriver.exe
driverPath = r""

#full path to firefox.exe
firefoxLocation.binary_location = r""


driver = webdriver.Firefox(options=firefoxLocation, executable_path=driverPath)
outOfStock = True
client = Client(twilioKey, twilioSecret)
while outOfStock == True:

    driver.get(itemURL)
    try:
        elem = driver.find_element_by_class_name("spin-button-children")

        if elem.get_attribute('innerText') == "Add to cart":
            print(str(datetime.now()) +" In stock!")
            client.messages.create(to=textToNumber,
                                    from_=twilioNumber,
                                    body="IN STOCK! " + itemURL)
            outOfStock = False
        else:
            print(str(datetime.now()) + " Not in stock.")
            time.sleep(3)
    except NoSuchElementException:
        print(str(datetime.now()) + " No such element found")
        time.sleep(5)
        

