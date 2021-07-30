from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    #index : polls/
    path('', views.IndexView.as_index, name='index'),
    #detail pg : polls/1/
    path('<int:pk>/', views.DetailView.as_detail, name='detail'),
    #results pg : polls/1/results
    path('<int:pk>/results/', views.ResultsView.as_results, name='results'),
    #vote pg : polls/1/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
