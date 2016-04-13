# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.channel import ChannelHelper

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.channel = ChannelHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://10.130.8.116/epg/")

    def destroy(self):
        self.wd.quit()