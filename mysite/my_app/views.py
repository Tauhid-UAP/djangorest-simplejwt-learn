from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer
# Create your views here.

class MyView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Looks like you are authorized!'}
        return Response(content)

class UserCreateView(APIView):
    def post(self, request):
        data = {}
        print('Getting POST data: ', request.data)

        serializer_data = {}
        serializer_data['first_name'] = request.data['firstName']
        serializer_data['last_name'] = request.data['lastName']
        serializer_data['username'] = request.data['username']
        serializer_data['email'] = request.data['email']
        serializer_data['password'] = request.data['password']
        print('serializer_data: ', serializer_data)
        serializer = UserSerializer(data=serializer_data)
        print('serializer: ', serializer)

        print('Checking validity:')
        if serializer.is_valid():
            print('Valid!')
            user = serializer.save()
            data['response'] = 'User created successfully.'
            data['first_name'] = user.first_name
            data['last_name'] = user.last_name
            data['email'] = user.email
            data['username'] = user.username

            return Response(data)
            
        print('Invalid!')
        data = serializer.errors
        print(data)

        return Response(data)


# simplejwt documentation

# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html
#                                         --------------------
# simplejwt tutorial

# https://simpleisbetterthancomplex.com/tutorial/2018/12/19/how-to-use-jwt-authentication-with-django-rest-framework.html
#                                         --------------------
# cURL commands for testing

# POST create user by providing the necessary fields
# curl -X POST -H "Content-Type: application/json" -d "{\"firstName\": \"Kamruzzaman\", \"lastName\": \"Tauhid\", \"username\": \"tauhid\", \"email\": \"17201114@uap-bd.edu\", \"password\": \"eastwestnets\"}" http://127.0.0.1:8000/user_create_view/
# Response: {"response":"User created successfully.","first_name":"Kamruzzaman","last_name":"Tauhid","email":"17201114@uap-bd.edu","username":"tauhid"}

# POST obtain jwt token pair using username and password
# curl -X POST -H "Content-Type: application/json" -d "{\"username\": \"tauhid\", \"password\": \"eastwestnets\"}" "http://localhost:8000/api/token/"
# Response: {"refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzMDkzMTQ5NywianRpIjoiY2UzYmYwMDUyODllNDU4M2EyYmVkMmNiYTlhNTg3ODciLCJ1c2VyX2lkIjozfQ.TpS24XiCbtwxolQXu21qh6GEi3OezsVkFF_cJZ7U6TA","access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMwODQ1Mzk3LCJqdGkiOiIxZjRhMmM4MGYwNGI0NWQzYTYxNGI1NzI1ZTNmM2IwYyIsInVzZXJfaWQiOjN9.rGtkv1LE8CtcsMZ4yXVFdWxNBEgWE6A_jbJxk8Qkq8U"}

# POST obtain new access token using refresh token
# curl -X POST -H "Content-Type: application/json" -d "{\"refresh\":\"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzMDkzMTQ5NywianRpIjoiY2UzYmYwMDUyODllNDU4M2EyYmVkMmNiYTlhNTg3ODciLCJ1c2VyX2lkIjozfQ.TpS24XiCbtwxolQXu21qh6GEi3OezsVkFF_cJZ7U6TA\"}" http://localhost:8000/api/token/refresh/
# Response: {"access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMwODQ1NjY2LCJqdGkiOiI3MzRhNDAzMWNkYTU0ZWQyYjgxODA4NGQ2NGQ4MzQ2ZCIsInVzZXJfaWQiOjN9.7sKaxaXzI833cskO5b20evibd_aCwFZjDbhcg72p77U"}

# GET access protected view
# curl -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMwODQ1NjY2LCJqdGkiOiI3MzRhNDAzMWNkYTU0ZWQyYjgxODA4NGQ2NGQ4MzQ2ZCIsInVzZXJfaWQiOjN9.7sKaxaXzI833cskO5b20evibd_aCwFZjDbhcg72p77U" http://localhost:8000/my_view/
# Response: {"message":"Looks like you are authorized!"}