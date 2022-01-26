import requests
import csv
import sys


category_list = ["askstories", "showstories", "newstories", "jobstories"]
if len(sys.argv) > 1:
    category_from_user = sys.argv[1]
else:
    category_from_user = "newstories"
if category_from_user not in category_list:
    print("Такої категорії немає...")
    raise SystemExit()

id_list = requests.get(f"https://hacker-news.firebaseio.com/v0/"
                       f"{category_from_user}.json?print=pretty").json()

all_keys_list = []

for id in id_list:
    try:
        page_keys = requests.get(f"https://hacker-news.firebaseio.com/v0/"
                                 f"item/{id}.json?print=pretty").json()
        for key in page_keys:
            if key not in all_keys_list:
                all_keys_list.append(key)
    except:
        pass

with open(f"{category_from_user}.csv", 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, dialect='excel', delimiter=';')
    writer.writerow(all_keys_list)

main_dict = {}
for key in all_keys_list:
    tmp_dict = {key: "null"}
    main_dict.update(tmp_dict)

for id in id_list:
    list_to_csv = []
    dict_to_csv = main_dict.copy()
    try:
        page = requests.get(f"https://hacker-news.firebaseio.com/v0/"
                            f"item/{id}.json?print=pretty").json()
        for key in page.keys():
            dict_to_csv[key] = page[key]
        for i in dict_to_csv.keys():
            list_to_csv.append(dict_to_csv[i])
        with open(f"{category_from_user}.csv", 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='excel', delimiter=';')
            writer.writerow(list_to_csv)
        print("write done")
    except:
        pass