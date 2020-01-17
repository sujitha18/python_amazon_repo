'''
@author : sujitha
@email:suji@gmail.com
@dta : 08/01/2020
'''
import time
from lib2to3.pgen2 import driver

from sources.utilities.generic_methods import GenericMethods
from sources.utilities import custom_logger as cv
from sources.pages.home_page_search_product import HomePageSearchProduct
from sources.utilities import excel

import logging
class Applexr128(GenericMethods):
    """
    Select one product and
    click on add to cart
    """
    log = cv.customLogger(logging.DEBUG)
    def __init__(self,driver):
        #we are inheriting GenericMethods for Webdriver(driver) using super keyword
        super().__init__(driver)#is a relation--inheritance
        self.driver=driver
        HomePageSearchProduct(driver)#has a relation
        self.add_to_cart="add-to-cart-button"
        self.verify_mesg_xpath="//h1[@class='a-size-medium a-text-bold']"
        self.product_01_click="//span[contains(text(),'Apple iPhone XR (128GB) - Black')]"
        self.cart_button="hlb-view-cart-announce"
        self.verify_product_link_xpath="//span[contains(text(),'Apple iPhone XR (128GB) - Black')]"
    def add_to_cart_link(self):
        self.elementclick(self.product_01_click,"xpath")
        self.switch_to_child_window(self.driver)
        self.elementclick(self.add_to_cart)
        self.elementclick(self.cart_button)
    def verify_the_page(self):
            actual_link=self.get_text(self.verify_product_link_xpath,"xpath")
            print(actual_link)
            # actual_mesg = self.get_text(self.verify_mesg_xpath,"xpath")
            # expec_mesg =excel.get_value("Cart","Tc_002","SuccessMesg")
            expect_link="Apple iPhone XR (128GB) - Black"
            assert expect_link in actual_link, "Product is not matched---fail"
            print("Product is Matched--pass")
            self.log.info("It is verified that,Pruducts able to match")



