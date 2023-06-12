from datetime import timedelta
from SeleniumLibrary import SeleniumLibrary


def is_element_visible(selib: SeleniumLibrary, locator: str, timeout: timedelta):
    try:
        selib.wait_until_element_is_visible(locator=locator, timeout=timeout)
        return True
    except Exception:
        return False