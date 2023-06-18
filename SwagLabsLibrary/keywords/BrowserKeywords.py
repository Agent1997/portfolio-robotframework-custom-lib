from SeleniumLibrary import SeleniumLibrary
from selenium.webdriver.chrome.options import Options
from robot.api import logger
from robot.api.deco import keyword

_urls: dict = {
    "prod": "https://www.saucedemo.com/"
}

def _chrome_options(is_headless: bool):
    options: Options = Options()

    if is_headless:
        logger.info(msg="Setting browser to run in headless mode.")
        options.add_argument("--headless")
    else:
        logger.info(msg="Setting browser to run in UI mode.")

    options.add_argument("--no-sandbox")
    options.add_argument("--test-type")
    options.add_argument("use-fake-device-for-media-stream")
    options.add_argument("use-fake-ui-for-media-stream")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--incognito")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-default-apps")
    options.add_argument("--disable-extensions-file-access-check")
    options.add_argument("--disable-infobars")
    options.add_argument("--window-size=1920,1080")
    return options

class BrowserKeywords:
    
    def __init__(self, selib: SeleniumLibrary, env: str, is_headless: bool):
        self.__env = env
        self.__selib = selib
        self.__is_headless = is_headless
     
    @keyword(tags=("BrowserKeywords",))   
    def open_swaglabs_in_browser(self, is_headless: bool = None, browser: str = 'chrome'):
        """Opens the Swaglabs website in a browser.

            Arguments:
            - ``is_headless``: Whether to run the browser in headless mode. If None, will follow the configuration set when `Importing` the library.
            - ``browser``: The browser to use. Defaults to 'chrome'.

            Example:
            | Open Swaglabs in Browser | is_headless=${True} | browser=firefox |
        """
        is_headless = is_headless if is_headless is not None else self.__is_headless
        
        url = _urls.get(self.__env)
        
        if url is None:
            raise Exception(f"No url configured for {self.__env} environment.")
        
        if browser == 'chrome':
            options = _chrome_options(is_headless=is_headless)
        else:
            raise Exception(f"{browser} is not supported.")
        
        self.__selib.open_browser(browser=browser, options=options, url=url)
        
    @keyword
    def close_all_swaglabs_browser(self):
        """Close all swaglabs browser opened by this instance of the library.

            Example:
            | Close All Swaglabs Browser |
        """
        self.__selib.close_all_browsers()