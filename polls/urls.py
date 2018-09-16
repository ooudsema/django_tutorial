from django.urls import path

from . import views

app_name = 'polls'
#urlpatterns = [
#    path('', views.index, name='index'),
#    path('owner', views.owner, name='owner'),
#    path('<int:question_id>/', views.detail, name='detail'),
#    path('<int:question_id>/results/', views.results, name='results'),
#    path('<int:question_id>/vote/', views.vote, name='vote'),
#]


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('owner', views.owner, name='owner'),
]

#urlpatterns = [
#    path('', views.IndexView.as_view(), name='index'),
#    path('/', views.DetailView.as_view(), name='detail'),
#    path('/results/', views.ResultsView.as_view(), name='results'),
#    path('owner', views.owner, name='owner'),
#    path('/vote/', views.vote, name='vote'),
#]