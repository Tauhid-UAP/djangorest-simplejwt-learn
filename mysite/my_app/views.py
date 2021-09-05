from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.

class MyView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Looks like you are authorized!'}
        return Response(content)


# simplejwt documentation
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html

# simplejwt tutorial
# https://simpleisbetterthancomplex.com/tutorial/2018/12/19/how-to-use-jwt-authentication-with-django-rest-framework.html

# cURL commands for testing
# POST obtain jwt token pair using username and password
# curl -X POST -H "Content-Type: application/json" -d "{\"username\": \"hp\", \"password\": \"eastwestnets\"}" "http://localhost:8000/api/token/"
# Response: {"refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzMDkyMzU3NywianRpIjoiNzMwNDUzYTgzMTRkNGMzOGI0ZTQ0N2Y2YWQwMTZkMzEiLCJ1c2VyX2lkIjoxfQ.9eGNoWcFt78Z-oI0ENZdwfvyI8VWMrt53LC5Kf1gP8U","access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMwODM3NDc3LCJqdGkiOiJiM2ExNGE3Y2MyZWE0YjEwYmFhMDU2MzU1YWI5MWVmMSIsInVzZXJfaWQiOjF9.TYyFDoCAeV4UigoeqeedzKb0LGqNvrEmaz4JWE7mxQg"}

# POST obtain new access token using refresh token
# curl -X POST -H "Content-Type: application/json" -d "{\"refresh\":\"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzMDkyMzU3NywianRpIjoiNzMwNDUzYTgzMTRkNGMzOGI0ZTQ0N2Y2YWQwMTZkMzEiLCJ1c2VyX2lkIjoxfQ.9eGNoWcFt78Z-oI0ENZdwfvyI8VWMrt53LC5Kf1gP8U\"}" http://localhost:8000/api/token/refresh/
# Response: {"access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMwODM4MjU4LCJqdGkiOiI1N2JlNmI1ZmY0MDU0NDg5YWYxZGRhZTk3YzljMzg3ZCIsInVzZXJfaWQiOjF9.h7Dx3Xc5EgoXlvz8DjNe-GLp41udoc7fFVii4V6Gn0M"}

# GET access protected view
# curl -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMwODM4MjU4LCJqdGkiOiI1N2JlNmI1ZmY0MDU0NDg5YWYxZGRhZTk3YzljMzg3ZCIsInVzZXJfaWQiOjF9.h7Dx3Xc5EgoXlvz8DjNe-GLp41udoc7fFVii4V6Gn0M" http://localhost:8000/my_view/
# Response: {"message":"Looks like you are authorized!"}