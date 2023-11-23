from django.urls import path
from . import views

urlpatterns = [
               path('', views.all_grains, name="all_grains"),
               path('doesnthavetobesameasview/<int:param>/', views.single_grain, name="single_grain"),
               path('doesnthavetobesameasview/<str:param>/', views.single_grain, name="single_grain"),
               path('doesnthavetobesameasview/', views.single_grain, name="single_grain"),
               path('<int:param>', views.all_grains, name="all_grains"),
               path('random_path/', views.roast, name='roast'),
               # path('tryme', views.tryme, name='tryme')
              ]

