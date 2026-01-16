import json


def validate(json_file):
    assert len(json_file) == 270
    ids = [q['id'] for q in json_file]
    assert all([_id not in all_ids for _id in ids])
    all_ids.extend(ids)
    questions_dict = {}
    for q in json_file:
        _id = q['id']
        category = '_'.join(_id.split('_')[:-1])
        difficulty = q['difficulty']
        if category not in questions_dict:
            questions_dict[category] = {}
        if difficulty not in questions_dict[category]:
            questions_dict[category][difficulty] = 0
        questions_dict[category][difficulty] += 1
    assert len(questions_dict) == 18
    print(json.dumps(questions_dict, indent=4))
    [print() for _ in range(1,4)]


if __name__ == '__main__':
    all_ids = []
    with open(f'./difficulty_validation_shuffled.json', 'r') as f:
        json_file = json.load(f)
    validate(json_file)
    print(len(all_ids))