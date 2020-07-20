from toastiedata.club.models import (
    Attendance,
    Award,
    Club,
    Meeting,
    Member,
    MemberAward,
    MemberRole,
    MemberSpeech,
    Pathway,
    PathwayLevel,
    PathwaySpeech,
    Role,
)


class MemberPipeline(object):
    def process_item(self, item, spider):
        print("bnbnbnbn")
        member, created = Member.objects.update_or_create(
            es_id=item["es_id"], defaults=item
        )
        print(member)
        print(created)
        return member


class RolePipeline(object):
    def process_item(self, item, spider):
        print("bnbnbnbn")
        club = Club.objects.first()
        role, _ = Role.objects.get_or_create(title=item["role"])
        meeting, _ = Meeting.objects.get_or_create(date=item["role_date"], club=club)
        member = Member.objects.get(es_id=item["es_id"])
        role, _ = MemberRole.objects.get_or_create(
            member=member, role=role, meeting=meeting
        )
        return role


class SpeechPipeline(object):
    def process_item(self, item, spider):
        pathway = item["pathway"]
        level = item["level"]
        # assignment = item["assignment"]
        speech_title = item["speech_title"]
        completed_date = item["completed_date"]
        member = Member.objects.get(es_id=item["es_id"])
        club = Club.objects.first()
        pathway, _ = Pathway.objects.get_or_create(title=pathway)
        pathway_level, _ = PathwayLevel.objects.get_or_create(
            title=level, pathway=pathway
        )
        pathway_speech, _ = PathwaySpeech.objects.get_or_create(
            title=speech_title, level=pathway_level
        )
        meeting, _ = Meeting.objects.get_or_create(date=completed_date, club=club)
        member_speech, _ = MemberSpeech.objects.get_or_create(
            title=speech_title,
            meeting=meeting,
            pathway_speech=pathway_speech,
            member=member,
        )
        return member_speech


class MeetingPipeline(object):
    def process_item(self, item, spider):
        print("bnbnbnbn")
        club = Club.objects.first()
        meeting_date = item["meeting_datetime"].date()
        attendance = item["attendance"]
        awards = item["awards"]
        roles = item['roles']
        meeting, _ = Meeting.objects.get_or_create(date=meeting_date, club=club)
        for attendee in attendance:
            member, created = Member.objects.get_or_create(es_id=attendee[1])
            if created:
                member.full_name = attendee[0]
                member.save()
            m_attendance, _ = Attendance.objects.get_or_create(
                member=member, meeting=meeting
            )
        for item_award in awards:
            award, _ = Award.objects.get_or_create(title=item_award[0])
            member, created = Member.objects.get_or_create(es_id=item_award[2])
            if created:
                member.full_name = item_award[1]
                member.save()

            m_award, _ = MemberAward.objects.get_or_create(
                award=award, member=member, meeting=meeting
            )
        for item_role in roles:
            member, created = Member.objects.get_or_create(es_id=item_role[2])
            if created:
                member.full_name = attendee[0]
                member.save()
            m_attendance, _ = Attendance.objects.get_or_create(
                    member=member, meeting=meeting
                )

            role_title = item_role[0]
            if 'Educational' in item_role[0]:
                role_title = 'Educational'
            elif 'Contestant' in item_role[0]:
                role_title = 'Contestant'
            elif 'Club Business' in item_role[0]:
                role_title = 'Club Business'
            elif 'Topic Evaluator' in item_role[0]:
                role_title = 'Table Topics Evaluator'
            elif 'Evaluator' in item_role[0]:
                role_title = 'Speech Evaluator'
            elif 'Speaker' in item_role[0]:
                role_title = 'Speaker'
            if role_title not in ['Speaker', 'Contestant','Club Business']:
                role, _ = Role.objects.get_or_create(title=role_title)
                _, _ = MemberRole.objects.get_or_create(member=member, role=role, meeting=meeting)
            
            
            #    role, _ = Role.objects.get_or_create(title=item['role'])

    #   meeting, _ = Meeting.objects.get_or_create(date=item['role_date'])
    #   member = Member.objects.get(es_id=item['es_id'])
    #   role,_ = MemberRole.objects.get_or_create(member=member,role=role,meeting=meeting)
    #   return role
