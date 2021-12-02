import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Endpoint for sending request for creating LogMessage
@api_view(['POST'])
def request_for_create_log_message(request):
    response = requests.post('http://127.0.0.1:8000/log-message/create/', data=request.data)

    if response.status_code == 201:
        return Response('LogMessage was created!', status=status.HTTP_201_CREATED)
    elif response.status_code == 400:
        return Response('Identifier or/and Code are not correct!', status=status.HTTP_400_BAD_REQUEST)
