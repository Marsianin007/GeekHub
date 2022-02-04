import requests
from django.shortcuts import render
from .forms import MyModelForm
from .models import AskModel, ShowModel, JobModel, NewsModel


def make_dict(post_id):
    dict_to_return = {"post_id": 0}
    try:
        page = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{post_id}.json?print=pretty").json()
        for key in page.keys():
            tmp = {key: page[key]}
            dict_to_return.update(tmp)
    except:
        print("Error: post not found")
    return dict_to_return


def do_parse(request):
    if request.method == "POST":
        form = MyModelForm(request.POST)
        id_list = requests.get(f"https://hacker-news.firebaseio.com/v0/"
                               f"{form['category'].value()}.json?print=pretty").json()

        if form["category"].value() == "askstories":
            for id_from_list in id_list:
                base_object = AskModel.objects.all().filter(post_id=id_from_list)
                if len(base_object) == 0:
                    keys_list = []
                    for key in AskModel._meta.get_fields():
                        keys_list.append(str(key).split(".")[2])
                    main_dict = make_dict(id_from_list)
                    for key in keys_list:
                        if key not in main_dict.keys():
                            tmp = {key: "null"}
                            main_dict.update(tmp)
                    model = AskModel(by=main_dict["by"], post_id=id_from_list, score=main_dict["score"],
                                     time=main_dict["time"], title=main_dict["title"], type=main_dict["type"],
                                     text=main_dict["text"], descendants=main_dict["descendants"],
                                     kids=main_dict["kids"])
                    model.save()
                else:
                    print("Вже є")

        if form["category"].value() == "showstories":
            for id_from_list in id_list:
                base_object = ShowModel.objects.all().filter(post_id=id_from_list)
                if len(base_object) == 0:
                    keys_list = []
                    for key in ShowModel._meta.get_fields():
                        keys_list.append(str(key).split(".")[2])
                    main_dict = make_dict(id_from_list)
                    for key in keys_list:
                        if key not in main_dict.keys():
                            tmp = {key: "null"}
                            main_dict.update(tmp)
                    model = ShowModel(by=main_dict["by"], post_id=id_from_list, score=main_dict["score"],
                                      time=main_dict["time"], title=main_dict["title"], type=main_dict["type"],
                                      url=main_dict["url"], text=main_dict["text"],
                                      descendants=main_dict["descendants"],
                                      kids=main_dict["kids"])
                    model.save()
                else:
                    print("Вже є")

        if form["category"].value() == "jobstories":
            for id_from_list in id_list:
                base_object = JobModel.objects.all().filter(post_id=id_from_list)
                if len(base_object) == 0:
                    keys_list = []
                    for key in JobModel._meta.get_fields():
                        keys_list.append(str(key).split(".")[2])
                    main_dict = make_dict(id_from_list)
                    for key in keys_list:
                        if key not in main_dict.keys():
                            tmp = {key: "null"}
                            main_dict.update(tmp)
                    model = JobModel(by=main_dict["by"], post_id=id_from_list, score=main_dict["score"],
                                     time=main_dict["time"], title=main_dict["title"], type=main_dict["type"],
                                     url=main_dict["url"])
                    model.save()
                else:
                    print("Вже є")

        if form["category"].value() == "newstories":
            for id_from_list in id_list:
                base_object = NewsModel.objects.all().filter(post_id=id_from_list)
                if len(base_object) == 0:
                    keys_list = []
                    for key in NewsModel._meta.get_fields():
                        keys_list.append(str(key).split(".")[2])
                    main_dict = make_dict(id_from_list)
                    for key in keys_list:
                        if key not in main_dict.keys():
                            tmp = {key: "null"}
                            main_dict.update(tmp)
                    model = NewsModel(by=main_dict["by"], descendants=main_dict["descendants"], post_id=id_from_list,
                                      kids=main_dict["kids"], score=main_dict["score"], time=main_dict["time"],
                                      title=main_dict["title"], type=main_dict["type"], url=main_dict["url"])
                    model.save()
                else:
                    print("Вже є")

    form = MyModelForm()
    context = {
        'form': form
    }
    return render(request, 'site_parse/index.html', context)
