import requests
from django.db import models


CATEGORY_CHOICES = (
        ('newstories', 'newstories'),
        ('jobstories', 'jobstories'),
        ('showstories', 'showstories'),
        ('askstories', 'askstories'),
    )

class MyModel(models.Model):
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='news')

    def __str__(self):
        return self.category

class SaveModel(models.Model):
    by = "null"
    post_idd = "null"
    score = "null"
    time = "null"
    title = "null"
    type = "null"
    url = "null"
    text = "null"
    descendants = "null"
    kids = "null"

    category = MyModel()
    dict_to_csv = {}
    id_list = requests.get(f"https://hacker-news.firebaseio.com/v0/"
                           f"{category}.json?print=pretty").json()
    for post_id in id_list:
        for key in dict_to_csv:
            dict_to_csv[key] = "null"
        list_to_csv = []
        try:
            page = requests.get(f"https://hacker-news.firebaseio.com/v0/"
                                     f"item/{post_id}.json?print=pretty").json()
            for key in page.keys():
                if key not in dict_to_csv.keys():
                    dict_to_csv.update({key: "null"})
                    dict_to_csv[key] = page[key]
                else:
                    dict_to_csv[key] = page[key]

        except:
            pass

        try:
            by = dict_to_csv["by"]
        except KeyError:
            pass

        try:
            post_id = dict_to_csv["post_id"]
        except KeyError:
            pass

        try:
            score = dict_to_csv["score"]
        except KeyError:
            pass

        try:
            time = dict_to_csv["time"]
        except KeyError:
            pass

        try:
            title = dict_to_csv["title"]
        except KeyError:
            pass

        try:
            type = dict_to_csv["type"]
        except KeyError:
            pass

        try:
            url = dict_to_csv["url"]
        except KeyError:
            pass

        try:
            text = dict_to_csv["text"]
        except KeyError:
            pass

        try:
            descendants = dict_to_csv["descendants"]
        except KeyError:
            pass

        try:
            kids = dict_to_csv["kids"]
        except KeyError:
            pass

        def __str__(self):
            return '{}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(self.by, self.post_id, self.score, self.time, self.title,
                                                                   self.type, self.url, self.text, self.descendants,
                                                                   self.kids)



