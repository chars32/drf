from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer

@api_view(['GET', 'POST'])
def user_api_view(request):

    if request.method == 'GET':
        users = User.objects.all()
        users_serialier = UserSerializer(users, many=True)
        return Response(users_serialier.data)

    elif request.method == 'POST':
        user_serialier = UserSerializer(data = request.data)
        if user_serialier.is_valid():
            user_serialier.save()
            return Response(user_serialier.data)
        return Response(user_serialier.errors)