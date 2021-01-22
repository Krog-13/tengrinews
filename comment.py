import requests
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from datetime import date
import time

class Comment:
    site = 'https://www.tengrinews.kz'
    HEADERS = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
               'accept': '*/*'}
    comment = []
    #inicialisation drive for chrome
    def __init__(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome('/home/krog/PycharmProjects/parse/chromedriver')

    def get_comments(self, links):
        """info about posts"""
        com = []
        for link in links:
            self.driver.get(link[1])
            time.sleep(20)
            #button = self.driver.find_element_by_xpath("//i[@class='tn-icon-arrow-up-dark']")
            button = self.driver.find_element_by_xpath("//span[@class='']")
            button.click()
            name = self.driver.find_element_by_class_name('tn-user-name')
            text_comment = self.driver.find_element_by_class_name('tn-comment-item-content-text')
            com.append(link[0])
            com.append(name.text)
            com.append(text_comment.text)
            self.comment.append(com)
        self.driver.close()
        return self.comment




if __name__ == '__main__':

    test = Comment()

