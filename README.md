# Створимо README.md
readme_path = os.path.join(project_root, "README.md")
readme_content = """# Домашнє завдання №3: Прості Flask маршрути

## 🚀 Опис

Цей проект реалізує простий веб-додаток на Flask з обробкою форм, маршрутизацією, шаблонами та збереженням повідомлень у JSON.

## 🔧 Основні можливості:

- Головна сторінка `/`
- Форма для введення повідомлення `/message`
- Перегляд усіх повідомлень `/read`
- Обробка помилки 404 (`error.html`)
- Збереження повідомлень у `storage/data.json` з міткою часу

## 📁 Структура

- `templates/` — HTML-шаблони
- `static/` — CSS та зображення
- `storage/` — збережені повідомлення
- `app.py` — головний файл додатка

## 🧪 Запуск

```bash
pip install -r requirements.txt
python app.py
