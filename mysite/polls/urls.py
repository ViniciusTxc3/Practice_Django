from django.urls import path

from . import views

# Precisa apontar a raiz da URLconf para o módulo polls.urls (mysitte/urls.py)
urlpatterns = [
    path('', views.index, name='index'), #/polls/
    path('<int:question_id>/', views.detail, name='detail'), #/polls/5
    path('<int:question_id>/results/', views.results, name='results'), #/polls/5/result  
    path('<int:question_id>/vote/', views.vote, name='vote'), #/polls/5/results/vote
]    
