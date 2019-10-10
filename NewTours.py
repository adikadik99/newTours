import unittest
from selenium import webdriver
import HtmlTestRunner

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="//Users/adik/Downloads/chromedriver")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def test_search_1(self):
        self.driver.get("http://newtours.demoaut.com/")
        self.driver.find_element_by_xpath("//input[@name='userName']").send_keys("mercury")
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys("mercury")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//input[@name='login']").click()
        x=self.driver.title
        print (x)
        self.assertEqual(x,"Find a Flight: Mercury Tours:")
        self.driver.save_screenshot("Users/adik/Desktop/jjj.png")
    @classmethod
    def tearDownClass(cls):
      cls.driver.close()
      cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="//Users/adik/Downloads"),verbosity=2)

