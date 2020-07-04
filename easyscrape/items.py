from scrapy_djangoitem import DjangoItem

from toastiedata.club.models import Member


class MemberItem(DjangoItem):
    django_model = Member
