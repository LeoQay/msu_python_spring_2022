# Домашнее задание к лекции #6

## 1. Клиент-серверное приложение для обкачки набора урлов
### Cервер
Написать master-worker cервер (количество воркеров задаётся при запуске) для обработки запросов от клиента.

Алгоритм должен быть следующим:

    - Мастер и воркеры это разные потоки в едином приложении;
    - Мастер слушает порт, на который клиент будет по TCP отправлять урлы для обкачки;
    - Мастер принимает запрос, читает url от клиента и передаёт этот url одному из воркеров;
    - Воркер обкачивает url по https и возвращает клиенту топ K самых частых слов и их количества в формате json;
    - После каждого обработанного урла сервер должен вывести статистику: сколько урлов было обработано на данный момент суммарно всеми воркерами;

`python server.py -w 10 -k 7` (сервер использует 10 воркеров для обкачки и отправляет клиенту топ-7 частых слов)


### Клиент
Утилита, отправляющая по TCP запросы с урлами серверу.
Нужно сделать следующее:

    - Подготовить файл с запросами (порядка 100 разных url);
    - На вход клиенту передаётся два аргумента --- файл с URL'ами и M (количество потоков);
    - Клиент отправляет параллельно M запросов на сервер и печатает ответ сервера в стандартый вывод, то есть, например: `xxx.com: {'word1': 100, 'word2': 50}`.

`python client.py 10 urls.txt`


Все действия должны быть выделены в функции.

### flake8, pylint
### тесты
