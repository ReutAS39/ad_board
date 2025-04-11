## sf_add_board

______
### Стек технологий 


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
______
### Описание проекта

[//]: # (*Новостной портал.*)

[//]: # ()
[//]: # ()
[//]: # (*Реализовано следующее:*)

[//]: # (+ ***Создание, редактирование и удаление объектов;***)

[//]: # (+ ***Фильтры и пагинация;***)

[//]: # (+ ***Регистрация и авторизация пользователей с помощью пакета allauth;***)

[//]: # (+ ***Возможность подписаться на интересующую категорию новостей. При создании новости подписчикам этой категории автоматически отправляется сообщение о пополнении в разделе. ;***)

[//]: # (+ ***Рассылка писем еженедельно с новыми статьями, добавленными за неделю в разделе, на который подписан пользователь. &#40;apscheduler &#41;;***)

### Установка 

*1. Клонируйте репозиторий:*

   ```bash
   git clone https://github.com/ReutAS39/ad_board.git
   ```

*2. Перейдите в директорию проекта:*

   ```bash
   cd ad_board
   ```

*3. Создайте и активируйте виртуальное окружение:*

   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Windows: venv\Scripts\activate
   ```

*4. Установите зависимости:*

   ```bash
   pip install -r requirements.txt
   ```

*5. Запустите сервер:*

   ```bash
   python manage.py runserver
   ```