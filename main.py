import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from math import ceil

service = Service(executable_path=os.path.join(os.getcwd(), 'chromedriver', 'chromedriver.exe'))
driver = webdriver.Chrome(service=service)


def get_html__list_of_link_to_cars(url, nbr_of_cars):
    try:
        driver.get(url=url)
        time.sleep(5)

        driver.find_element(By.CLASS_NAME, 'CheckboxCaptcha-Button').click()
        time.sleep(6)

        with open('.html', 'w', encoding='utf-8') as f:
            f.write(driver.page_source)

        < a        class ="Button Button_color_white Button_size_s Button_type_link Button_width_default ListingPagination__next" role="link" href="https://auto.ru/rossiya/cars/tesla/all/?with_discount=false&amp;page=2" > < span class ="Button__content" > < span class ="Button__text" > —ледующа€, Ctrl ? < / span > < / span > < / a >
        < a        class ="Button Button_color_white Button_disabled Button_size_s Button_type_link Button_width_default ListingPagination__next" role="link" > < span class ="Button__content" > < span class ="Button__text" > —ледующа€, Ctrl ? < / span > < / span > < / a >
        for i in range(1, ceil(nbr_of_cars/37) + 1):
        # # print(driver.title)
        # x = driver.find_element(By.CLASS_NAME, 'ListingCars__loaderOverlay')
        # with open('cars3.html', 'w', encoding='utf-8') as f:
        #     f.write(driver.page_source)

    except Exception as e:
        print(e)
    finally:
        driver.close()
        driver.quit()

if __name__ == '__main__':
    url = 'https://auto.ru/rossiya/cars/tesla/all/?output_type=table'
    get_html__list_of_link_to_cars(url, 437)

    # количество объ€влений на странице - 37
    # tesla - 437 / 37 = 11.8

