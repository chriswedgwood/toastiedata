select * from club_club C 
JOIN club_meeting M On M.club_id=C.id 
JOIN club_memberrole MR ON MR.meeting_id = M.id
JOIN club_member ON club_member.id = MR.member_id
JOIN club_role R ON R.id = MR.role_id
--order by M.date desc
where M.date = '2020-06-30'



    select * from club_club C 
    JOIN club_meeting M On M.club_id=C.id 
    JOIN club_memberspeech MS ON MS.meeting_id = M.id
    JOIN club_member CM ON CM.id = MS.member_id
    JOIN club_pathwayspeech PS ON PS.id = MS.pathway_speech_id
    JOIN club_pathwaylevel PL ON PL.id = PS.level_id
    JOIN club_pathway PW ON PW.id = PL.pathway_id
    where M.date = '2020-06-30'


select CM.es_id,CM.full_name,* from club_member CM
JOIN club_memberspeech MS ON MS.member_id = CM.id
JOIN club_meeting M ON M.id = MS.meeting_id
JOIN club_pathwayspeech PS ON PS.id = MS.pathway_speech_id
    JOIN club_pathwaylevel PL ON PL.id = PS.level_id
    JOIN club_pathway PW ON PW.id = PL.pathway_id

--SPEECHES
select CM.es_id,count(*) cnt speeches from club_member CM
JOIN club_memberspeech MS ON MS.member_id = CM.id
JOIN club_meeting M ON M.id = MS.meeting_id
JOIN club_pathwayspeech PS ON PS.id = MS.pathway_speech_id
    JOIN club_pathwaylevel PL ON PL.id = PS.level_id
    JOIN club_pathway PW ON PW.id = PL.pathway_id
    GROUP BY CM.es_id,CM.full_name
    ORDER BY 3 desc

--ROLES
select es_id,count(*) from club_club C 
JOIN club_meeting M On M.club_id=C.id 
JOIN club_memberrole MR ON MR.meeting_id = M.id
JOIN club_member ON club_member.id = MR.member_id
JOIN club_role R ON R.id = MR.role_id
GROUP BY es_id

--MEETINGS
SELECT es_id,count(*) FROM club_attendance A 
JOIN club_member CM ON CM.id = A.member_id
GROUP BY es_id

select * from club_attendance A 
JOIN club_member CM ON CM.id = A.member_id
where es_id = 20474


---API QUERY FRO MEMEBERS---

    SELECT full_name,join_date,meeting_count,role_count,speech_count FROM club_member M 
    JOIN (SELECT es_id,count(*) meeting_count FROM club_attendance A
            JOIN club_meeting M On M.id=A.
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
    WHERE M.join_date IS NOT NULL 
ORDER BY 2 desc


24	Jackie Gallego	2018-02-06	49407	49407	92	49407	19	49407	6