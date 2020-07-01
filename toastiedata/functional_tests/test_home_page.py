

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class TestHomePage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.close()

    def test_title_is_toastiedata(self):
        self.browser.get(self.live_server_url)

        # The user opens the home page
        brand = self.browser.find_element_by_class_name('navbar-brand')
        self.assertEquals(
            brand.text,
            'toastiedata'
        )
