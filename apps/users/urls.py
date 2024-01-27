from django.urls import path, re_path, include

from apps.users import views

app_name = 'users'
urlpatterns = [
    re_path(r'^register/$', views.RegisterView.as_view(), name='register'),
]
