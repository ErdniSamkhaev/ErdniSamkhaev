from datetime import datetime

now = datetime.now()
hour = now.hour

if hour < 12:
    greeting = "Доброе утро!"
elif hour < 18:
    greeting = "Добрый день!"
else:
    greeting = "Добрый вечер!"

with open("README.md", "r") as file:
    content = file.readlines()

for i in range(len(content)):
    if content[i].startswith("<p align=\"center\">"):
        content[i] = f"<p align=\"center\">\n  <b>{greeting}</b>\n</p>\n"

with open("README.md", "w") as file:
    file.writelines(content)
