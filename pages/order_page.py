from pages.base_page import BasePage
import locators.order_page_locators as locators
import allure

class OrderPage(BasePage):

    @allure.step('Ждем загрузки страницы "Для кого самокат"')
    def wait_person_info_page(self):
        self.find_element(locators.PERSON_INFO_FORM)

    @allure.step('Выбираем станцию метро')
    def select_metro_station(self, station_name):
        self.click_to_element(locators.PersonForm.METRO_STATION)
        self.find_element(locators.PersonForm.METRO_STATION_LIST)
        station_button_locator = (
            locators.PersonForm.METRO_STATION_BUTTON[0],
            locators.PersonForm.METRO_STATION_BUTTON[1].format(station_name)
        )
        self.click_to_element(station_button_locator)

    @allure.step('Выбираем срок аренды')
    def select_order_period(self, rent_period):
        self.click_to_element(locators.RentForm.PERIOD)
        item_locator = self.format_locator(locators.RentForm.PERIOD_ITEM, rent_period)
        self.click_to_element(item_locator)

    @allure.step('Заполняем форму "Для кого самокат"')
    def fill_person_info_form(self, person_info):
        self.add_text(locators.PersonForm.FIRST_NAME, person_info['first_name'])
        self.add_text(locators.PersonForm.SECOND_NAME, person_info['last_name'])
        self.add_text(locators.PersonForm.ADDRESS, person_info['address'])
        self.add_text(locators.PersonForm.PHONE, person_info['phone_number'])
        self.select_metro_station(person_info['metro_station'])
        self.click_to_element(locators.PersonForm.NEXT_BUTTON)

    @allure.step('Заполняем форму "Про аренду"')
    def fill_rent_info_form(self, rent_info):
        self.add_text(locators.RentForm.START_DATE, rent_info['start_date'])
        self.select_order_period(rent_info['rent_period'])
        self.add_text(locators.RentForm.COMMENTS, rent_info['comment'])
        if rent_info['color'] == 'black':
            self.click_to_element(locators.RentForm.BLACK_COLOR_OF_SCOOTER)
        else:
            self.click_to_element(locators.RentForm.GREY_COLOR_OF_SCOOTER)

    @allure.step('Получаем заголовок формы "Про аренду"')
    def get_rent_info_header(self):
        return self.find_element(locators.RENT_INFO_HEADER)

    @allure.step('Кликаем на кнопку "Заказать" формы "Про аренду"')
    def click_order_finish_button(self):
        self.click_to_element(locators.RentForm.ORDER_BUTTON)

    @allure.step('Кликаем на кнопку "Да" в диалоге подтверждения заказа')
    def confirm_order(self):
        self.click_to_element(locators.CONFIRMATION_BUTTON)

    @allure.step('Получаем заголовок диалога информации о заказе')
    def get_order_info_header(self):
        return self.find_element(locators.ORDER_FINISH_HEADER)

    @allure.step('Получаем заголовок формы "Для кого самокат"')
    def get_person_info_header(self):
        return self.find_element(locators.PERSON_INFO_HEADER)

    @allure.step('Переходим на главную страницу, кликая на логотип "Самоката"')
    def go_to_main_page_by_scooter_logo(self):
        self.click_to_element(locators.SCOOTER_LOGO)