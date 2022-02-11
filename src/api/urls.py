from django.urls import path
from .views import UserView,UserDetail, ClientView, ClientDetail

urlpatterns  = [
	path('users/',UserView.as_view()),
	path('users/<int:pk>/',UserDetail.as_view()),

	path('clients/',ClientView.as_view()),
	path('clients/<int:pk>/',ClientDetail.as_view()),
	]