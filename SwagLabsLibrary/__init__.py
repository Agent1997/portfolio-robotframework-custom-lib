from SeleniumLibrary import SeleniumLibrary
from robotlibcore import DynamicCore
from robot.api.deco import library

from SwagLabsLibrary.keywords.BrowserKeywords import BrowserKeywords
from SwagLabsLibrary.keywords.LoginKeywords import LoginKeywords
from SwagLabsLibrary.keywords.MenuKeywords import MenuKeywords
from SwagLabsLibrary.keywords.ProductsKeywords import ProductsKeywords

@library(scope='GLOBAL')
class SwagLabsLibrary(DynamicCore):
    """SwagLabsLibrary is a demo library that provides keywords to automateinteraction with the Swag Labs demo application (https://www.saucedemo.com/v1/index.html).
    This library demonstrate the basic usage of `PythonLibCore` (https://github.com/robotframework/PythonLibCore) for creating custom Robot Framework library that suites your application.
    To learn more about robot framework, visit the following websites:
    - https://robotframework.org/ 
    - https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html
    NOTE: This is for demo purposes only! The construction of the keywords and the codes may be different in real projects and may be a little more complicated.
    """
    
    def __init__(self, is_headless: bool = True, env: str = 'prod'):
        """Configuration whether to open browser in headless mode and on which environment to execute can be passed when importing the library.

            Arguments:
            - ``is_headless``: Whether to run the browser in headless mode. Defaults to ``True``.
            - ``env``: Will be used to identify which url will be used when opening the application in the browser.
            
            Example:
            | Library | SwagLabsLibrary | is_headless=${False} |
        """
        self.__selib = SeleniumLibrary(screenshot_root_directory='EMBED')
        components = [
            BrowserKeywords(selib=self.__selib, env=env, is_headless=is_headless),
            LoginKeywords(selib=self.__selib),
            MenuKeywords(selib=self.__selib),
            ProductsKeywords(selib=self.__selib)
        ]
        DynamicCore.__init__(self, library_components=components)