from datetime import timedelta
from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword
from robot.api import logger

from SwagLabsLibrary.helpers.SeleniumLibraryHelper import is_element_visible
from SwagLabsLibrary.timeouts import GLOBAL_SWAGLABS_TIMEOUT

_BURGER_BTN: str = 'id:react-burger-menu-btn'
_CLOSE_BTN: str = 'id:react-burger-cross-btn'
_MENU_ITEMS_LABLE: str = "xpath://nav[@class='bm-item-list']/a"
_LOGOUT: str = 'id:logout_sidebar_link'

class MenuKeywords:
    
    def __init__(self, selib: SeleniumLibrary):
        self.__selib = selib
        
    @keyword
    def logout_from_swaglabs(self):
        """Logout from swaglabs.
            
            Example:
            | Logout from swaglabs |
        """
        self.__open_menu()
        self.__selib.click_element(locator=_LOGOUT)
        
    @keyword
    def menu_items_should_have(self, *args):
        """Validates that ``args`` are displayed in the menu.

            Arguments:
            - ``args``: The expected items that should be displayed in the menu.
            
            Example:
            | Menu Items Should Have | About Logout Reset${SPACE}App${SPACE}State |
        """
        self.__open_menu()
        act_texts = [i.text for i in self.__selib.find_elements(locator=_MENU_ITEMS_LABLE)]
        if not all(text in act_texts for text in list(args)):
            raise AssertionError("")
        
    def __open_menu(self):
        if is_element_visible(selib=self.__selib, locator=_BURGER_BTN, timeout=timedelta(seconds=0.5)):
            self.__selib.click_element(locator=_BURGER_BTN)
            self.__selib.wait_until_element_is_visible(locator=_CLOSE_BTN, timeout=GLOBAL_SWAGLABS_TIMEOUT)
        