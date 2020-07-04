import os
import unittest
from time import sleep
from appium import webdriver


def PATH(p):
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )


class TestCaseOne(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platfomVersion'] = '8.1.0'
        desired_caps['deviceName'] = 'orzel'
        desired_caps['app'] = PATH('ApiDemos-debug.apk')
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'

        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_notifications(self):
        self.driver.open_notifications()
        sleep(5)
        elements = self.driver.find_elements_by_class_name(
            'android.widget.TextView')
        flag = False
        for el in elements:
            if el.text == 'Appium Settings':
                flag = True
        self.assertTrue(flag)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCaseOne)
    unittest.TextTestRunner(verbosity=2).run(suite)
