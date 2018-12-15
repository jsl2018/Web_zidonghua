import pytest
import time

from page.page_login import PageLogin
from base.get_driver import get_driver


class TestLogin():
    def setup_class(self):
        self.login = PageLogin(get_driver())

    def teardown_class(self):
        time.sleep(5)
        self.login.driver.quit()

    @pytest.mark.parametrize("username, password,verify_code", [(15573235704, 123456, 8888)])
    def test_login(self, username, password,verify_code):
        self.login.page_click_login()
        self.login.page_input_username(username)
        self.login.page_input_password(password)
        self.login.page_input_verify_code(verify_code)
        self.login.page_click_login_submit()
