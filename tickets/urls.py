from django.urls import path


from . import views



urlpatterns = [
    path("ticket/", views.TicketListView.as_view()),
    path("ticket/<int:pk>/", views.TicketDetailView.as_view()),
    path("answer/", views.AnswerListView.as_view()),
    path("answer/<int:pk>/", views.AnswerDetailView.as_view()),
    path("ticketCreate/", views.TicketCreateView.as_view()),
    path("answerCreate/", views.AnswerCreateView.as_view()),
    path("ticketUpdate/<int:pk>/", views.TicketUpdateView.as_view()),

]