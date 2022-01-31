import requests
import csv
import sys

class RequestsParse(object):

    @staticmethod
    def check_category():
        category_list = ["askstories", "showstories", "newstories", "jobstories"]
        if len(sys.argv) > 1:
            category_from_user = sys.argv[1]
        else:
            category_from_user = "newstories"
        if category_from_user not in category_list:
            print("Такої категорії немає...")
            raise SystemExit()

        RequestsParse.id_list = requests.get(f"https://hacker-news.firebaseio.com/v0/"
                               f"{category_from_user}.json?print=pretty").json()

        return category_from_user, RequestsParse.id_list

    @staticmethod
    def take_values():
        dict_to_csv = {}
        category_from_user, id_list = RequestsParse.check_category()
        for id in id_list:
            for key in dict_to_csv:
                dict_to_csv[key] = "null"
            list_to_csv = []
            try:
                page = requests.get(f"https://hacker-news.firebaseio.com/v0/"
                                         f"item/{id}.json?print=pretty").json()
                for key in page.keys():
                    if key not in dict_to_csv.keys():
                        dict_to_csv.update({key: "null"})
                        dict_to_csv[key] = page[key]
                    else:
                        dict_to_csv[key] = page[key]
                for value in dict_to_csv.values():
                    list_to_csv.append(value)
                with open(f"{category_from_user}.csv", 'a', newline='', encoding='utf-8') as f:
                         writer = csv.writer(f, dialect='excel', delimiter=';')
                         writer.writerow(list_to_csv)
            except:
                pass

        with open(f"{category_from_user}.csv", 'r+', newline='', encoding='utf-8') as f:
            old_csv = f.read()
            f.seek(0)
            writer = csv.writer(f, dialect='excel', delimiter=';')
            writer.writerow(dict_to_csv.keys())
            f.write(old_csv)

RequestsParse.take_values()