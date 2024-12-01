from selenium.webdriver.common.by import By

COOKIES_BUTTON = (By.ID, "rcc-confirm-button")
IMPORTANT_QUESTIONS_TEXT = (By.XPATH, ".//div[text() = 'Вопросы о важном']")
QUESTION = (By.ID, "accordion__heading-{}")
ANSWER = (By.XPATH, "//div[@id='accordion__panel-{}']/p")
ORDER_BUTTON_UP = (By.XPATH, '//div[contains(@class, "Header_Nav")]/button[text()="Заказать"]')
ORDER_BUTTON_DOWN = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button[text()="Заказать"]')
HOME_PAGE_HEADER = (By.XPATH, '//div[contains(@class, "Home_Header")]')
YANDEX_LOGO = (By.XPATH, '//a[contains(@class, "Header_LogoYandex")]')
DZEN_NEWS_TITLE = (By.XPATH, '//div[@data-testid="floor-title-text" and text()="Новости"]')