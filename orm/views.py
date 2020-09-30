from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Shoe, Shoes_Brand, Framework
from .serializers import ShoeSerializer, ShoesBrandSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets  # , permissions
# Create your views here.


class list_object(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'rest/list.html'
    def get(self, request):

        queryset = Shoe.objects.all()
        context = {
            'object': queryset
        }
        print(context)
        return Response(context)


class detail_object(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'rest/detail.html'

    def get(self, request, pk):
        queryset = get_object_or_404(Shoe, id=pk)
        context = {
            'object': queryset
        }
        print(context)
        return Response(context)


class update_object(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'rest/update.html'

    def get(self, request, pk):
        shoe = get_object_or_404(Shoe, id=pk)
        serializer = ShoeSerializer(Shoe)
        context = {
            'serializer': serializer,
            'shoe': shoe
        }
        return Response(context)

    def post(self, request, pk):
        shoe = get_object_or_404(Shoe, id=pk)
        serializer = ShoeSerializer(Shoe, data=request.data)
        context = {
            'serializer': serializer,
            'shoe': shoe
        }
        if not serializer.is_valid():
            return Response(context)
        serializer.save()
        return redirect('orm:shoe-list"')


# def list_object(request):
# 	query_set = shoe.objects.get(id=2)
# 	context = {
# 		'object' : query_set
# 	}
# 	return render(request, 'rest/detail.html', context)


class ShoeViewSet(viewsets.ModelViewSet):
    #	permission_classes = ([permissions.IsAuthenticated])
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer


class ShoesBrandViewSet(viewsets.ModelViewSet):
    #	permission_classes = ([permissions.IsAuthenticated])
    queryset = Shoes_Brand.objects.all()
    serializer_class = ShoesBrandSerializer
