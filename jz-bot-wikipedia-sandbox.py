from selenium import webdriver
from time import sleep

class ASimpleBot:

    def addingmytext(self):
        url = "https://en.wikipedia.org/wiki/Wikipedia:Sandbox"
        mybrowser = webdriver.Chrome(executable_path="/home/minime/Downloads/chromedriver")
        mybrowser.get(url)
        mybrowser.maximize_window()

        sleep(3)
        element1 = mybrowser.find_element_by_link_text("Log in")
        element1.click()
        # OR
        # element1.send_keys("<whatever text you want to enter goes here>")
        sleep(3)

        sleep(3)
        element2 = mybrowser.find_element_by_xpath("/html//input[@id='wpName1']")
        # element2.click()
        # OR
        element2.send_keys("Minime2020")
        sleep(3)

        sleep(3)
        element3 = mybrowser.find_element_by_xpath("/html//input[@id='wpPassword1']")
        # element3.click()
        # OR
        element3.send_keys("mysupersecretpassword")
        sleep(3)

        sleep(3)
        element4 = mybrowser.find_element_by_xpath("/html//button[@id='wpLoginAttempt']")
        element4.click()
        # OR
        # element4.send_keys("<whatever text you want to enter goes here>")
        sleep(3)

        sleep(3)
        element5 = mybrowser.find_element_by_xpath("//li[@id='ca-edit']/a[@title='Edit this page [alt-shift-e]']")
        element5.click()
        # OR
        # element5.send_keys("<whatever text you want to enter goes here>")
        sleep(3)

       

        sleep(3)
        element7 = mybrowser.find_element_by_xpath("/html//textarea[@id='wpTextbox1']")
        # element7.click()
        # OR
        element7.send_keys(" a wonderful world")
        sleep(3)

        sleep(3)
        element8 = mybrowser.find_element_by_xpath("/html//input[@id='wpSave']")
        element8.click()
        # OR
        # element8.send_keys("<whatever text you want to enter goes here>")
        sleep(10)

        # sleep(3)
        # element9 = mybrowser.find_element_by_xpath("<Element's XPATH goes here>")
        # element9.click()
        # OR
        # element9.send_keys("<whatever text you want to enter goes here>")
        # sleep(3)

        # sleep(3)
        # element10 = mybrowser.find_element_by_xpath("<Element's XPATH goes here>")
        # element10.click()
        # OR
        # element10.send_keys("<whatever text you want to enter goes here>")
        # sleep(3)

Iam = ASimpleBot().addingmytext()


