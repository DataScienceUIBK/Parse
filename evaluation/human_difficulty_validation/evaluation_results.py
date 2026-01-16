import json
import statistics
from prettytable import PrettyTable


######### Boolean Multihop #########
def boolean_multihop_comparative(ground_truth, prediction):
    q_diff = ground_truth['difficulty']
    g_answer = ground_truth['answer']
    p_answer = prediction['human_answer']
    score = int(g_answer == p_answer)
    return 'boolean', q_diff, score


def boolean_multihop_negation(ground_truth, prediction):
    q_diff = ground_truth['difficulty']
    g_answer = ground_truth['answer']
    p_answer = prediction['human_answer']
    score = int(g_answer == p_answer)
    return 'boolean', q_diff, score


def boolean_multihop_simple(ground_truth, prediction):
    q_diff = ground_truth['difficulty']
    g_answer = ground_truth['answer']
    p_answer = prediction['human_answer']
    score = int(g_answer == p_answer)
    return 'boolean', q_diff, score


######### Boolean Reasoning #########
def boolean_reasoning_comparative(ground_truth, prediction):
    q_diff = ground_truth['difficulty']
    g_answer = ground_truth['answer']
    p_answer = prediction['human_answer']
    score = int(g_answer == p_answer)
    return 'boolean', q_diff, score


def boolean_reasoning_negation(ground_truth, prediction):
    q_diff = ground_truth['difficulty']
    g_answer = ground_truth['answer']
    p_answer = prediction['human_answer']
    score = int(g_answer == p_answer)
    return 'boolean', q_diff, score


def boolean_reasoning_simple(ground_truth, prediction):
    q_diff = ground_truth['difficulty']
    g_answer = ground_truth['answer']
    p_answer = prediction['human_answer']
    score = int(g_answer == p_answer)
    return 'boolean', q_diff, score


######### Factoid Multihop #########
def factoid_multihop_listbased(ground_truth, prediction):
    q_diff = ground_truth['difficulty']
    g_answers = set([ans.strip().lower() for ans in ground_truth['answer']])
    if prediction['human_answer'] is None:
        prediction['human_answer'] = ''
    p_answers = set([ans.strip().lower() for ans in prediction['human_answer'].split('؛')])

    score = len(g_answers & p_answers) / len(g_answers)
    return 'factoid', q_diff, score


def factoid_multihop_nonanswerable(ground_truth, prediction):
    q_diff = ground_truth['difficulty']
    g_answer = ground_truth['answer']
    p_answer = prediction['human_answer']
    score = int(g_answer == p_answer)
    return 'factoid', q_diff, score


def factoid_multihop_simple(ground_truth, prediction):
    q_diff = ground_truth['difficulty']
    g_answer = ground_truth['answer'].lower().strip()
    if prediction['human_answer'] is None:
        prediction['human_answer'] = ''
    p_answer = prediction['human_answer'].lower().strip()
    score = int(g_answer == p_answer)
    return 'factoid', q_diff, score


######### Factoid Reasoning #########
def factoid_reasoning_listbased(ground_truth, prediction):
    q_diff = ground_truth['difficulty']
    g_answers = set([ans.strip().lower() for ans in ground_truth['answer']])
    if prediction['human_answer'] is None:
        prediction['human_answer'] = ''
    p_answers = set([ans.strip().lower() for ans in prediction['human_answer'].split('؛')])

    score = len(g_answers & p_answers) / len(g_answers)
    return 'factoid', q_diff, score


def factoid_reasoning_nonanswerable(ground_truth, prediction):
    q_diff = ground_truth['difficulty']
    g_answer = ground_truth['answer']
    p_answer = prediction['human_answer']
    score = int(g_answer == p_answer)
    return 'factoid', q_diff, score


def factoid_reasoning_simple(ground_truth, prediction):
    q_diff = ground_truth['difficulty']
    g_answer = ground_truth['answer'].lower().strip()
    if prediction['human_answer'] is None:
        prediction['human_answer'] = ''
    p_answer = prediction['human_answer'].lower().strip()
    score = int(g_answer == p_answer)
    return 'factoid', q_diff, score


######### Multichoice Multihop #########
def multichoice_multihop_multi(ground_truth, prediction):
    q_diff = ground_truth['difficulty']
    g_answers = set(ground_truth['answer'])
    if prediction['human_answer'] is None:
        prediction['human_answer'] = []
    p_answers = set(prediction['human_answer'])

    score = len(g_answers & p_answers) / len(g_answers)
    return 'mutlichoice', q_diff, score


def multichoice_multihop_non_answerable(ground_truth, prediction):
    q_diff = ground_truth['difficulty']
    if prediction['human_answer'] is None:
        prediction['human_answer'] = 'هیچ‌کدام'
    p_answer = prediction['human_answer']

    score = int(p_answer == 'هیچ‌کدام')
    return 'mutlichoice', q_diff, score


def multichoice_multihop_single(ground_truth, prediction):
    q_diff = ground_truth['difficulty']
    g_answers = ground_truth['answer']
    if prediction['human_answer'] is None:
        prediction['human_answer'] = ''
    p_answer = prediction['human_answer']

    score = int(p_answer in g_answers)
    return 'mutlichoice', q_diff, score


######### Multichoice Reasoning #########
def multichoice_reasoning_multi(ground_truth, prediction):
    q_diff = ground_truth['difficulty']
    g_answers = set(ground_truth['answer'])
    if prediction['human_answer'] is None:
        prediction['human_answer'] = []
    p_answers = set(prediction['human_answer'])

    score = len(g_answers & p_answers) / len(g_answers)
    return 'mutlichoice', q_diff, score


def multichoice_reasoning_non_answerable(ground_truth, prediction):
    q_diff = ground_truth['difficulty']
    if prediction['human_answer'] is None:
        prediction['human_answer'] = 'هیچ‌کدام'
    p_answer = prediction['human_answer']

    score = int(p_answer == 'هیچ‌کدام')
    return 'mutlichoice', q_diff, score


def multichoice_reasoning_single(ground_truth, prediction):
    q_diff = ground_truth['difficulty']
    g_answers = ground_truth['answer']
    if prediction['human_answer'] is None:
        prediction['human_answer'] = ''
    p_answer = prediction['human_answer']

    score = int(p_answer in g_answers)
    return 'mutlichoice', q_diff, score


def main():
    id_function_map = {'boolean_multihop_comparative': boolean_multihop_comparative,
                       'boolean_multihop_negation': boolean_multihop_negation,
                       'boolean_multihop_simple': boolean_multihop_simple,
                       'boolean_reasoning_comparative': boolean_reasoning_comparative,
                       'boolean_reasoning_negation': boolean_reasoning_negation,
                       'boolean_reasoning_simple': boolean_reasoning_simple,
                       'factoid_multihop_listbased': factoid_multihop_listbased,
                       'factoid_multihop_nonanswerable': factoid_multihop_nonanswerable,
                       'factoid_multihop_simple': factoid_multihop_simple,
                       'factoid_reasoning_listbased': factoid_reasoning_listbased,
                       'factoid_reasoning_nonanswerable': factoid_reasoning_nonanswerable,
                       'factoid_reasoning_simple': factoid_reasoning_simple,
                       'multichoice_multihop_multi': multichoice_multihop_multi,
                       'multichoice_multihop_non_answerable': multichoice_multihop_non_answerable,
                       'multichoice_multihop_single': multichoice_multihop_single,
                       'multichoice_reasoning_multi': multichoice_reasoning_multi,
                       'multichoice_reasoning_non_answerable': multichoice_reasoning_non_answerable,
                       'multichoice_reasoning_single': multichoice_reasoning_single}

    with open('./difficulty_validation_shuffled.json', 'r') as f:
        ground_truth_json = json.load(f)

    results = dict()

    table = PrettyTable(['Question Type', 'Easy', 'Medium', 'Hard'])

    annotators = ['P1', 'P2', 'P3']
    for annotator in annotators:
        with open(f'./evaluation/human_answers_{annotator}.json', 'r') as f:
            prediction_json = json.load(f)
        for ground_truth, prediction in zip(ground_truth_json, prediction_json):
            _id = ground_truth['id']
            question_type = '_'.join(_id.split('_')[:-1])
            q_type, difficulty, score = id_function_map[question_type](ground_truth, prediction)
            if q_type not in results:
                results[q_type] = dict()
            if difficulty not in results[q_type]:
                results[q_type][difficulty] = []
            results[q_type][difficulty].append(score)
    for q_type in ['factoid', 'boolean', 'mutlichoice']:
        for difficulty in results[q_type]:
            results[q_type][difficulty] = round(statistics.mean(results[q_type][difficulty]), 3)
        table.add_row([q_type, results[q_type]['Easy'], results[q_type]['Medium'], results[q_type]['Hard']])
    print(table)


if __name__ == '__main__':
    main()
