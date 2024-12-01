from pages.base_page import BasePage
import locators.main_page_locators as locators
import allure

class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Получаем текст ответа по номеру вопроса')
    def get_answer_text(self, num):
        locator_question = self.format_locator(locators.QUESTION, num)
        locator_answer = self.format_locator(locators.ANSWER, num)
        self.scroll_to_element(locator_question)
        self.click_to_element(locator_question)
        return self.get_text(locator_answer)

    @allure.step('Нажимаем на кнопку "Заказать" вверху страницы')
    def click_to_order_button_up(self):
        self.click_to_element(locators.ORDER_BUTTON_UP)

    @allure.step('Нажимаем на кнопку "Заказать"  внизу страницы')
    def click_to_order_button_down(self):
        self.scroll_to_element(locators.ORDER_BUTTON_DOWN)
        self.click_to_element(locators.ORDER_BUTTON_DOWN)

    @allure.step('Переходим на страницу "Дзен" кликом по лого Яндекса')
    def go_to_dzen_by_yandex_logo(self):
        self.click_to_element(locators.YANDEX_LOGO)
        self.change_tab(-1)

    @allure.step('Проверяем загрузку страницы "Дзен"')
    def get_dzen_news_title(self):
        return self.find_element(locators.DZEN_NEWS_TITLE).text

    @allure.step('Переходим к форме заказа')
    def go_to_order_page(self):
        self.click_to_element(locators.ORDER_BUTTON_UP)

    @allure.step('Получаем текст заголовка на главной странице')
    def get_main_header_text(self):
        return self.find_element(locators.HOME_PAGE_HEADER).text

