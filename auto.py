from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui

class auto:
    def __init__(self, username, password, target):
        self.username = username
        self.password = password
        self.target = target
        self.browser = webdriver.Chrome()

    def login(self):
        browser=self.browser
        browser.implicitly_wait(5)  
        browser.get('https://www.instagram.com')
        browser.find_element_by_xpath("//input[@name='username']").send_keys(self.username)
        browser.find_element_by_xpath("//input[@name='password']").send_keys(self.password)  
        browser.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2.5)
        not_now_button = browser.find_element_by_xpath("//button[text()='Not Now']")
        sleep(1)
        not_now_button.click()
        sleep(2.5)
        not_now_button = browser.find_element_by_xpath("//button[text()='Not Now']")
        sleep(1)
        not_now_button.click()

    def Search(self):
        browser=self.browser
        browser.implicitly_wait(5)
        browser.find_element_by_xpath("//span[text()='Search']").click()
        browser.find_element_by_xpath("//input[@placeholder='Search']").send_keys(self.target)
        sleep(2)
        browser.find_element_by_xpath("//span[text()='"+self.target+"']").click()
        sleep(2)
    
    def direct(self):
        browser=self.browser
        browser.implicitly_wait(5)
        browser.get('https://www.instagram.com/direct/inbox/')
        sleep(2)
        browser.get('https://www.instagram.com/direct/new/')
        sleep(2)
        browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/div/div[2]/input").click()
        browser.find_element_by_xpath("//input[@name='queryBox']").send_keys(self.target)
        sleep(5) 
        browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/button/span").click()
        
        


    def message(self):
        browser = self.browser
        browser.implicitly_wait(5)
        browser.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[2]/div/button").click()
        message_area = browser.find_element_by_xpath("//textarea[@placeholder='Message...']")
        message_area.click()
        message_area.send_keys("This is BOT.", Keys.ENTER)
        message_area = browser.find_element_by_xpath("//textarea[@placeholder='Message...']")
        message_area.click()
        f= open("text.txt", 'r')
        for word in f:
            pyautogui.typewrite(word)
            pyautogui.press("enter")

        browser.close()

if __name__ == '__main__':
        #bot = auto('<username>', '<password>', '<target>')
        #bot.login()
        #bot.Search()
        #bot.direct()
        #bot.message()
