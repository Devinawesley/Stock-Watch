from selenium.webdriver.firefox import webelement
from twilio.rest import Client
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from datetime import datetime
import time

def SendText(itemURL, twilioNumber, textToNumber, client):
    client.messages.create(to=textToNumber,
                        from_=twilioNumber,
                        body="IN STOCK! " + itemURL)
    print(str(datetime.now()) + " In stock, text sent to " + textToNumber)

def WatchPage(itemURL, twilioNumber, textToNumber, driverPath, firefoxLocation, elementClassName, client):
    driver = webdriver.Firefox(options=firefoxLocation, executable_path=driverPath)
    outOfStock = True
    while outOfStock == True:
        driver.get(itemURL)
        if driver.find_elements_by_class_name(elementClassName):
            SendText(itemURL, twilioNumber, textToNumber, client)
            outOfStock = False
        else:
            print(str(datetime.now()) + " Not in stock.")
            time.sleep(5)
