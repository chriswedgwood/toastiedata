from django.core.management.base import BaseCommand
from easyscrape.spiders.member import MemberSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from toastiedata.club.models import Club, Member


class Command(BaseCommand):
    help = "Release the spiders"

    def handle(self, *args, **options):
        Member.objects.all().delete()
        Club.objects.get_or_create(title="London Victorians")
        process = CrawlerProcess(get_project_settings())
        process.crawl(MemberSpider)
        process.start()
