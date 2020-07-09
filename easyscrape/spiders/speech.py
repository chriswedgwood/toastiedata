import csv
import re
from datetime import datetime

import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request


class SpeechSpider(scrapy.Spider):
    name = "speeches"
    start_urls = ["https://toastmasterclub.org/login.php"]
    member_ids = []

    custom_settings = {"ITEM_PIPELINES": {"easyscrape.pipelines.SpeechPipeline": 300,}}

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
        with open("tm_speeches.csv", "w", newline="\n", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(
                ["id", "Name", "Club", "WorkBook", "Speech", "title", "completed", ""]
            )

        data = response.text
        soup = BeautifulSoup(data, features="lxml")
        workbook_history_table = soup.find(string="Mentor").find_parent("table")
        table_rows = workbook_history_table.find_all("tr")
        user_ids = []
        for tr in table_rows:
            td = tr.find_all("td")
            row = [i.text.strip("\n") for i in td]
            print(row)
            if len(td) > 1:
                user_id = td[0].span.a["href"][-5:]
                if user_id not in user_ids:
                    user_ids.append(user_id)

        print(f"USER_IDS:{user_ids}")

        for id in user_ids:
            # id = 54991
            # id = 49407
            url = f"https://toastmasterclub.org/profile_cc.php?u={id}"
            yield Request(url=url, callback=self.get_user_info, meta={"id": id})

    def get_user_info(self, response):
        pathways = []
        id = response.meta.get("id")
        print(f"id:{id}")

        self.member_ids.append(id)
        data = response.text
        soup = BeautifulSoup(data, features="lxml")
        workbook_history_table = soup.find(string="Workbook History").find_parent(
            "table"
        )
        workbooks_span = workbook_history_table.findAll("span", {"class": "smalltitle"})

        for span in workbooks_span:
            pathway = span.text.strip().replace("(Pathway) ", "")
            print(pathway)

        for _, tr in enumerate(workbook_history_table.find_all("tr", recursive=False)):
            pathway = tr.find("span", {"class": "smalltitle"}) or None
            speech_span = tr.find("span", {"class": "gen"}) or None

            if pathway:
                pathway_text = pathway.text.strip().replace("(Pathway) ", "")
                pathways.append(pathway_text)
            if speech_span:
                title = tr.find("a", {"class": "gen"})
                print(title)

                if speech_span.text:
                    assignment = speech_span.text.strip().replace("(Pathway) ", "")

                if title:

                    completed_obj = tr.findAll(text=re.compile("Completed "))

                    if completed_obj:
                        completed_span = completed_obj[0].find_parent()
                        completed_a = completed_span.find_all("a")

                        if len(completed_a) == 1:
                            completed_date = completed_span.text[-9:]
                        else:
                            completed_date = completed_a[-1].text

                        completed_date = datetime.strptime(
                            completed_date, "%d %b %y"
                        ).date()
                        level = assignment[:7]
                        if level[:5] != "Level":
                            level = "Level 0"
                        assignment = assignment[8:]
                        speech_data = {
                            "pathway": pathways[-1],
                            "level": level,
                            "assignment": assignment,
                            "speech_title": title.text,
                            "completed_date": completed_date,
                            "es_id": id,
                        }
                        yield speech_data
