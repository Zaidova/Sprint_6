from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure

import locators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ищем элемент {locator}')
    def find_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Кликаем на элемент {locator}')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Принимаем куки')
    def accept_cookie(self):
        self.click_to_element(locators.main_page_locators.COOKIES_BUTTON)

    @allure.step('Скроллим страницу')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Заполняем текстом элемент {locator}')
    def add_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step('Получаем текст элемента')
    def get_text(self, locator):
        return self.find_element(locator).text

    @staticmethod
    def format_locator(locator, value):
        return locator[0], locator[1].format(value)

    @allure.step('Переключаемся на другую вкладку')
    def change_tab(self, tab_number):
        self.driver.switch_to.window(self.driver.window_handles[tab_number])


