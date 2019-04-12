from functools import reduce
import requests
import math
import csv

USD_COURSE = 26.9579
EUR_COURSE = 30.5092

candidates = {
    "poroshenko": "539d7fe3-7cfa-4d88-8a97-070b0841f56e",
    "tymoshenko": "5e670ba6-12d8-4d30-bd65-bfcb800cbd60",
    "zelenskyi": "1c2a5064-f1bc-4ee5-b3e6-d9b3b37db48d",
    "boyko": "b1a5b66f-e314-4004-ac70-396c075d36ec",
    "gritsenko": "5357e277-2934-4091-b5e0-4e48ee51f9f8",
    "lyashko": "0311129e-ea16-43b4-99b3-74b45c021020",
    "myraev": "e85e604e-bd9a-4228-97bd-f0f0a02efd03",
    "sadovyi": "95e19cca-1e38-4aac-b95d-c8361bbdeb3e",
    "vilkyl": "e7e9d0fa-c59f-42c4-965f-3598b3cb1c46",
    "koshylynskii": "da776581-9f25-4810-9a68-42a2046797b1",
    "tymoshenko_yurii": "808f3285-28be-4a0c-8b0d-510f56a5ce26",
    "shevchenko": "ad887ab6-5123-4ace-9688-06b6479c1d8a",
    "taryta": "84dfdd51-6328-4c39-883c-e81a702e300d",
    "kaplin": "09525d7a-f667-4b2b-928a-9dc166a79b1c",
    "bondar": "bc3ca5a6-b9d6-4e9e-a502-0465dab2482b",
    "dobrodomov": "e6b5705c-0c7e-4cf9-9f41-70c43efa2066",
    "derevyanko": "c0348f06-feb7-49fe-8c10-5983f3c9e884",
    "bohomolets": "392b50ae-399c-4226-9a19-e39f872c03cd",
    "kornatskyi": "bed5d66a-661b-4bf4-bb34-50cf3885fb33",
    "kryvenko": "800c102c-1f3e-4444-96b2-09bdc5a213b5",
    "kyprii": "8ca01efa-026c-4f56-a597-80be8fcb51a9",
    "bezsmertnyi": "8ced3078-d83b-47a9-a595-edc9aa4d8f74",
    "gnap": "ebc46ecc-04ac-44a0-a0fe-dd74889ed2d5",
    "kyva": "cb24d4ad-5ad2-4474-97df-5a05c3cd01b2",
    "nalyvaychenko": "58d0652d-1f58-4dc7-b3bf-a6551584599b",
    "smeshko": "19f470d6-c356-4fc2-b358-537a5b58b6cf",
    "nasirov": "f580a34e-9dad-4018-af2b-1022c16bfb8a",
    "shevchenko_igor": "e2910ae7-2259-4f5e-a768-5cac5e0cb397",
    "kryvonos": "c2ce4fd4-d79a-461b-a219-bfa0d950930b",
    "petrov": "6bda3b00-f8d7-458f-99f2-1a3399ce6b4e",
    "balashov": "6847dea6-9e55-4dc5-a8af-7f81a2be5f30",
    "soloviyov": "61fea75c-5967-4668-8d49-6136ce3fd604",
    "moroz": "3ad38687-70d1-4150-aa06-3c06b06c7aa6",
    'karmazin': "cdb758e8-e54d-48b4-9f0f-2e500a78b4fd",
    "bogoslovska": "001b474b-2cf8-4f11-bdf5-3e519df21c13",
    "danyliuk": "bed167d9-b2cb-44d7-87a4-6c9c80181675",
    "novak": "f650a829-dfa0-45e2-bea9-75387b6f2f65",
    "lytvynenko": "dbd8bfcb-a9d1-43e2-945a-83acb36cfcf9",
    "gaber": "175b580f-288d-4314-b492-59bcd3720c34",
    "skotsyk": "ed6cd752-6210-41cf-9843-f7d496aa6c9b",
    "rygovanov": "70a23b43-36d7-457c-8f56-acb62287f56c",
    "jyravliov": "ca4f9ccf-047d-46d6-952e-1927ea8b902e",
    "vaschenko": "7ee118e7-e23b-44ca-9702-172fc6a741f5",
    "nosenko": "dc9c1595-5cc7-4156-8d1e-b80b4d00aee4"
}

for candidate in candidates:
    try:
        data = requests.get("https://public-api.nazk.gov.ua/v1/declaration/" + candidates.get(candidate, "")).json()
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


    def sincerity_coefficient(declared_elements=0, revealed_elements=0):
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
    # TODO implementation
    sincerity_coefficient = sincerity_coefficient()
    person = [last_name,
              is_married,
              realty_worth,
              movables_worth,
              vehicles_worth,
              securities_worth,
              corporation_rights,
              revenue_volume,
              cash_assets]
    print(last_name)
    print(is_married)
    print(realty_worth)
    print(movables_worth)
    print(vehicles_worth)
    print(securities_worth)
    print(corporation_rights)
    print(revenue_volume)
    print(cash_assets)

    with open("data.csv", "a", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(person)
    csv_file.close()
