from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Camara
from .serializers import ProductoSerializer

class ProductoList(APIView):
    def get(self, request):
        productos = Camara.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
