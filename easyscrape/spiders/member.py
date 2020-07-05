import csv
from datetime import datetime

import scrapy
from bs4 import BeautifulSoup
from easyscrape.items import MemberItem
from scrapy.http import Request


class MemberSpider(scrapy.Spider):
    name = "member"
    start_urls = ["https://toastmasterclub.org/login.php"]
    member_ids = []

    custom_settings = {"ITEM_PIPELINES": {"easyscrape.pipelines.MemberPipeline": 300, }}

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={"username": "cwlv", "password": "9752f82d"},
            callback=self.after_login,
        )

    def after_login(self, response):
        url = "https://toastmasterclub.org/memberchart.php?c=486&chart=9"
        yield Request(url=url, callback=self.action)

    def action(self, response):
        with open("tm_members.csv", "w", newline="\n", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(
                ["id", "Name", "Joined", ]
            )

        data = response.text
        soup = BeautifulSoup(data, features="lxml")
        workbook_history_table = soup.find(string="Mentor").find_parent("table")
        table_rows = workbook_history_table.find_all("tr")
        users = []

        for tr in table_rows:
            td = tr.find_all("td")
            row = [i.text.strip("\n") for i in td]
            print(row)
            # if len(td) >3:
            if len(row) == 7:
                user_id = td[0].span.a["href"][-5:]
                row.append(user_id)
                users.append(row)
        for row in users:
            with open("tm_members.csv", "a", newline="\n", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(row)
            join_date = datetime.strptime(row[4], "%d %b %y").date()
            member_data = {"full_name": row[0], "join_date": join_date, "es_id": row[7]}
            item = MemberItem(member_data)
            yield item
