from seleniumbase import BaseCase

class test_ContactPage(BaseCase):

    def test_verify_contact_page_title(self):
        self.maximize_window()
        self.open("https://practice.automationbro.com/contact/")
        self.assert_title("Contact – Practice E-Commerce Site")

    def test_verify_contact_form_submission(self):
        self.maximize_window()
        self.open("https://practice.automationbro.com/contact/")
        self.scroll_to_element("//h3[contains(text(),'Send Us Message')]")
        self.send_keys("//input[@id='evf-277-field_ys0GeZISRs-1']","Subrata K Bhowmik")
        self.send_keys("//input[@id='evf-277-field_LbH5NxasXM-2']","subratakbhowmik@hotmail.com")
        self.send_keys("//input[@id='evf-277-field_66FR384cge-3']", "008801818224947")
        self.send_keys("//textarea[@id='evf-277-field_yhGx3FOwr2-4']","Thanks Automation Bro for make me learning new automation tests.")
        self.click("//button[@id='evf-submit-277']")
        self.wait_for_element("//div[@role='alert']")
        self.assert_text('Thanks for contacting us! We will be in touch with you shortly',"//div[contains(text(),'Thanks for contacting us!')]")