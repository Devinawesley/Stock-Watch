from selenium.webdriver.firefox.options import Options
from threading import Thread
import concurrent.futures
from itertools import repeat
import StockWatch
from twilio.rest import Client

#list of strings of full URLs of each item to watch
itemURLs = [""]

#API key and secret provided by twilio
twilioKey = ""
twilioSecret = ""
client = Client(twilioKey, twilioSecret)

#phone numbers as strings in format "+55555555555"
twilioNumber = ""
textToNumber = ""

#full path to geckodriver.exe
driverPath = r""

#full path to firefox.exe
firefoxLocation = Options()
firefoxLocation.binary_location = r""

#class name for add to cart button on www.microcenter.com is "STBTN". Some sites like Walmart use the same class name for
#out of stock as add to cart. In this case you'll want to add a conditional to the StockWatch module to check the innerText property
#using .get_property('innerText') method
#right click > inspect element on the web page. Dig around until you find the right class name for the website.
elementClassName = ""

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(itemURLs)) as executor:
        executor.map(
        StockWatch.WatchPage, 
        itemURLs, 
        repeat(twilioNumber), 
        repeat(textToNumber), 
        repeat(driverPath), 
        repeat(firefoxLocation),
        repeat(elementClassName),
        repeat(client))



        
