from django.urls import path

from . import views

app_name = 'lists_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('to_compleated/<int:completed_id>', views.to_compleated, name="to_compleated"),
    path('add_it/', views.add_it, name="add_it"),
    path('delete_it/', views.delete_it, name="delete_it"),
]
