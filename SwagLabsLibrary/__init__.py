from SeleniumLibrary import SeleniumLibrary
from robotlibcore import DynamicCore

from SwagLabsLibrary.keywords.BrowserKeywords import BrowserKeywords
from SwagLabsLibrary.keywords.LoginKeywords import LoginKeywords
from SwagLabsLibrary.keywords.MenuKeywords import MenuKeywords
from SwagLabsLibrary.keywords.ProductsKeywords import ProductsKeywords

class SwagLabsLibrary(DynamicCore):
    
    def __init__(self, is_headless: bool = True, env: str = 'prod'):
        self.__selib = SeleniumLibrary(screenshot_root_directory='EMBED')
        components = [
            BrowserKeywords(selib=self.__selib, env=env, is_headless=is_headless),
            LoginKeywords(selib=self.__selib),
            MenuKeywords(selib=self.__selib),
            ProductsKeywords(selib=self.__selib)
        ]
        DynamicCore.__init__(self, library_components=components)