Cлужба саппорта 
1) Пользователь пишет тикет и отправляет - path("ticketCreate/", views.TicketCreateView.as_view())
2) Саппорт видит решенные, нерешенные и замороженные тикеты (все по факту), может отвечать на них, изменять статусы тикетов - 
    -path("ticket/", views.TicketListView.as_view(), name="ticketList") - посмотреть нерешенные тикеты
    - path("doneTicket/", views.DoneTicketListView.as_view()) - посмотреть решенные тикеты
    - path("allTicket/", views.AllTicketListView.as_view()) - посмотреть все тикеты
    - path("ticket/<int:pk>/", views.TicketDetailView.as_view()) - посмотреть конкретный тикет
    - path("answerCreate/", views.AnswerCreateView.as_view()) - создать ответ на тикет
    - path("ticketUpdate/<int:pk>/", views.TicketUpdateView.as_view()) - присвоить ответ тикету + изменить статус
3)Пользователь может просмотреть ответ саппорта, и добавить новое сообщение( саппорт ответить на него) - path("answer/<int:pk>/", views.AnswerDetailView.as_view(), name="answerDetail"),

Технологии:
Django + Django Rest Framework, JWT авторизация, PostgreSQL, Docker (Docker-compose), PyTestsб Celery и Redis, ckEditor, yasg-документирование, corsheaders

Для код стайла: 
flake8, isort



Запуск проекта:
docker-compose up
docker exec -t -i "ID контейнера" bash
python manage.py migrate
port - 127.0.0.1:8000


Запуск Celery: 
celery -A support beat
celery -A support worker -l INFO
