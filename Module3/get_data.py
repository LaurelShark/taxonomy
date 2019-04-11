import io
from functools import reduce
import requests
import json

try:
    data = requests.get("https://public-api.nazk.gov.ua/v1/declaration/539d7fe3-7cfa-4d88-8a97-070b0841f56e").json()
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
    cost_assessment = list(find_keys(step_3, "costAssessment"))
    cost_date = list(find_keys(step_3, 'costDate'))
    available_checks_list = []
    for i in range(0, len(cost_assessment)):

        if cost_assessment[i] != '':
            available_checks_list.append(int(cost_assessment[i]))

        if cost_date[j] != '' and cost_assessment[i] == '':
            available_checks_list.append(int(cost_date[j]))

        j += 1
    sum_of_availables = reduce((lambda x, y: x + y), available_checks_list)
    return sum_of_availables


def movables_worth():
    step_5 = data["data"]["step_5"]
    declared_elements = list(find_keys(step_5, "costDateUse"))
    available_movable_prices = []
    for i in declared_elements:
        if i != '':
            available_movable_prices.append(int(i))
    sum_of_availables = reduce((lambda x, y: x + y), available_movable_prices)
    return sum_of_availables


last_name = data["data"]["step_1"]["lastname"]
is_married = is_married()
# TODO ln()
realty_worth = realty_worth()
movables_worth = movables_worth()
print(last_name)
print(is_married)
print(realty_worth)
print(movables_worth)
