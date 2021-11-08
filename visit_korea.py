from bs4 import BeautifulSoup
from selenium import webdriver
import time

chromedriver = 'C:\\Users\\bitcamp\\PycharmProjects\\flaskProject\\data'
class VisitKorea(object):
    def __init__(self):

        driver = webdriver.Chrome(chromedriver)
        driver.implicitly_wait(3)
        driver.get('https://logins.daum.net/accounts/signinform.do')
        driver.implicitly_wait(3)

        driver.find_element_by_id('id').send_keys('wendy0310')
        driver.find_element_by_id('inputPwd').send_keys('ekdmagpals')
        driver.find_element_by_id('log.login').click()
        driver.implicitly_wait(3)
        # driver.find_element_by_link_text('검색').click()

if __name__ == '__main__':
    VisitKorea()

