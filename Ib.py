import time
from random import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def closeNavegador(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        login_botton = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        # login_bolton = driver.find_element_by_css_selector('button.0mzm-.sqdOP.L3NKy"')
        login_botton.click()
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)

        pic_hrefs =[]

        for i in range(1, 6):

                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)


                hrefs = driver.find_elements_by_tag_name('a')
                hrefs = [elem.get_attribute('href') for elem in hrefs
                 if '.com/p/' in elem.get_attribute('href')]
                #lista de contrucao
                [pic_hrefs.append(href) for href in hrefs if href not in pic_hrefs]
                print('photos: ' + str(len(pic_hrefs)))

                for pic_href in pic_hrefs:
                    driver.get(pic_href)
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    try:
                        driver.find_element_by_css_selector('button.dCJp8.afkep._0mzm-').click()
                        time.sleep(2)
                    except Exception as e:
                        time.sleep(2)

weltonjbs = InstagramBot("weltonjbs", "monyele01")
weltonjbs.login()
weltonjbs.like_photo('lancer')