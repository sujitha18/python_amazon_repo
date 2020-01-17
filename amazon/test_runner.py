import pytest
from test_scripts.test_cases.test_amazon import *

from sources.utilities import excel
@pytest.mark.usefixtures("oneTimeSetUp")
class Test_AmazonProj():
    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.ta=Test_Amazon(self.driver)

    def test_tc_001_add_product_and_verify(self):
        self.ta.searchProduct(excel.get_value("Cart","Tc_002","ProductName"))
    def test_tc_002_click_link_and_verify(self):
        self.ta.clickTab()



