import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class NewVisitorTest(unittest.TestCase):
    """Тест нового посетителя"""

    def setUp(self) -> None:
        """Установка"""
        google_driver_path = "/home/galkin/projects/tests_book/driver/chromedriver"
        service = Service(executable_path=google_driver_path)
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.browser = webdriver.Chrome(
            options=options,
            service=service,
        )

    def tearDown(self) -> None:
        """Демонтаж"""
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """Тест: можно начать список и получить его позже"""
        # Эдит слышала про крутое новое онлайн-приложение со
        # списком неотложных дел. Она решает оценить его
        # домашнюю страницу
        self.browser.get('http://localhost:8000')

        # Она видит, что заголовок и шапка страницы говорят о
        # списках неотложных дел
        self.assertIn('To-Do', self.browser.title)
        self.fail('Закончить тест!')

        # Ей сразу же предлагается ввести элемент списка


if __name__ == '__main__':
    unittest.main(warnings='ignore')
