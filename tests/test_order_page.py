from pages.order_page import OrderPage
from pages.main_page import MainPage
import pytest
import data
import allure


@allure.suite('Тесты на заказ самоката')
class TestOrderPage:
    @allure.title('Создание заказа')
    @pytest.mark.parametrize(
        'person_info, rent_info',
        [
            (data.CHARACTER_1, data.RENT_INFO_1),
            (data.CHARACTER_2, data.RENT_INFO_2)
        ]
    )
    def test_make_order(self, driver, person_info, rent_info):
        main_page = MainPage(driver)
        main_page.accept_cookie()
        main_page.click_to_order_button_up()

        order_page = OrderPage(driver)
        order_page.wait_person_info_page()
        order_page.fill_person_info_form(person_info)

        rent_info_header = order_page.get_rent_info_header()
        assert rent_info_header.text == data.RENT_INFO_HEADER

        order_page.fill_rent_info_form(rent_info)
        order_page.click_order_finish_button()
        order_page.confirm_order()

        order_finish_header = order_page.get_order_info_header()
        assert data.ORDER_FINISH_HEADER in order_finish_header.text

    @allure.title('Проверка кнопки "Заказать" внизу страницы')
    def test_open_order_form_button(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookie()
        main_page.click_to_order_button_up()

        order_page = OrderPage(driver)
        header = order_page.get_person_info_header()
        assert header.text == data.PERSON_INFO_HEADER

    @allure.title('Переход на главную страницу кликом по логотипу "Самоката"')
    def test_transfer_by_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookie()
        main_page.go_to_order_page()

        order_page = OrderPage(driver)
        header = order_page.get_person_info_header()
        assert header.text == data.PERSON_INFO_HEADER

        page = OrderPage(driver)
        page.go_to_main_page_by_scooter_logo()

        main_page_header_text = main_page.get_main_header_text()
        assert data.HEADER_SCOOTER in main_page_header_text