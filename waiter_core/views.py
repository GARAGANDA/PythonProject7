from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from app_core.models import Order
from waiter_core.serializers import OrderSerializer


# Create your views here.
class OrderDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'order_detail.html'
    def get(self,request,pk):
        order = get_object_or_404(Order, pk=pk)
        serializer=OrderSerializer(order)
        return Response({"serializer":serializer,"order":order})
