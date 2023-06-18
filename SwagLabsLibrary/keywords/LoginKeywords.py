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
        
    @keyword(tags=("LoginKeywords",))
    def wait_until_login_page_is_visible(self, timeout: Any = None):
        """Wait until login page is visible.

            Arguments:
            - ``timeout``: Specific maximum time to wait before raising an exception if not visible. Defaults to None.

            Example:
            | Wait Until Login Page Is Visible | timeout=5s |
            | Wait Until Login Page Is Visible |            |
        """
        timeout = timeout if timeout is not None else GLOBAL_SWAGLABS_TIMEOUT
        
        self.__selib.wait_until_element_is_visible(
            locator=_LOGIN_BTN, timeout=timeout, error="Cannot wait for login page to be visible.")

    @keyword(tags=("LoginKeywords",))
    def login_to_swaglabs(self, username: str = None, password: str = None):
        """Login to Swaglabs using the provided ``username`` and ``password``. This will click the login button
           even when no ``username`` and/or ``password`` were provided.

            Arguments:
            - ``username``: Username to use for login.
            - ``password``: Password to use for login.
            
            Example:
            | Login To SwagLabs | username=standard_user | password=secret_sauce |
        """
        self.wait_until_login_page_is_visible()

        if username is not None:
            self.__selib.input_text(locator=_USERNAME_FLD, text=username)
        if password is not None:
            self.__selib.input_password(locator=_PASSWORD_FLD, password=password)
            
        self.__selib.click_element(locator=_LOGIN_BTN)
        
    @keyword(tags=("LoginKeywords", "AssertionKeywords"))
    def login_error_msg_should_be(self, err_msg: str):
        """Validates that the displayed error message in the login page match ``err_msg``.

            Arguments:
            - ``err_msg``: The exepcted error message.
            
            Example:
            | Login Error Msg Should Be | err_msg=Username is required. |
        """
        self.__selib.element_text_should_be(locator=_ERROR_DISPLAY, expected=err_msg)
        