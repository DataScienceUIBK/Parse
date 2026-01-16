import os
import json
import random as rnd

rnd.seed(42)

from together import Together
from together.utils import check_file


def boolean(question, answer, prompt_template):
    json_item = {'messages': []}
    user_prompt_text = prompt_template.replace("<Question>", question)
    user_prompt = {"role": "user", "content": user_prompt_text}
    json_item['messages'].append(user_prompt)
    assistant_prompt_text = {'answer': 'Yes' if answer else 'No'}
    assistant_prompt = {"role": "assistant", "content": json.dumps(assistant_prompt_text)}
    json_item['messages'].append(assistant_prompt)
    return json_item


def multichoice(question, answer, options, prompt_template):
    if isinstance(answer, str):
        answer = [answer]
    json_item = {'messages': []}
    user_prompt_text = prompt_template.replace("<Question>", question).replace('<Option_1>', options[0]).replace(
        '<Option_2>', options[1]).replace('<Option_3>', options[2]).replace('<Option_4>', options[3])
    user_prompt = {"role": "user", "content": user_prompt_text}
    json_item['messages'].append(user_prompt)
    answer_id = sorted([options.index(ans) + 1 for ans in answer])
    assistant_prompt_text = {'answer': answer_id}
    assistant_prompt = {"role": "assistant", "content": json.dumps(assistant_prompt_text)}
    json_item['messages'].append(assistant_prompt)
    return json_item


def factoid(question, answer, prompt_template):
    if answer is None:
        answer = []
    elif isinstance(answer, str):
        answer = [answer]
    json_item = {'messages': []}
    user_prompt_text = prompt_template.replace("<Question>", question)
    user_prompt = {"role": "user", "content": user_prompt_text}
    json_item['messages'].append(user_prompt)
    assistant_prompt_text = {'answers': answer}
    assistant_prompt = {"role": "assistant", "content": json.dumps(assistant_prompt_text)}
    json_item['messages'].append(assistant_prompt)
    return json_item


def make_together_ai_files():
    with open('../dataset/train.json', 'r', encoding='utf-8') as f:
        train_set = json.load(f)
    train_together_ai = []
    for language in ['english', 'persian']:
        for q_type in train_set:
            with open(f'./{language}_prompt/{q_type}.txt', 'r', encoding='utf-8') as f:
                prompt_template = f.read()
            for sub_type in train_set[q_type]:
                for sub_sub_type in train_set[q_type][sub_type]:
                    for q in train_set[q_type][sub_type][sub_sub_type]:
                        question = q['question']
                        answer = q['answer']
                        options = q['options'] if 'options' in q else None
                        if q_type == 'boolean':
                            json_line = boolean(question, answer, prompt_template)
                        elif q_type == 'multichoice':
                            json_line = multichoice(question, answer, options, prompt_template)
                        elif q_type == 'factoid':
                            json_line = factoid(question, answer, prompt_template)
                        train_together_ai.append(json_line)
    rnd.shuffle(train_together_ai)
    with open('./together_ai_data_format/train_together.jsonl', 'w') as f:
        for line in train_together_ai:
            f.write(json.dumps(line) + '\n')


def check_files():
    client = Together(api_key=TOGETHER_API_KEY)

    sft_report = check_file('./together_ai_data_format/train_together.jsonl')
    print(json.dumps(sft_report, indent=2))

    assert sft_report["is_check_passed"] == True

    train_file_resp = client.files.upload('./together_ai_data_format/train_together.jsonl', check=True)
    return train_file_resp.id  # Save this ID for starting your fine-tuning job


if __name__ == '__main__':
    TOGETHER_API_KEY = 'YOUR_TOGETHER_AI_API_KEY'
    make_together_ai_files()
    train_file_id = check_files()
