
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, viewsets

from .models import Client, Mailing, Message


#Serializers to be used

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class MailingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mailing
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'
 



#ViewSets declaration

class ClientViewSet(viewsets.ModelViewSet):
    
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()


class MailingViewSet(viewsets.ModelViewSet):
    serializer_class = MailingSerializer
    queryset = Mailing.objects.all()

    @action(detail = True, methods = ['get'])
    def info(self, request, pk = None):
    
        
        #summary data for specific mailing list        

        queryset = Mailing.objects.all()

        mailing = get_object_or_404(queryset, pk = pk)          


        serializer = MailingSerializer(mailing)

        return Response(serializer.data)
                                                                                                        
    
    @action(detail=False, methods=['get'])
    def fullinfo(self, request):         
        
        
        #summary data for all mails
               

        queryset = Mailing.objects.all()

        serializer = MailingSerializer(queryset, many = True)
        
        return Response(serializer.data)

