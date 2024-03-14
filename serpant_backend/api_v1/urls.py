from django.urls import path
from .views.authentication import login_view, registration_view

app_name = 'waspsapi'

urlpatterns = [
    path('sign-in/', login_view, name='sign-in'),
    path('sign-up/', registration_view, name='sign-up')
]