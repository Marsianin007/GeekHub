import requests
from django.shortcuts import render
from .forms import MyModelForm
from .models import AskModel, ShowModel, JobModel, NewsModel


def make_ask_and_show_dict(post_id):
    dict_to_csv = {"by": "null", "post_id": 0, "score": "null", "time": "null", "title": "null", "type": "null",
                   "url": "null", "text": "null", "descendants": "null", "kids": "null"}
    try:
        page = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{post_id}.json?print=pretty").json()
        for key in page.keys():
            tmp = {key: page[key]}
            dict_to_csv.update(tmp)
    except:
        print("Error: page not found")
    return dict_to_csv


def make_jobstories_dict(post_id):
    dict_to_csv = {"by": "null", "descendants": "null", "post_id": 0, "kids": "null", "score": "null",
                   "time": "null", "title": "null", "type": "null", "url": "null"}
    try:
        page = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{post_id}.json?print=pretty").json()
        for key in page.keys():
            tmp = {key: page[key]}
            dict_to_csv.update(tmp)
    except:
        print("jsdf")
    return dict_to_csv


def make_newstories_dict(post_id):
    dict_to_csv = {"by": "null", "descendants": "null", "post_id": 0, "score": "null", "time": "null", "title": "null", "type": "null",
                   "url": "null", "kids": "null"}
    try:
        page = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{post_id}.json?print=pretty").json()
        for key in page.keys():
            tmp = {key: page[key]}
            dict_to_csv.update(tmp)
    except:
        print("jsdf")
    return dict_to_csv


def do_parse(request):
    if request.method == "POST":
        form = MyModelForm(request.POST)

        if form["category"].value() == "askstories":
            id_list = requests.get(f"https://hacker-news.firebaseio.com/v0/"
                                   f"askstories.json?print=pretty").json()
            quantity = 0
            for id_from_list in id_list:
                quantity += 1
                base_object = AskModel.objects.all().filter(post_id=id_from_list)
                if len(base_object) == 0:
                    main_dict = make_ask_and_show_dict(id_from_list)
                    try:
                        model = AskModel(by=main_dict["by"], post_id=id_from_list, score=main_dict["score"],
                                         time=main_dict["time"], title=main_dict["title"], type=main_dict["type"],
                                         text=main_dict["text"], descendants=main_dict["descendants"],
                                         kids=main_dict["kids"])
                        model.save()
                    except KeyError:
                        pass
                else:
                    print("Вже є")

        if form["category"].value() == "showstories":
            id_list = requests.get(f"https://hacker-news.firebaseio.com/v0/"
                                   f"showstories.json?print=pretty").json()
            quantity = 0
            for id_from_list in id_list:
                quantity += 1
                base_object = ShowModel.objects.all().filter(post_id=id_from_list)
                if len(base_object) == 0:
                    main_dict = make_ask_and_show_dict(id_from_list)
                    try:
                        model = ShowModel(by=main_dict["by"], post_id=id_from_list, score=main_dict["score"],
                                          time=main_dict["time"], title=main_dict["title"], type=main_dict["type"],
                                          url=main_dict["url"], text=main_dict["text"],
                                          descendants=main_dict["descendants"],
                                          kids=main_dict["kids"])
                        model.save()
                    except KeyError:
                        pass
                else:
                    print("Вже є")

        if form["category"].value() == "jobstories":
            id_list = requests.get(f"https://hacker-news.firebaseio.com/v0/"
                                   f"jobstories.json?print=pretty").json()
            quantity = 0
            for id_from_list in id_list:
                quantity += 1
                base_object = JobModel.objects.all().filter(post_id=id_from_list)
                if len(base_object) == 0:
                    main_dict = make_jobstories_dict(id_from_list)
                    try:
                        model = JobModel(by=main_dict["by"], post_id=id_from_list, score=main_dict["score"],
                                         time=main_dict["time"], title=main_dict["title"], type=main_dict["type"],
                                         url=main_dict["url"])
                        model.save()
                    except KeyError:
                        pass
                else:
                    print("Вже є")

        if form["category"].value() == "newstories":
            id_list = requests.get(f"https://hacker-news.firebaseio.com/v0/"
                                   f"newstories.json?print=pretty").json()
            quantity = 0
            for id_from_list in id_list:
                quantity += 1
                base_object = NewsModel.objects.all().filter(post_id=id_from_list)
                if len(base_object) == 0:
                    main_dict = make_newstories_dict(id_from_list)
                    try:
                        model = NewsModel(by=main_dict["by"], descendants=main_dict["descendants"], post_id=id_from_list,
                                          kids=main_dict["kids"], score=main_dict["score"], time=main_dict["time"],
                                          title=main_dict["title"], type=main_dict["type"], url=main_dict["url"])
                        model.save()
                    except KeyError:
                        pass
                else:
                    print("Вже є")

    form = MyModelForm()
    context = {
        'form': form
    }
    return render(request, 'site_parse/index.html', context)
