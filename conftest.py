import pytest
from selenium import webdriver
import data


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(data.URL)
    yield driver
    driver.quit()
