import requests
from django.db import models


CATEGORY_CHOICES = (
        ('newstories', 'newstories'),
        ('jobstories', 'jobstories'),
        ('showstories', 'showstories'),
        ('askstories', 'askstories'),
    )

class MyModel(models.Model):
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='none')

    def __str__(self):
        return self.category

class AskModel(models.Model):
    result_str = ""
    result_list = []
    dict_to_csv = {"by" : "null", "post_id" : "null", "score" : "null", "time" : "null", "title" : "null",
                   "type" : "null", "url" : "null", "text" : "null", "descendants" : "null", "kids" : "null"}

    id_list = requests.get(f"https://hacker-news.firebaseio.com/v0/"
                           f"askstories.json?print=pretty").json()

    for for_id in id_list:
        tmp_list = []
        print(for_id)
        for key in dict_to_csv:
            dict_to_csv[key] = "null"
        try:
            page = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{for_id}.json?print=pretty").json()
            for key in page.keys():
                dict_to_csv[key] = page[key]
        except:
            print("error with parse")
        for key in dict_to_csv:
            tmp_list.append(str(dict_to_csv[key]))
        tmp_str = str(", ".join(tmp_list))  # спроба передачі у вигляді стрінгу
        result_list.append(tmp_str)  # спроба передачі у вигляді стрінгу
        result_str = ", ".join(result_list)  # спроба передачі у вигляді стрінгу

    by = dict_to_csv["by"]
    post_id = dict_to_csv["post_id"]
    score = dict_to_csv["score"]
    time = dict_to_csv["time"]
    title = dict_to_csv["title"]
    type = dict_to_csv["type"]
    url = dict_to_csv["url"]
    text = dict_to_csv["text"]
    descendants = dict_to_csv["descendants"]
    kids = dict_to_csv["kids"]

    def __str__(self):
        # return '{}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(self.by, self.post_id, self.score, self.time, self.title,
        #                                                        self.type, self.url, self.text, self.descendants,
        #                                                        self.kids)
        return self.result_str  # спроба передачі у вигляді стрінгу






