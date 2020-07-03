from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from toastiedata.club.models import Club
from toastiedata.easyscrape.spiders.meeting import MeetingSpider
from toastiedata.easyscrape.spiders.member import MemberSpider
from toastiedata.easyscrape.spiders.role import RoleSpider
from toastiedata.easyscrape.spiders.speech import SpeechSpider


class Command(BaseCommand):
    help = "Release the spiders"

    def handle(self, *args, **options):
       
        Club.objects.get_or_create(title="London Victorians")
        process = CrawlerProcess(get_project_settings())
        
        process.crawl(MemberSpider)
        process.crawl(SpeechSpider)
        process.crawl(MeetingSpider)
        process.crawl(RoleSpider)
       
        
        process.start()
