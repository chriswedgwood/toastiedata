from django.shortcuts import render
from toastiedata.club.models import Member
from rest_framework import  generics
from .serializers import MemberSerializer
# Create your views here.

class MemberList(generics.ListAPIView):
    """
    Return a list of all the products that the authenticated
    user has ever purchased, with optional filtering.
    """
    model = Member
    serializer_class = MemberSerializer
  
    def get_queryset(self):
        return Member.objects.all()
