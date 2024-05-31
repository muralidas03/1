from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item #* - all models come
from .serializers import ItemSerializer

class ItemListCreate(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemInfo(APIView):
    def get(self,request,id):
        try:
            obj = Item.objects.get(id=id)
        except Item.DoesNotExist:
            msg={"msg":"Not Found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serializer =ItemSerializer(obj)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,id):
        try:
            obj = Item.objects.get(id=id)
       
        except Item.DoesNotExist:
            msg={"msg":"Not Found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
       
       
        serializer =ItemSerializer(obj,data=request.data)
       
       
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        try:
            obj = Item.objects.get(id=id)
        except Item.DoesNotExist:
            msg={"msg":"Not Found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)   