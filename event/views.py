from datetime import datetime, date
from django.http import JsonResponse
from icecream import ic
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from event.models import Event
from event.serializer import EventSerializer
from common.decorators import request_converting_to_object_id
from bson.objectid import ObjectId
from rest_framework.utils import json

@api_view(['GET', 'POST'])
# @parser_classes([JSONParser])
def event_all(request):
    if request.method == 'GET':
        all_event = Event.objects.all()
        serializer = EventSerializer(all_event, many=True)
        return Response(data=serializer.data)

    elif request.method == 'POST':
        new_event = request.data
        if Event.objects.count() == 0:
            new_event["event_id"] = 1
        else:
            new_event["event_id"] = Event.objects.filter(event_id__gt=0).last().event_id + 1
        serializer = EventSerializer(data=new_event)
        if serializer.is_valid():
            serializer.save()
            return Response({'result': f'Welcome,{serializer.data.get("event_id")}'}, status=201)

    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
# @parser_classes([JSONParser])
def event_by_id(request, id):
    try:
        event = Event.objects.get(event_id=id)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method =='GET':
        serializer = EventSerializer(event)
        return Response({'result': serializer.data}, status=201)

    elif request.method == 'PUT':
        serializer = EventSerializer(instance=event, data=request.data)
        ic(event, request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response({'result': f'Welcome,{serializer.data.get("event_id")}'}, status=201)

    elif request.method == 'DELETE':
        print("===delete까지 옴===")
        event.delete()
        return Response({'result': '삭제 성공'}, status=status.HTTP_204_NO_CONTENT)

    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_event_detail(request, id):
    try:
        event = Event.objects.get(event_id=id)
    except Event.DoesNotExist:
        # print(Event.objects.get(event))
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method =='GET':
        serializer = EventSerializer(event)
        start = serializer.data.get("start")
        end = serializer.data.get("end")
        created = serializer.data.get("created")
        ic(created)
        d_start = datetime.strptime(start, '%Y-%m-%d')
        d_end = datetime.strptime(end, '%Y-%m-%d')
        from_tz = "09:00"
        # d_created = datetime.strptime(created,f'%Y-%m-%dT%H:%M:%S.%f+%')
        # d_created2 = datetime.
        # ic(d_start, d_end,)
        return Response({'result': serializer.data}, status=201)



@api_view(['POST'])
def get_event_detail2(request):
    if request.method == "POST":
        # Event.objects.filter(id__gt=3).update(active=True, name='x')
        print('POST' + '=' * 100)
        new_event = request.data
        print(f'{new_event} \n =================')
        # Event.objects.get(_id=new_event.)
        # update(active=True, name='x')

        return Response({'result': f'Welcome,{new_event}'}, status=201)

    return Response({"result":"fail"}, status=status.HTTP_400_BAD_REQUEST)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
