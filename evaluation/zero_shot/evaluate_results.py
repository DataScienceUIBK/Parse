import json
import inspect
from statistics import mean
from prettytable import PrettyTable


def prepare_answers_as_dict(answers):
    final_dict = dict()
    for itm in answers:
        q_id, predicted_answer = itm['id'], itm['predicted_answer']
        final_dict[q_id] = predicted_answer
    return final_dict


####################### Boolean #######################

def evaluate_boolean(answer, predicted_answer, sub_sub_method):
    return int(answer == predicted_answer)


def boolean(language):
    _method_name = inspect.stack()[0][3]
    fields = ['Model']
    for _submethod in full_dataset[_method_name]:
        for _subsubmethod in full_dataset[_method_name][_submethod]:
            fields.append(f'{_submethod} - {_subsubmethod}')
    table = PrettyTable(fields)
    for _model in models:
        with open(f'./prompt_results/{_method_name}/{language}/answers_{_model}.json', 'r', encoding='utf8') as f:
            answers = prepare_answers_as_dict(json.load(f))
        final_result = dict()
        for _submethod in full_dataset[_method_name]:
            if _submethod not in final_result:
                final_result[_submethod] = dict()
            for _subsubmethod in full_dataset[_method_name][_submethod]:
                if _subsubmethod not in final_result[_submethod]:
                    final_result[_submethod][_subsubmethod] = []
                for q in full_dataset[_method_name][_submethod][_subsubmethod]:
                    q_id = q['id']
                    answer = q['answer']
                    predicted_answer = answers[q_id]
                    """"""""""""""""""
                    evaluated_value = evaluate_boolean(answer, predicted_answer, _subsubmethod)
                    final_result[_submethod][_subsubmethod].append(evaluated_value)
                    """"""""""""""""""
        row = [_model]
        for _submethod in final_result:
            for _subsubmethod in final_result[_submethod]:
                final_result[_submethod][_subsubmethod] = round(mean(final_result[_submethod][_subsubmethod]), 2)
                row.append(final_result[_submethod][_subsubmethod])
        table.add_row(row)
    print(f'{language.capitalize()} prompt:')
    print(table)
    print(table.get_csv_string())
    print()


####################### Multichoice #######################

def evaluate_multichoice(answer, predicted_answer, options, sub_sub_method):
    if isinstance(answer, str):
        answer = [answer]
    answer_id = [options.index(ans) + 1 for ans in answer]

    if len(predicted_answer) == 0:
        return 0

    if sub_sub_method == 'multi':
        return len(set(answer_id) & set(predicted_answer)) / len(set(answer_id) | set(predicted_answer))
    elif sub_sub_method == 'non_answerable':
        return int(answer_id[0] == predicted_answer[0])
    elif sub_sub_method == 'single':
        return int(answer_id[0] == predicted_answer[0])


def multichoice(language):
    _method_name = inspect.stack()[0][3]
    fields = ['Model']
    for _submethod in full_dataset[_method_name]:
        for _subsubmethod in full_dataset[_method_name][_submethod]:
            fields.append(f'{_submethod} - {_subsubmethod}')
    table = PrettyTable(fields)
    for _model in models:
        with open(f'./prompt_results/{_method_name}/{language}/answers_{_model}.json', 'r', encoding='utf8') as f:
            answers = prepare_answers_as_dict(json.load(f))
        final_result = dict()
        for _submethod in full_dataset[_method_name]:
            if _submethod not in final_result:
                final_result[_submethod] = dict()
            for _subsubmethod in full_dataset[_method_name][_submethod]:
                if _subsubmethod not in final_result[_submethod]:
                    final_result[_submethod][_subsubmethod] = []
                for q in full_dataset[_method_name][_submethod][_subsubmethod]:
                    q_id = q['id']
                    answer = q['answer']
                    options = q['options']
                    predicted_answer = answers[q_id]
                    """"""""""""""""""
                    evaluated_value = evaluate_multichoice(answer, predicted_answer, options, _subsubmethod)
                    final_result[_submethod][_subsubmethod].append(evaluated_value)
                    """"""""""""""""""
        row = [_model]
        for _submethod in final_result:
            for _subsubmethod in final_result[_submethod]:
                final_result[_submethod][_subsubmethod] = round(mean(final_result[_submethod][_subsubmethod]), 2)
                row.append(final_result[_submethod][_subsubmethod])
        table.add_row(row)
    print(f'{language.capitalize()} prompt:')
    print(table)
    print(table.get_csv_string())
    print()


####################### Factoid #######################

def evaluate_factoid(answer, predicted_answer,  sub_sub_method):
    if isinstance(answer, str):
        answer = [answer]

    if sub_sub_method == 'listbased':
        detected_answers = set()
        for ans in answer:
            for p_ans in predicted_answer:
                if p_ans.find(ans) >= 0:
                    detected_answers.add(p_ans)
        return len(detected_answers) / max(len(answer), len(predicted_answer))
    elif sub_sub_method == 'nonanswerable':
        return int(len(predicted_answer) == 0)
    elif sub_sub_method == 'simple':
        detected_answers = set()
        for p_ans in predicted_answer:
            if p_ans.find(answer[0]) >= 0:
                detected_answers.add(p_ans)
        return len(detected_answers) / max(len(answer), len(predicted_answer))


def factoid(language):
    _method_name = inspect.stack()[0][3]
    fields = ['Model']
    for _submethod in full_dataset[_method_name]:
        for _subsubmethod in full_dataset[_method_name][_submethod]:
            fields.append(f'{_submethod} - {_subsubmethod}')
    table = PrettyTable(fields)
    for _model in models:
        with open(f'./prompt_results/{_method_name}/{language}/answers_{_model}.json', 'r', encoding='utf8') as f:
            answers = prepare_answers_as_dict(json.load(f))
        final_result = dict()
        for _submethod in full_dataset[_method_name]:
            if _submethod not in final_result:
                final_result[_submethod] = dict()
            for _subsubmethod in full_dataset[_method_name][_submethod]:
                if _subsubmethod not in final_result[_submethod]:
                    final_result[_submethod][_subsubmethod] = []
                for q in full_dataset[_method_name][_submethod][_subsubmethod]:
                    q_id = q['id']
                    answer = q['answer']
                    predicted_answer = answers[q_id]
                    """"""""""""""""""
                    evaluated_value = evaluate_factoid(answer, predicted_answer, _subsubmethod)
                    final_result[_submethod][_subsubmethod].append(evaluated_value)
                    """"""""""""""""""
        row = [_model]
        for _submethod in final_result:
            for _subsubmethod in final_result[_submethod]:
                final_result[_submethod][_subsubmethod] = round(mean(final_result[_submethod][_subsubmethod]), 4)
                row.append(final_result[_submethod][_subsubmethod])
        table.add_row(row)
    print(f'{language.capitalize()} prompt:')
    print(table)
    print(table.get_csv_string())
    print()


if __name__ == '__main__':
    models = ['llama-3-8b', 'persian-llama-3-8b', 'qwen-25-7b', 'mistral-24b',
              'gemma-2-27b', 'llama-3-70b', 'qwen-25-72b']
    with open('../../dataset/full.json', 'r', encoding='utf8') as f:
        full_dataset = json.load(f)

    method_map = {'boolean': boolean, 'multichoice': multichoice, 'factoid': factoid}

    for _method in method_map:
        print(f'{_method}: ')
        for language in ['english', 'persian']:
            method_map[_method](language)
        print()
        print()
