import selenium
from time import sleep


from selenium import webdriver

browser = webdriver.Chrome("C:\\Users\\Administrator\\Downloads\\chromedriver.exe")

a=[]

class Url():
    def run(self):
        browser.get("https://www.computerhope.com/")

class Back():
    def run(self):
            browser.back()
            sleep(.5)
            browser.forward()
            sleep(.5)
            t5.run()

class Allow():
    def run(self):
        print("clicked")
        a.append("b")
        c = len(a)
        print(c)
        elem = browser.find_element_by_link_text('Help')
        elem.click()
        sleep(.2)
        t3.run()

class Image():
    def run(self):
        try:
            ima = browser.find_element_by_xpath('/html/body/div[2]/*')
            if ima.is_displayed():
                print("displayed")
                a = input("press space and enter to allow just enter to skip")
                if a==(" "):
                    t2.run()
                else:
                    t3.run()
        except Exception as E:
            print("Refreshinggggg")
            t3.run()



t1 = Url()
t2 = Allow()
t3 = Back()

t5 = Image()


t1.run()
t5.run()
