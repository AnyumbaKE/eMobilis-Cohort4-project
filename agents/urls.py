from django.urls import path
from . import views
from agents.views import model_form_upload


app_name = 'Agents'

urlpatterns = [
    path('', model_form_upload, name='agents'),

]