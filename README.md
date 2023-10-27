# Дипломный проект курса "Инженер по тестированию плюс" Яндекс Практикум

Скрипты SQL запросов:



# Задание 1. 

SELECT c.login, COUNT(*) FROM "Couriers" AS c INNER JOIN "Orders" AS o ON c.id = o."courierId" WHERE o."inDelivery" = true GROUP BY c.login;

см. скриншот - script 1.

Также запрос приведен в файле  SQL_requests
# Задание 2.

SELECT track, CASE WHEN finished=true THEN 2 WHEN cancelled=true THEN -1 WHEN "inDelivery"=true THEN 1 ELSE 0 END FROM "Orders";

см. скриншот - script 2.

Также запрос приведен в файле  SQL_requests
#  Автоматизация теста к API

Для запуска автотеста, необходимо выгрузить репозиторий, открыть проект можно в  PyCharm  
Зпустить автотест можно в файле get_track_order_info.py

Условия:
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполянется командой pytest