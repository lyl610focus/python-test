import pytest
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class Test_appium:

    def setup_class(self):
        # 启动参数
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "5.1"
        desired_caps["deviceName"] = "192.168.51.101:5555"
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings'
        # 解决中文问题
        desired_caps["unicodeKeyboard"] = True
        desired_caps["resetKeyboard"] = True
        # 建立驱动
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    def teardown_class(self):
        self.driver.quit()

    # 显式等待
    def wait_element(self, type, data):
        if type == 'id':
            return WebDriverWait(self.driver, 5, 1).until(lambda x : x.find_element_by_id(data))

        if type == 'xpath':
            return WebDriverWait(self.driver, 5, 1).until(lambda x : x.find_element_by_xpath(data))

    @pytest.fixture()
    def init_index(self):
        gengduo = self.wait_element('xpath', "//*[contains(@text, '更多')]")
        dianchi = self.wait_element('xpath', "//*[contains(@text, '电池')]")
        self.driver.drag_and_drop(dianchi, gengduo)
        self.wait_element('xpath', "//*[contains(@text, '位置信息')]").click()

    @pytest.mark.usefixtures("init_index")
    def test_change_mod(self):
        mod = self.wait_element('id', "android:id/summary")
        mod.click()
        self.wait_element('xpath', "//*[contains(@text, '耗电量低')]").click()
        self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        assert "耗电量低" in mod.text





