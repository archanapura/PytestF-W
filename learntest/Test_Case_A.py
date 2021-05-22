import pytest


class Test_A:
    def test_case(self,chrome_browser):
        print("first case")


    # @pytest.mark.parametrize("url", [("http://www.gmail.com"), ("http://www.flipkart.com"), ("http://www.amazon.com")])
    #def test_something_quick(url):
    @pytest.mark.parametrize("browser", [('Chrome'),('firefox')])
    def test_browser_name(self,browser):
        print(browser)