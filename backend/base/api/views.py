from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .serializers import NoteSerializer
from ..models import Note


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
        '/api/register'
    ]
    return Response(routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    user = request.user
    notes = user.note_set.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addNote(request):
    try:
        data = request.data
        data['user_id'] = request.user.id
        note = Note.objects.create(**data)
        if note:
            return Response({'message': 'Note added successfully.'}, status=200)
    except Exception as e:
        return Response({"errors": str(e)}, status=400)


class Register(APIView):
    def post(self, request):
        data = request.data
        try:
            if "password" in data:
                data["password"] = make_password(data["password"])
            user = User.objects.create(**data)
            if user:
                return Response(status=201)
        except Exception as e:
            return Response({"errors": str(e)}, status=400)
