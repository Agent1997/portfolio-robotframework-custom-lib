from typing import Any
from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword

from SwagLabsLibrary.timeouts import GLOBAL_SWAGLABS_TIMEOUT

_USERNAME_FLD: str = 'id:user-name'
_PASSWORD_FLD: str = 'id:password'
_LOGIN_BTN: str = 'id:login-button'
_ERROR_DISPLAY: str = 'xpath://h3[@data-test="error"]'


class LoginKeywords:

    def __init__(self, selib: SeleniumLibrary):
        self.__selib = selib
        
    @keyword(tags="LoginKeywords",)
    def wait_until_login_page_is_visible(self, timeout: Any = None):
        timeout = timeout if timeout is not None else GLOBAL_SWAGLABS_TIMEOUT
        
        self.__selib.wait_until_element_is_visible(
            locator=_LOGIN_BTN, timeout=timeout, error="Cannot wait for login page to be visible.")

    @keyword(tags="LoginKeywords",)
    def login_to_swaglabs(self, username: str = None, password: str = None):
        self.wait_until_login_page_is_visible()

        if username is not None:
            self.__selib.input_text(locator=_USERNAME_FLD, text=username)
        if password is not None:
            self.__selib.input_password(locator=_PASSWORD_FLD, password=password)
            
        self.__selib.click_element(locator=_LOGIN_BTN)
        
    @keyword(tags=("LoginKeywords", "AssertionKeywords"))
    def login_error_msg_shoul_be(self, err_msg: str):
        self.__selib.element_text_should_be(locator=_ERROR_DISPLAY, expected=err_msg)
        