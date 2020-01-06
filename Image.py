import pyautogui

import selenium

from time import sleep





from selenium import webdriver



browser = webdriver.Chrome("C:\\Users\\Administrator\\Downloads\\chromedriver.exe")



class Url():

    def run(self):

        browser.get("https://www.computerhope.com/")





class Help():

    def run(self):

        elem = browser.find_element_by_link_text('Help')

        elem.click()

        sleep(3)





class Next():

    def run(self):

        elem = browser.find_element_by_link_text('Page categories')

        elem.click()

        sleep(3)





class Back():

    def run(self):

            sleep(1)

            browser.back()







class Image():

    def run(self):

        try:

            ima = browser.find_element_by_xpath('/html/body/div[2]/header/a/img')

            if ima.is_displayed():

                print ("u dont have the opertunity to learn more")





        except Exception as e:

            ima2 = browser.find_element_by_xpath('/html/body/div[2]/header/img')

            if ima2.is_displayed():

                print("it's page1")







t1 = Url()

t2 = Help()

t3 = Back()

t4 = Next()

t5 = Image()





t1.run()

t2.run()

t3.run()





A = input("enter1")

if A == ("1"):

    print("true")

    t5.run()

else:

    t4.run()
