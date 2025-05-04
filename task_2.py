import os
import requests
from bs4 import BeautifulSoup

# Настройки
base_url = 'https://lenta.ru/'
keyword = 'Трамп'
output_folder = r'C:\Users\PC\parsing_website_lenta\Text-html'
output_file = os.path.join(output_folder, f'{keyword.lower()}_mentions.html')

# Создаем папку, если ее нет
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

try:
    # Получаем HTML-код страницы
    response = requests.get(base_url)
    response.raise_for_status()  # Проверяем успешность запроса
    
    # Парсим HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    news_blocks = soup.find_all('div', class_='card-mini__text') 
    
    # Собираем упоминания ключевого слова
    mentions = []
    for block in news_blocks:
        text = block.get_text()
        if keyword.lower() in text.lower():
            mentions.append(text.strip())
    
    # Формируем HTML-документ
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Упоминания {keyword}</title>
        <meta charset="utf-8">
        <style>
            table {{ width: 100%; border-collapse: collapse; }}
            th, td {{ padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }}
            tr:hover {{ background-color: #f5f5f5; }}
        </style>
    </head>
    <body>
        <h1>Упоминания "{keyword}" на LENTA.RU</h1>
        <table>
            <tr><th>№</th><th>Текст новости</th></tr>
    """
    
    for i, mention in enumerate(mentions, 1):
        html_content += f'<tr><td>{i}</td><td>{mention}</td></tr>'
    
    html_content += """
        </table>
    </body>
    </html>
    """
    
    # Сохраняем в файл
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Результаты сохранены в {output_file}")

except Exception as e:
    print(f"Произошла ошибка: {e}")