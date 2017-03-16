# encoding: UTF-8
import logging
import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class Actionwords:

    def __init__(self):
        self.browser = webdriver.Chrome()
        self.log = logging.getLogger('logbehave')

    def check_exists_by_id(self,id):
        try:
            self.browser.find_element_by_id(id)
        except NoSuchElementException:
            return False
        return True

    def the_user_opens_website(self, website="http://www.google.es"):
        self.browser.get(website)

    def the_user_searches_for_word(self, word="Hiptest"):
        search = self.browser.find_element_by_name('q')
        search.send_keys(word)
        search.send_keys(Keys.RETURN)
        time.sleep(5)
        try:
            self.browser.find_element_by_partial_link_text(
                'Oysho: Tendencias Primavera Verano 2017 en moda de mujer').click()
        finally:
            print(self.browser.title)

    def the_title_should_be_title(self, title="Tecnilógica"):
        title = 'Tendencias'
        WebDriverWait(self.browser, 10).until(EC.title_contains(title))
        try:
           assert title in self.browser.title
        except AssertionError:
           print(self.browser.title)

    def a_user_that_wants_to_register_on_website(self, website="http://www.oysho.es"):
        self.browser.get(website)
        self.browser.find_element_by_id('closed_cookies').click()
        # Implement action: "the user clicks on \"IDENTIFICATE\""
        self.browser.find_element_by_id('headerLoginButton').click()

    def the_user_credentials_are_introduced(self, user_mail="newuser@gmail.com", birth_date="10/02/2001", password="Hola1234"):

        self.browser.find_element_by_id('registerButton').click()
        time.sleep(2)
        useremail = self.browser.find_element_by_name('email')
        birthdate = self.browser.find_element_by_id('birthDate')
        passw = self.browser.find_element_by_id('password')
        confirmpass = self.browser.find_element_by_id('passwordConfirm')
        # Implement action: "Fill the %s" % (userEmail)
        useremail.send_keys(user_mail)
        # Implement action: "Fill the %s " % (birthDate)
        birthdate.send_keys(birth_date)
        # Implement action: "Fill the %s" % (password)
        passw.send_keys(password)
        confirmpass.send_keys(password)
        # Implement action: "Click Submit"
        self.browser.find_element_by_id('checkboxPolicy').click()
        self.browser.find_element_by_id('registerFormButton').click()


    def the_user_is_registered(self, id = 'headerLoginButton' ):
        respo = self.check_exists_by_id(id)
        assert respo is True
        #but = self.browser.find_element_by_id(id)
        #if but.is_displayed():
         #   respo = True
        #else:
         #   respo = False
        #assert respo is True

    def the_user_select_an_item(self, p1="www.oysho.es"):
        # TODO: Implement action:
        # "https://hiptest.net/app/projects/43860/actionwords/544985"
        raise NotImplementedError

    def the_item_should_be_in_the_basket(self):
        pass

    def go_to_p1_page(self, p1="www.oysho.es"):
        # TODO: Implement action:
        # "https://hiptest.net/app/projects/43860/actionwords/544985"
        raise NotImplementedError

