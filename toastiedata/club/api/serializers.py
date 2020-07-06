from toastiedata.club.models import Member
from rest_framework import serializers


class MemberSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Member
        fields = ['full_name']


