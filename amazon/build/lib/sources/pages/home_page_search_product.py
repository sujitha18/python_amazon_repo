'''
@author : sujitha
@email:suji@gmail.com
@dta : 08/01/2020
'''
import time
from lib2to3.pgen2 import driver
from sources.utilities.generic_methods import GenericMethods
from sources.utilities import custom_logger as cv
import logging

class HomePageSearchProduct(GenericMethods):
    """
    DocString
    Searching Products in Amazone
    and click it...
    """
    log = cv.customLogger(logging.DEBUG)
    def __init__(self,driver):
        #we are inheriting GenericMethods for Webdriver(driver) using super keyword
        super().__init__(driver)
        self.driver=driver
        self.search_product_name="twotabsearchtextbox"

    def searchBox(self,productName):
        #using self keyword we can access the method in genericmethods
        self.sendkeys(productName,self.search_product_name)
        self.elementclick("//span[contains(text(),'Go')]/../input", "xpath")#Searching product and click search button





