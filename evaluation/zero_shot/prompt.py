import json
import argparse
from utils.boolean_api import Boolean as BooleanAPI
from utils.multichoice_api import Multichoice as MultichoiceAPI
from utils.factoid_api import Factoid as FactoidAPI

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--question_type', type=str, required=True)
    parser.add_argument('--prompt_type', type=str, required=True)
    parser.add_argument('--model', type=str, required=True)
    parser.add_argument('--language', type=str, required=True)
    parser.add_argument('--finetune_inference', type=bool, required=True)
    parser.add_argument('--api-key', type=str, required=True)

    args = parser.parse_args()
    question_type = args.question_type
    prompt_type = args.prompt_type
    model = args.model
    language = args.language
    finetune_inference = args.finetune_inference
    api_key = args.api_key

    if finetune_inference:
        json_url = '../../dataset/test.json'
    else:
        json_url = '../../dataset/full.json'
    with open(json_url, 'r', encoding='utf8') as f:
        json_data = json.load(f)

    if question_type == 'boolean':
        if prompt_type == 'api':
            boolean = BooleanAPI(model, language, api_key)
        else:
            boolean = None
        boolean.qa(json_data[question_type])
    elif question_type == 'factoid':
        if prompt_type == 'api':
            factoid = FactoidAPI(model, language, api_key)
        else:
            factoid = None
        factoid.qa(json_data[question_type])
    elif question_type == 'multichoice':
        if prompt_type == 'api':
            multichoice = MultichoiceAPI(model, language, api_key)
        else:
            multichoice = None
        multichoice.qa(json_data[question_type])
