from pages.main_page import MainPage
import pytest
import data
import allure

@allure.suite('Тесты на главной странице')
class TestMainPage:

    @allure.title('Соответствие текста ответа вопросу')
    @pytest.mark.parametrize(
        'num, text',
        [
            (0, data.ANSWER_1),
            (1, data.ANSWER_2),
            (2, data.ANSWER_3),
            (3, data.ANSWER_4),
            (4, data.ANSWER_5),
            (5, data.ANSWER_6),
            (6, data.ANSWER_7),
            (7, data.ANSWER_8)
        ]
    )
    def test_answers_questions_compliance(self, driver, num, text):
        main_page = MainPage(driver)
        main_page.accept_cookie()
        assert main_page.get_answer_text(num) == text

    @allure.title('Переход на страницу "Дзен" при нажатии на логотип "Яндекс"')
    def test_transfer_to_dzen(self, driver):
        page = MainPage(driver)
        page.accept_cookie()
        page.go_to_dzen_by_yandex_logo()

        dzen_news_title = page.get_dzen_news_title()
        assert dzen_news_title == data.DZEN_NEWS_TITLE