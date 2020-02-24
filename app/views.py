from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.status import HTTP_200_OK , HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticated, IsAdminUser,AllowAny,IsAuthenticatedOrReadOnly
from .serializers import PostSerializer,RegisterSerializer
from .models import Post




@api_view(['POST'])

def registration_view(request):

    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            account= serializer.save()

            data['response'] = 'successfully registered a new user.'
            data['email'] = account.email
            data['username'] = account.username

        else:
            data = serializer.errors

        return Response(data)

























# alot of code all are smae
class PostView(mixins.ListModelMixin ,mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = PostSerializer

    queryset = Post.objects.all()

    def get(self,request, *args , **kwargs):

        return self.list(request, *args , **kwargs)

    def post(self,request, *args , **kwargs):
        return self.create(request, *args , **kwargs)

#lesser code class all are same

class PostCreateView(mixins.ListModelMixin, generics.CreateAPIView):
    serializer_class = PostSerializer

    queryset = Post.objects.all()

    def get(self,request, *args , **kwargs):

        return self.list(request, *args , **kwargs)



# least less code class all are same
class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    queryset = Post.objects.all()



# class UserLoginAPIView(APIView):
#     permission_class = [AllowAny]
#     serializer_class = UserLoginSerializer
#
#     def post(self,request, *args , **kwargs):
#
#         data = request.data
#         serializer = UserLoginSerializer(data=data)
#
#         if serializer.is_valid(raise_exception=True):
#             new_data = serializer.data
#             return Response(new_data, status=HTTP_200_OK)
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)




# class TestView(APIView):
#
#     permission_class = (IsAuthenticated, )
#
#     def get(self,request, *args , **kwargs):
#
#         qs = Post.objects.all()
#         serializer = PostSerializer(qs, many=True)
#
#         return Response(serializer.data)
#
#
#     def post(self,request, *args , **kwargs):
#
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
