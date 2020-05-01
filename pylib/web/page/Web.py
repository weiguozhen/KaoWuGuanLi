from robot.api import logger
from selenium import webdriver
from pylib.web.util.handel_ini import HandelIni
from pylib.web.page.LoginPage import LoginPage

handel_ini = HandelIni()


class Web:
    # driver: webdriver = None
    # ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def start(self):
        browser_name = handel_ini.get_value('browser', 'name')
        wait = handel_ini.get_value('wait', 'wait_time')

        self.driver = self._get_local_web_driver(browser_name)
        self.driver.implicitly_wait(wait)
        return LoginPage(self.driver)

    def _get_local_web_driver(self, browser_name: str):
        """
        :param browser_name: 浏览器类型
        :return: 浏览器实例
        """
        if browser_name.upper() == "CHROME":
            driver = webdriver.Chrome()
        elif browser_name.upper() == "FIREFOX":
            driver = webdriver.Firefox()
        elif browser_name.upper() == "IE":
            driver = webdriver.Ie()
        else:
            logger.error(f"浏览器类型错误：{browser_name}")
            raise ValueError(f"浏览器类型错误：{browser_name}")
        return driver

    def quit(self):
        self.driver.quit()
