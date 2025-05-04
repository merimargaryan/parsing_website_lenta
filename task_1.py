import os
import urllib.request

# Список URL изображений для загрузки
image_urls = [
    'https://vproekte.com/wp-content/uploads/2021/11/liv-1_Post-Copy.jpg',
    'https://stdkhv.ru/upload/iblock/43f/onxq6ahu4wfm0loyfido6edo54tb08nu.png',
    'https://evdom.ru/wp-content/uploads/2019/05/83c35b7c-2305-46c6-a92b-353fd47b373d-1000x667.jpeg',
    'https://99px.ru/sstorage/86/2018/02/image_862502181033486990906.gif'
]

# Папка для сохранения
download_folder = r'C:\Users\PC\parsing_website_lenta\Pictures'

# Создаем папку, если ее нет
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Функция для загрузки изображений
def download_images(urls, folder):
    for url in urls:
        try:
            # Извлекаем имя файла из URL
            filename = os.path.basename(url)
            # Полный путь для сохранения
            save_path = os.path.join(folder, filename)
            
            # Загружаем изображение
            urllib.request.urlretrieve(url, save_path)
            print(f"Изображение {filename} успешно загружено в {save_path}")
        except Exception as e:
            print(f"Ошибка при загрузке {url}: {e}")

# Вызываем функцию загрузки
download_images(image_urls, download_folder)