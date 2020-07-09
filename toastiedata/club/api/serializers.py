from rest_framework import serializers

from toastiedata.club.models import Member


class MemberSerializer(serializers.ModelSerializer):
    meeting_count = serializers.IntegerField()
    role_count = serializers.IntegerField()
    speech_count = serializers.IntegerField()

    class Meta:
        model = Member
        fields = [
            "full_name",
            "es_id",
            "join_date",
            "meeting_count",
            "role_count",
            "speech_count",
        ]
