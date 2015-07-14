import json
def get_labeled_items(json):
    item_ids = []
    if json['menu']['items']:
        for item in json['menu']['items']:
            try:
                if 'label' in item:
                    item_ids.append(item['id'])
            except TypeError:
                pass
    return item_ids

# for test in test_cases:
#     ids = get_labeled_items(json.loads(test))
#     return sum(ids)
