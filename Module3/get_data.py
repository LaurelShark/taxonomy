import io
from functools import reduce
import requests
import json

try:
    data = requests.get("https://public-api.nazk.gov.ua/v1/declaration/8ced3078-d83b-47a9-a595-edc9aa4d8f74").json()
# poroshenko - 539d7fe3-7cfa-4d88-8a97-070b0841f56e
# bezsmertnyi - 8ced3078-d83b-47a9-a595-edc9aa4d8f74
#   with io.open("bezsmertnyi_data.json", "w", encoding="utf8") as json_file:
#        json.dump(data, json_file, ensure_ascii=False, indent=4, sort_keys=True)
except ValueError:
    print("getting data failed")
if data is not None:
    #  print(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))
    pass


def find_keys(node, kv):
    if isinstance(node, list):
        for i in node:
            for x in find_keys(i, kv):
                yield x
    elif isinstance(node, dict):
        if kv in node:
            yield node[kv]
        for j in node.values():
            for x in find_keys(j, kv):
                yield x


def is_married():
    if find_keys(data, 'дружина') or find_keys(data, 'чоловік'):
        spouse = 1
    else:
        spouse = 0
    return spouse


#
def realty_worth(j=0):
    step_3 = data["data"]["step_3"]
    costAssessment = list(find_keys(step_3, 'costAssessment'))
    costDate = list(find_keys(step_3, 'costDate'))
    available_checks_list = []
    print(costAssessment)
    print(costDate)

    for i in range(0, len(costAssessment)):

        if costAssessment[i] != '':
            available_checks_list.append(int(costAssessment[i]))

        if costDate[j] != '' and costAssessment[i] == '':
            available_checks_list.append(int(costDate[j]))

        j += 1
    sum_of_list = reduce((lambda x, y: x + y), available_checks_list)
    return sum_of_list


last_name = data["data"]["step_1"]["lastname"]
is_married = is_married()
# TODO ln()
realty_worth = realty_worth()
print(last_name)
print(is_married)
print(realty_worth)
