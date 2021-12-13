from seleniumbase import BaseCase


class HomeTest(BaseCase):
    def test_Verify_Logo(self):
        self.open("https://practice.automationbro.com/")
        self.assert_element("//img[@class='custom-logo']")

    def test_verify_copyright_text(self):
        self.open("https://practice.automationbro.com/")
        self.assert_text("Copyright © 2020 Automation Bro", "//div[@class='tg-site-footer-section-1']//p")

    def test_verify_title(self):
        self.open("https://practice.automationbro.com/")
        self.assert_title("Practice E-Commerce Site – Automation Bro")
