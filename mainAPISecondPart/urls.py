from django.urls import path

from .views import request_for_create_log_message

urlpatterns = [
    path('log-message-request/create/', request_for_create_log_message, name="log-message-request-create")
]
