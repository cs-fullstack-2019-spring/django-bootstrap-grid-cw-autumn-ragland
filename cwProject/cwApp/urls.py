from django.urls import path
from . import views

urlpatterns = [
    # page 1
    path('', views.index, name='page_one'),
    # page 2
    path('page_two/', views.page_two, name='page_two'),
    # page 3
    path('page_three/', views.page_three, name='page_three')
]
