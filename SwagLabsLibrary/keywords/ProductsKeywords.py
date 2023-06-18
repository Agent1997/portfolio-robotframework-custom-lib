from typing import Any

from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword

from SwagLabsLibrary.timeouts import GLOBAL_SWAGLABS_TIMEOUT

_PAGE_TITLE: str = "xpath://span[@class='title' and text()='Products']"


class ProductsKeywords:

    def __init__(self, selib: SeleniumLibrary):
        self.__selib = selib

    @keyword(tags=("ProductsKeywords",))
    def wait_until_products_page_is_visible(self, timeout: Any = None):
        timeout = timeout if timeout is not None else GLOBAL_SWAGLABS_TIMEOUT
        self.__selib.wait_until_element_is_visible(
            locator=_PAGE_TITLE, timeout=timeout, error="Cannot wait for the products page to be visible.")
