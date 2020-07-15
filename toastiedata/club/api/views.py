from django.db import connection
from django.shortcuts import render
from rest_framework import generics
from toastiedata.club.models import Member
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
        

        start = self.request.query_params.get('start', '2000-01-01')
        end = self.request.query_params.get('end', '2025-01-01')
        if len(start) == 0:
            start = '2000-01-01'
        if len(end) == 0:
            end = '2025-01-01'
        

        sql_query = """SELECT M.id,M.es_id,full_name,join_date,coalesce(meeting_count,0) meeting_count,coalesce(role_count,0) role_count,
        coalesce(speech_count,0) speech_count FROM club_member M 
    LEFT JOIN (SELECT es_id,count(*) meeting_count FROM club_attendance A
            JOIN club_meeting M On M.id=A.meeting_id
            JOIN club_member CM ON CM.id = A.member_id
            WHERE M.date > %s and M.date < %s
            GROUP BY es_id
            ) SQM ON SQM.es_id=M.es_id
    LEFT JOIN (select es_id,count(*) role_count  from club_club C 
            JOIN club_meeting M On M.club_id=C.id 
            JOIN club_memberrole MR ON MR.meeting_id = M.id
            JOIN club_member ON club_member.id = MR.member_id
            JOIN club_role R ON R.id = MR.role_id
            WHERE M.date > %s and M.date < %s
            GROUP BY es_id)  SQR ON SQR.es_id=M.es_id
    LEFT JOIN (SELECT CM.es_id,count(*) speech_count from club_member CM
        JOIN club_memberspeech MS ON MS.member_id = CM.id
        JOIN club_meeting M ON M.id = MS.meeting_id
        JOIN club_pathwayspeech PS ON PS.id = MS.pathway_speech_id
        JOIN club_pathwaylevel PL ON PL.id = PS.level_id
        JOIN club_pathway PW ON PW.id = PL.pathway_id
        WHERE M.date > %s and M.date < %s
        GROUP BY CM.es_id,CM.full_name) SQS ON SQS.es_id = M.es_id 
    WHERE M.join_date IS NOT NULL"""


        print(sql_query)
        print(start)
        print(end)
        # cursor = connection.cursor()
        # cursor.execute(sql_query)
        result = Member.objects.raw(sql_query, [start, end, start, end, start, end])
            
        return result
