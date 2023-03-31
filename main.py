# coding: utf-8

import os
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def get_html__list_of_link_to_cars(url):
    service = Service(executable_path=os.path.join(os.getcwd(), 'chromedriver', 'chromedriver.exe'))
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    try:
        driver.get(url=url)
        time.sleep(4)

        driver.find_element(By.CLASS_NAME, 'CheckboxCaptcha-Button').click()
        time.sleep(2)

        # links = driver.find_element(By.CLASS_NAME, 'Link ListingItemTitle__link')

        car = 'tesla'
        i = 0
        while True:
            i += 1
            with open(car + '_' + str(i) + '.html', 'w', encoding='utf-8') as f:
                f.write(driver.page_source)

            next_button = driver.find_element(By.CLASS_NAME, 'ListingPagination__next')
            if not next_button.get_attribute('href'):
                break
            next_button.click()
            time.sleep(2)

    except Exception as e:
        print(e)
    finally:
        time.sleep(999999)
        driver.close()
        driver.quit()


def get_links_from_html():
    all_links = []
    for i in range(1, 13):
        with open('tesla_' + str(i) + '.html', encoding='utf-8') as f:
            src = f.read()

        soup = BeautifulSoup(src, 'lxml')
        links = soup.find_all('a', class_='Link ListingItemTitle__link')
        href_links = [link.get('href') for link in links]
        all_links.extend(href_links)

    return all_links

def get_data_from_link_with_characteristics(url):
    service = Service(executable_path=os.path.join(os.getcwd(), 'chromedriver', 'chromedriver.exe'))
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    try:
        driver.get(url=url)
        time.sleep(3)

        # нажимаем на капче "я не робот"
        driver.find_element(By.CLASS_NAME, 'CheckboxCaptcha-Button').click()
        time.sleep(4)

        # нажимаем на кнопку 'Войти'
        driver.find_element(By.CLASS_NAME, 'HeaderUserMenu__loginButton').click()
        time.sleep(3)

        # вводим почту и нажимаем Enter
        ActionChains(driver).send_keys('kuro4kinalexei@gmail.com').key_down(Keys.ENTER).perform()
        # ActionChains(driver).send_keys('kurochkinalexei@yandex.ru').key_down(Keys.ENTER).perform()
        time.sleep(2)

        # вводим проверочный код. Для этого на своей почте его смотрим и вводим в через консоль
        # pass_input = driver.find_element(By.CLASS_NAME, 'AuthFormCodeInput__input')
        pass_from_email = input('Введи пароль из письма: ').strip()
        # pass_input.clear()
        # pass_input.send_keys(x)
        ActionChains(driver).send_keys(pass_from_email).key_down(Keys.ENTER).perform()
        time.sleep(8)



        # нажимаем на кнопку "показать телефон"
        driver.find_element(By.CLASS_NAME, 'OfferPhone_button').click()
        time.sleep(4)


        time.sleep(99)


    except Exception as e:
        print(e)
    finally:
        driver.close()
        driver.quit()

def entry_in_auto_ru():
    pass

if __name__ == '__main__':
    # url = 'https://auto.ru/rossiya/cars/tesla/all/?output_type=table'
    # get_html__list_of_link_to_cars(url)
    # all_link = get_links_from_html()
    get_data_from_link_with_characteristics('https://auto.ru/cars/used/sale/volkswagen/tiguan/1116854013-c1de166a/')
