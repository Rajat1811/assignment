from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Contact
from .serializers import ContactSerializer
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.filters import SearchFilter

# Create your views here.
class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ["first_name", "last_name", "email"]

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# class ContactList(ListCreateAPIView):
#     serializer_class = ContactSerializer
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
#     filter_backends = [SearchFilter]
#     search_fields = ['first_name','last_name','email']

#     def perform_create(self, serializer):
#         serializer.save(user= self.request.user)

#     def get_queryset(self):
#         return  Contact.objects.filter(user = self.request.user)


# class ContactDetailView(RetrieveUpdateDestroyAPIView):
#     serializer_class = ContactSerializer
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [permissions.IsAuthenticated,]
#     lookup_field = 'id'
#     filter_backends = [SearchFilter]
#     search_fields = ['first_name','last_name','email']

#     def get_queryset(self):
#         return  Contact.objects.filter(user = self.request.user)

