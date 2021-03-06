from django.contrib import admin

from toastiedata.club.models import (
    Club,
    Meeting,
    Member,
    MemberRole,
    MemberSpeech,
    Pathway,
    PathwayLevel,
    PathwaySpeech,
    Role,
)


class MemberSpeechAdmin(admin.ModelAdmin):
    list_display = ("title", "meeting", "pathway_speech", "member")
    search_fields = ["member"]


admin.site.register(Club)
admin.site.register(Member)
admin.site.register(Role)
admin.site.register(Meeting)
admin.site.register(Pathway)
admin.site.register(PathwayLevel)
admin.site.register(PathwaySpeech)
admin.site.register(MemberSpeech, MemberSpeechAdmin)
admin.site.register(MemberRole)
