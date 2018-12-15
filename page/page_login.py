import page
from base.base import Base


class PageLogin(Base):
    def page_click_login(self,):
        self.base_click(page.login_click)

    def page_input_username(self, username):
        self.base_input(page.loc_username, username)

    def page_input_password(self, password):
        self.base_input(page.loc_password, password)

    def page_input_verify_code(self, verify_code):
        self.base_input(page.loc_verify_code, verify_code)

    def page_click_login_submit(self):
        self.base_click(page.submit_login_click)