from functools import reduce
import requests
import json
import math

USD_COURSE = 26.9579
EUR_COURSE = 30.5092

try:
    data = requests.get("https://public-api.nazk.gov.ua/v1/declaration/1c2a5064-f1bc-4ee5-b3e6-d9b3b37db48d").json()
# poroshenko - 539d7fe3-7cfa-4d88-8a97-070b0841f56e
# bezsmertnyi - 8ced3078-d83b-47a9-a595-edc9aa4d8f74
# tymoshenko - 5e670ba6-12d8-4d30-bd65-bfcb800cbd60
# zelenskii - 1c2a5064-f1bc-4ee5-b3e6-d9b3b37db48d
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
    if len(available_checks_list) != 0:
        sum_of_availables = reduce((lambda x, y: x + y), available_checks_list)
    else:
        return 1.01
    return sum_of_availables


def movables_worth():
    step_5 = data["data"]["step_5"]
    declared_elements = list(find_keys(step_5, "costDateUse"))
    available_movable_prices = []
    for i in declared_elements:
        if i != '':
            available_movable_prices.append(int(i))
    if len(available_movable_prices) != 0:
        sum_of_availables = reduce((lambda x, y: x + y), available_movable_prices)
    else:
        return 1.01
    return sum_of_availables


def vehicles_worth():
    step_6 = data["data"]["step_6"]
    declared_vehicles = list(find_keys(step_6, "costDate"))
    available_venicle_prices = []
    for i in declared_vehicles:
        if i != '':
            available_venicle_prices.append(int(i))
    if len(available_venicle_prices) != 0:
        sum_of_availables = reduce((lambda x, y: x + y), available_venicle_prices)
    else:
        return 1.01
    return sum_of_availables


def securities_worth():
    step_7 = data["data"]["step_7"]
    declared_papers = list(find_keys(step_7, "cost"))
    available_securities_prices = []
    for price in declared_papers:
        if price != '':
            available_securities_prices.append(int(price))
    if len(available_securities_prices) != 0:
        sum_of_availables = reduce((lambda x, y: x + y), available_securities_prices)
    else:
        return 1.01
    return sum_of_availables


def corporation_rights():
    step_8 = data["data"]["step_8"]
    declared_rights = list(find_keys(step_8, "cost"))
    available_rights_prices = []
    for price in declared_rights:
        if price != '':
            available_rights_prices.append(int(price))
    if len(available_rights_prices) != 0:
        sum_of_availables = reduce((lambda x, y: x + y), available_rights_prices)
    else:
        return 1.01
    return sum_of_availables


def revenue_volume():
    step_11 = data["data"]["step_11"]
    declared_revenue = list(find_keys(step_11, "sizeIncome"))
    available_revenue_volume = []
    for revenue in declared_revenue:
        if revenue != '':
            available_revenue_volume.append(int(revenue))
    if len(available_revenue_volume) != 0:
        sum_of_availabilities = reduce((lambda x, y: x + y), available_revenue_volume)
    else:
        return 1.01
    return sum_of_availabilities


def cash_assets():
    step_12 = data["data"]["step_12"]
    candidate_currencies = list(find_keys(step_12, "assetsCurrency"))
    amount_of_currencies = list(map(int, list(find_keys(step_12, "sizeAssets"))))
    list_of_sums_in_uah = []
    for i in range(0, len(candidate_currencies)):
        if candidate_currencies[i] == 'USD':
            list_of_sums_in_uah.append(amount_of_currencies[i] * USD_COURSE)
        elif candidate_currencies[i] == 'EUR':
            list_of_sums_in_uah.append(amount_of_currencies[i] * EUR_COURSE)
        else:
            list_of_sums_in_uah.append(amount_of_currencies[i])
    if len(list_of_sums_in_uah) != 0:
        total_sum_in_uah = reduce((lambda x, y: x + y), list_of_sums_in_uah)
    else:
        return 1.01
    return total_sum_in_uah


def sincerity_coefficient(declared_elements = 0, revealed_elements = 0):
    pass


last_name = data["data"]["step_1"]["lastname"]
is_married = is_married()
realty_worth = math.log(realty_worth())
movables_worth = math.log(movables_worth())
vehicles_worth = math.log(vehicles_worth())
securities_worth = math.log(securities_worth())
corporation_rights = math.log(corporation_rights())
revenue_volume = math.log(revenue_volume())
cash_assets = math.log(cash_assets())
sincerity_coefficient = sincerity_coefficient()
print(last_name)
print(is_married)
print(realty_worth)
print(movables_worth)
print(vehicles_worth)
print(securities_worth)
print(corporation_rights)
print(revenue_volume)
print(cash_assets)
