from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from olcha.models import Category, Group, Product, Image, PraductAttribute
from olcha.serializers import (CustomersModelSerializers,
                               GroupModelSerialize,
                               ProductSerialize,
                               ImageSerializer,
                               )
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
class CategoryListView(APIView):
    permission_classes = [IsAuthenticated]
    # authentication_classes = [SessionAuthentication ,BasicAuthentication]
    authentication_classes = [JWTAuthentication]
    def get(self,request):
        categories = Category.objects.all()
        serializers = CustomersModelSerializers(categories,many=True,context= { 'request':request })
        return Response(serializers.data,status=status.HTTP_200_OK)


class GroupListView(APIView):
    def get(self,request):
        groups = Group.objects.all()
        serializers = GroupModelSerialize(groups, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

class ProductListView(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializers = ProductSerialize(product, many=True,context={'request':request})
        return Response(serializers.data,status=status.HTTP_200_OK)

class ImagelistView(APIView):
    def get(self, request):
        image = Image.objects.all()
        serializers = ImageSerializer(image,many=True, context={'request':request})
        return Response(serializers.data, status=status.HTTP_200_OK)

# class ProductAtributListView(APIView):
#     def get(self):
#         atribut = PraductAttribute.objects.all()
#         serializers = AtrinutSerializer(atribut, many=True,read_only=True)
#         return Response(serializers.data, status=status.HTTP_200_OK)
class CategoryDelete(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomersModelSerializers
    queryset = Category.objects.all()
    lookup_field = 'pk'

# class CategoryModelViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CustomersModelSerializers

""" CRUD """


class CategitiyListCRUD(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    model = Category
    serializer_class = CustomersModelSerializers
    queryset = Category.objects.all()

class ProductList_CRUD(generics.ListAPIView):
    model = Product
    serializer_class = ProductSerialize
    queryset = Product.objects.all()
class GroupList_CRUD(generics.ListAPIView):
    model = Group
    serializer_class = GroupModelSerialize
    queryset = Group.objects.all()


class CategoryDetialCRUD(generics.RetrieveAPIView):
    model = Category
    serializer_class = CustomersModelSerializers
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset

class CategoryAddCRUD(generics.CreateAPIView):
    serializer_class = CustomersModelSerializers
    queryset = Category.objects.all()

class GroupAddCRUD(generics.CreateAPIView):
    serializer_class = GroupModelSerialize
    queryset = Group.objects.all()

class ProductAddCRUD(generics.CreateAPIView):
    serializer_class = ProductSerialize
    queryset = Product.objects.all()

class CategoryUpdata(generics.UpdateAPIView):
    serializer_class = CustomersModelSerializers
    queryset = Category.objects.all()
    lookup_field = 'pk'

class CategoryUpdata(generics.UpdateAPIView):
    serializer_class = CustomersModelSerializers
    queryset = Category.objects.all()
    lookup_field = 'pk'

class GroupUpdata(generics.UpdateAPIView):
    serializer_class = GroupModelSerialize
    queryset = Group.objects.all()
    lookup_field = 'pk'

class ProductUpdata(generics.UpdateAPIView):
    serializer_class = ProductSerialize
    queryset = Product.objects.all()
    lookup_field = 'pk'

class CategoryDelete(generics.DestroyAPIView):
    serializer_class = CustomersModelSerializers
    lookup_field = 'pk'
    queryset = Category.objects.all()
class GroupDelete(generics.DestroyAPIView):
    serializer_class = GroupModelSerialize
    lookup_field = 'pk'
    queryset = Group.objects.all()
class ProductDelete(generics.DestroyAPIView):
    serializer_class = ProductSerialize
    lookup_field = 'pk'
    queryset = Product.objects.all()

# """" ModelViewSet """
class CategoryModelViewSet(viewsets.ModelViewSet):
    serializer_class = CustomersModelSerializers
    queryset = Category.objects.all()
    lookup_field = 'pk'

class GroupModelViewSet(viewsets.ModelViewSet):
    serializer_class = GroupModelSerialize
    queryset = Group.objects.all()
    lookup_field = 'pk'

class ProductModelViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerialize
    queryset = Product.objects.all()
    lookup_field = 'pk'
