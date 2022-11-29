from django.urls import path
from . import views

app_name = 'Dictionary'

urlpatterns = [
    
    path('',views.index_view,name = 'index'),
    path('word',views.word_view,name = 'word')
    
    ]