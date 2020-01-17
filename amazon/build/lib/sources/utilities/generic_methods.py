import os
import time
import logging

from traceback import print_stack
from selenium.common.exceptions import NoSuchElementException, ElementNotSelectableException, ElementNotVisibleException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from sources.utilities import custom_logger as cl
from selenium.webdriver.support import expected_conditions as EC

class GenericMethods():
    log=cl.customLogger(logging.DEBUG)
    def __init__(self,driver):
        self.driver=driver
    def screenShot(self,resultMessage):
        #take screenshot f the current open the web pge
        fileName=resultMessage+"."+str(round(time.time()*1000))+".png"
        screenshotDirectory="../screenshots/"
        relativeFilename=screenshotDirectory+fileName
        currentDirectory=os.path.dirname(__file__)
        destinatiomFile=os.path.join(currentDirectory,relativeFilename)
        destinationDirectory=os.path.join((currentDirectory,screenshotDirectory))
        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinatiomFile)
            self.log.info("screenshot save the directory:"+destinatiomFile)
        except:
            self.log.error("### Exception occured")
            print_stack()
    def get_Title(self):
        title=None
        try:
            title=self.driver.title
            self.log.info("Able to fetch the Title")
        except:
            self.log.info("### Not Able to fetch the Title###:")
        return title
    def getByType(self,locatorType):
        locatorType=locatorType.lower()
        if locatorType=="id":
            return By.ID
        elif locatorType=="name":
            return By.NAME
        elif locatorType=="xpath":
            return By.XPATH
        elif locatorType=="css":
            return By.CSS_SELECTOR
        elif locatorType=="link":
            return By.LINK_TEXT
        elif locatorType=="class":
            return By.CLASS_NAME

        else:
            self.log.info("Locator type"+locatorType+"Not correct/support")
            return False
    def getElement(self,locator,locatorType="id"):
        element=None
        try:
            locatorType=locatorType.lower()
            bytype=self.getByType(locatorType)
            element=self.driver.find_element(bytype,locator)
            self.log.info("Element found with locator:"+locator+"and locator type:"+locatorType)
        except:
            self.log.info("Element not found with locator:"+locator+"and locatortype:"+locatorType)
        return element
    def clearText(self,locator,locatorType="id"):
        try:
            self.getElement(locator,locatorType).clear()
            self.log.info("Text field is cleared with locator:" + locator + "and locator type:" + locatorType)
        except:
            self.log.info("### Not able to clear###:" + locator + "and locatortype:" + locatorType)

    def elementclick(self,locator,locatorType="id"):
        try:
            element=self.getElement(locator,locatorType)
            element.click()
            self.log.info("Clicked on the Element locator:" + locator + "and locator type:" + locatorType)
        except:
            self.log.info("Cannot click on the Element with locator:" + locator + "and locatortype:" + locatorType)
    def isElementPresent(self,locator,locatorType="id"):
         try:
             element=self.getElement(locator,locatorType)
             if element is not None:
                 self.log.info("Element found")
                 return True
             else:
                 self.log.info("Element not found")
                 return False
         except:
             self.log.info("Element not found")
             return False
    def elementPresenceCheck(self,locator,byType):
        try:
            elementlist=self.driver.find_elements(byType,locator)
            if len(elementlist) > 0:
                self.log.info("Element found")
                return True
            else:
                self.log.info("Element not found")
                return  False
        except:
            self.log.info("Element not found")
            return False
    def waitForElement(self,locator,locatorType="id",timeout=10,Pollfrequency=0.5):
        element=None
        try:
            byType=self.getByType(locatorType)
            self.log.info("waiting for maximum::"+str(timeout)+"::seconds for element to be clickable")
            wait=WebDriverWait(self.driver,timeout=10,poll_frequency=Pollfrequency,ignored_exceptions=
                                    [NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])
            element=wait.until(EC.element_to_be_clickable(byType,locator))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
            return element
    def sendkeys(self,data,locator,locatorType="id"):
        try:
            element=self.getElement(locator,locatorType)
            element.send_keys(data)
            self.log.info("send data on th element with the locator:"+locator+"Locator Type"+locatorType)
        except:
            self.log.info("Cannot send data on the element with locator:"+locator+"Locator Type"+locatorType)
            print_stack()
    def switch_to_child_window(self,driver):
        child_window=None
        parent_window=driver.current_window_handle
        window_ids=driver.window_handles
        try:
            for window_id in window_ids:
                if window_id != parent_window:
                    child_window=window_id
                    break
            driver.switch_to.window(child_window)
        except Exception:
            self.log.info("Unable to change the focus to the child window")
            print_stack()
    def timeSleep(self,time_secs):
        time.sleep(time_secs)
    def get_url(self):
        url = None
        try:
            url = self.driver.current_url
            self.log.info("Able to fetch the current url")
        except:
            self.log.info("### Not Able to fetch the current url###:")
        return url
    def get_text(self,locator,locatorType="id"):
        text=None
        try:
            element = self.getElement(locator, locatorType)
            text=element.text
            self.log.info("Get Text on th element with the locator:" + locator + "Locator Type" + locatorType)
        except:
            self.log.info("Cannot Get Text on the element with locator:" + locator + "Locator Type" + locatorType)
        return text