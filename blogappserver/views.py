from django.shortcuts import render
from rest_framework import viewsets
from . serializer import BloggerSerializer, UserSerializer
from . models import Blogger
from django.contrib.auth.models import User
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django.http import JsonResponse, HttpResponse


# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser


# Create your views here.


class BloggerViewSet(viewsets.ModelViewSet):
    queryset = Blogger.objects.all().order_by('id')
    serializer_class = BloggerSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def getDetails(request):
    details = {'name': 'sagar', "address": 'delhi'}
    return JsonResponse(details)


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })


# @api_view(['GET', 'POST'])
# def blog_list(request):
#     if request.method == 'GET':
#         data = Blogger.objects.all()

#         serializer = BloggerSerializer(data, context={'request': request}, many=True)

#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = BloggerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT', 'DELETE'])
# def blog_detail(request, pk):
#     try:
#         blogger = Blogger.objects.get(pk=pk)
#     except Blogger.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PUT':
#         serializer = BloggerSerializer(blogger, data=request.data,context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         blogger.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @csrf_exempt
# def snippet_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Blogger.objects.all()
#         serializer = BloggerSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = BloggerSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def snippet_detail(request):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Blogger.objects.get('id')
#     except Blogger.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = BloggerSerializer(snippet)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = BloggerSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)
