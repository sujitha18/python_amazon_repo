from sources.pages.home_page_search_product import HomePageSearchProduct
from sources.pages.apple_xr_128gb import Applexr128
from sources.utilities.webdriver_factory import WebDriverFactory

class Test_Amazon(WebDriverFactory):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
    def searchProduct(self,name):
        HomePageSearchProduct(self.driver).searchBox(name)

    def clickTab(self):
        Applexr128(self.driver).add_to_cart_link()










