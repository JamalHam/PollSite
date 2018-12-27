from django.urls import path

from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('Choice', views.ChoiceView)

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    #path('', include(router.urls)),
    path('', views.ChoiceView.as_view(router.urls)),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('create/', views.CreatePollView.as_view(), name='create')
]