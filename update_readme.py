from datetime import datetime

# Получаем текущее время
now = datetime.now()
hour = now.hour

# Определяем приветствие
if hour < 12:
    greeting = "Доброе утро!"
elif hour < 18:
    greeting = "Добрый день!"
else:
    greeting = "Добрый вечер!"

# Открываем README.md
with open("README.md", "r") as file:
    content = file.readlines()

# Обновляем строку с приветствием
for i in range(len(content)):
    if "<p align=\"center\">" in content[i] and "<b>" in content[i]:
        content[i] = f'<p align="center">\n  <b>{greeting}</b>\n</p>\n'

# Сохраняем изменения в README.md
with open("README.md", "w") as file:
    file.writelines(content)
