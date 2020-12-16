from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Parking, Parkinglotlist
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ParkingSerializer, ParkinglotlistSerializer
from rest_framework.decorators import api_view
# Create your views here.


# Django Rest API CRUD operation
# First we fetch the data using get
# Second we save object by using post

# Listing all the the main Parkinglotlist showing the name of all parking lots
class ParkingLotList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'parkinglotmanager/parkinglot_list.html'

    def get(self, request):
        parkinglotlist = Parkinglotlist.objects.all()
        context = {
            'parkinglist': parkinglotlist
        }
        return Response(context)


class ParkingLotListDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'parkinglotmanager/parkinglot_detail.htm'

    def get(self, request, pk):
        query = get_object_or_404(Parking, pk=pk)
        serializer = ParkingSerializer(query)
        context = {
            'object': query,
            'serializer': serializer
        }
        return Response(context)

    def post(self, request, pk):
        query = get_object_or_404(Parking, pk=pk)
        serializer = ParkingSerializer(query, data=request.data)
        if not serializer.is_valid():
            context = {
                'object': query,
                'serialier': serializer
            }
            return Response(context)
        serializer.save()
        return redirect()

# CRUD of Parking model
class ParkingList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'parkinglotmanager/parking_list.html'

    def get(self, request):
        query = Parking.objects.all()
        context = {
            'object': query
        }
        return Response(context)


class ParkingUpdate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'parkinglotmanager/parking_update.html'

    def get(self, request, pk):
        query = get_object_or_404(Parking, pk=pk)
        serializer = ParkingSerializer(query)
        context = {
            'object': query,
            'serializer': serializer
        }
        return Response(context)

    def post(self, request, pk):
        query = get_object_or_404(Parking, pk=pk)
        serializer = ParkingSerializer(query, data=request.data)
        if not serializer.is_valid():
            context = {
                'object': query,
                'serialier': serializer
            }
            return Response(context)
        serializer.save()
        return redirect('alpr:parking-list')


class ParkingDelete(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'parkinglotmanager/parking_delete.html'

    def get(self, request, pk):
        query = get_object_or_404(Parking, pk=pk)
        serializer = ParkingSerializer(query)
        context = {
            'object': query,
            'serializer': serializer
        }
        return Response(context)

    def post(self, request, pk):
        query = get_object_or_404(Parking, pk=pk)
        if request.method == 'POST':
            query.delete()
        return redirect('alpr:parking-list')


class ParkingCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'parkinglotmanager/parking_create.html'

    def get(self, request):
        serializer = ParkingSerializer()
        context = {
            'serializer': serializer
        }
        return Response(context)

    def post(self, request):
        serializer = ParkingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            context = {
                'serializer': serializer
            }
            return Response(context)
        return redirect('alpr:parking-list')

#@api_view(['DELETE'])
def Task_Delete(request, pk):
    tasklist = get_object_or_404(Parking, pk=pk)
    tasklist.delete()
    return redirect("alpr:parking-list")


# This is to list all related child parent via a foreign key 
class LotDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'parkinglotmanager/parkinglot_child.html'

    def get(self, request, pk):
        queryset = Parking.objects.filter(parkinglotid_id=pk)
        context = {
            'parkinglist': queryset
        }
        print(context)
        return Response(context)




# This is unnecessary because we don't need to view the parking lot detail
# we can comment it out but remember to do the same to urls.py
class ParkingDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'parkinglotmanager/parkinglot_detail.html'
    def get(self, request, pk):
        parking = get_object_or_404(Parking, pk=pk) 
        query = Parking.objects.filter(pk=pk)
        context = {
                'parking': parking
                }
        print(context)
        return Response(context)
