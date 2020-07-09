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

        sql_query = """SELECT M.id,full_name,M.es_id,join_date,meeting_count,role_count,speech_count FROM club_member M 
                        JOIN (SELECT es_id,count(*) meeting_count FROM club_attendance A 
                                JOIN club_member CM ON CM.id = A.member_id
                                GROUP BY es_id
                                ) SQM ON SQM.es_id=M.es_id
                        JOIN (select es_id,count(*) role_count  from club_club C 
                                JOIN club_meeting M On M.club_id=C.id 
                                JOIN club_memberrole MR ON MR.meeting_id = M.id
                                JOIN club_member ON club_member.id = MR.member_id
                                JOIN club_role R ON R.id = MR.role_id
                                GROUP BY es_id)  SQR ON SQR.es_id=M.es_id
                        JOIN (SELECT CM.es_id,count(*) speech_count from club_member CM
                            JOIN club_memberspeech MS ON MS.member_id = CM.id
                            JOIN club_meeting M ON M.id = MS.meeting_id
                            JOIN club_pathwayspeech PS ON PS.id = MS.pathway_speech_id
                            JOIN club_pathwaylevel PL ON PL.id = PS.level_id
                            JOIN club_pathway PW ON PW.id = PL.pathway_id
                            GROUP BY CM.es_id,CM.full_name) SQS ON SQS.es_id = M.es_id 
                        WHERE M.join_date IS NOT NULL"""

        # cursor = connection.cursor()
        # cursor.execute(sql_query)
        result = Member.objects.raw(sql_query)
        return result
