import time
import csv
import pandas as pd
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_prices_from_url():
    driver = webdriver.Chrome()

    # URL для парсинга
    url = "https://www.divan.ru/category/divany-i-kresla"

    # Открываем страницу
    driver.get(url)
    time.sleep(3)  # Ждем загрузки страницы

    # Парсим данные
    sofas = driver.find_elements(By.CLASS_NAME, 'wYUX2')
    data = []

    for sofa in sofas:
        try:
            price_text = sofa.find_element(By.CSS_SELECTOR, 'meta[itemprop="price"]').get_attribute('content')
            price = int(price_text.replace(' ', '').replace('₽', ''))
            data.append([price])
        except:
            continue

    # Сохраняем данные в CSV файл
    with open('sofas.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Price'])
        writer.writerows(data)

    # Закрываем браузер
    driver.quit()


def calculate_average_price():

    # Находим среднюю цену
    average_price = df['Price'].mean()
    print(f"Средняя цена на диваны: {average_price:.2f} руб.")


def build_a_graph():
    plt.figure(figsize=(10, 6))
    plt.hist(df['Price'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Гистограмма цен на диваны')
    plt.xlabel('Цена (руб)')
    plt.ylabel('Количество диванов')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    # Создаем файл с ценами
    get_prices_from_url()

    df = pd.read_csv('sofas.csv')
    # Обработка данных
    calculate_average_price()
    # Создаем гистограмму
    build_a_graph()