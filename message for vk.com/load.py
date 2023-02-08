import requests #импортируем модуль
f=open(r'file_bdseo.xls',"wb") #открываем файл для записи, в режиме wb
ufr = requests.get("https://docs.google.com/spreadsheets/d/1sbQcIVUD8S1IQ5jg0nz61999Ydqb85hPcszkmJ-91K8/export?format=xlsx&id=1sbQcIVUD8S1IQ5jg0nz61999Ydqb85hPcszkmJ-91K8") #делаем запрос
f.write(ufr.content) #записываем содержимое в файл; как видите - content запроса
f.close()