from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('answers/', views.AnswerListView.as_view(), name='answers'),
    path('create/', views.DataCreate.as_view(), name='data-create'),
    path('<int:id>/update/', views.DataUpdate.as_view(), name='data-update'),
]