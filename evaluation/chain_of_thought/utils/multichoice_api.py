import json
import asyncio
import os
import re
import random as rnd

rnd.seed(42)

from copy import deepcopy
from termcolor import colored
from together import AsyncTogether
from tenacity import retry
from tqdm import tqdm


class Multichoice:

    def __init__(self, model_url, language, api_key):
        self._class_type = self.__class__.__name__.lower()
        self.base_path = "./prompt_results"
        with open(f'../../Dataset/final_dataset/full.json', mode='r', encoding='utf8') as f:
            self.dataset = json.load(f)
        self.language = language
        self.api_key = api_key

        with open(f'./utils/{self.language}_prompt/{self._class_type}.txt', mode='r', encoding='utf8') as f:
            self._prompt_template = f.read()
        self.model_url = model_url

        models_map = {
            'meta-llama-3-8b-instruct-lite': 'llama-3-8b',
            'llama-3.3-70b-instruct-turbo': 'llama-3-70b',
            'mistral-small-24b-instruct-2501': 'mistral-24b',
            'qwen2.5-7b-instruct-turbo': 'qwen-25-7b',
            'qwen2.5-72b-instruct-turbo': 'qwen-25-72b',
            'google': 'gemma-2-27b',
            'dorna-llama3-8b-instruct-persianqa-afba6231-d1dbbaca': 'persian-llama-3-8b',
            'meta-llama-3-8b-instruct-persianqa-finetuned-44415861-7915f60b': 'persian-llama-3-8b-finetuned',
            'meta-llama-3-8b-instruct-persianqa-f5fffacc-adbb5454': 'llama-3-8b-finetuned'
        }
        self.model_name = models_map[self.model_url.split('/')[1].lower()]

        self.answers = []
        if os.path.exists(f'./{self.base_path}/{self._class_type}/{self.language}/answers_{self.model_name}.json'):
            with open(f'./{self.base_path}/{self._class_type}/{self.language}/answers_{self.model_name}.json', mode='r',
                      encoding='utf8') as f:
                self.answers = json.load(f)

    async def extract_final_json(self, text):
        """
        Extracts the last {...} JSON object from text and parses it.
        Returns a dict if valid, else None.
        """
        matches = list(re.finditer(r'\{[\s\S]*?\}', text))
        if not matches:
            return None

        last_json = matches[-1].group(0).strip()

        try:
            return json.loads(last_json)
        except json.JSONDecodeError:
            return None

    async def _extract_content(self, content):
        content_json = await self.extract_final_json(content)
        answer = content_json['answer']
        # print(answer)

        if len(answer) > 0 and isinstance(answer[0], str):
            answer = [int(ans) for ans in answer]

        filtered_answer = []
        for val in answer:
            if 1 <= val <= 4:
                filtered_answer.append(val)

        answer = deepcopy(filtered_answer)

        if len(answer) > 0 and not (1 in answer or 2 in answer or 3 in answer or 4 in answer):
            raise Exception()

        output = list(sorted(answer))
        return output

    @retry()
    async def _prompt_thread(self, qid_prompt):
        q_id, prompt = qid_prompt
        client = AsyncTogether(api_key=self.api_key)
        response = await client.chat.completions.create(
            model=self.model_url,
            messages=prompt,
            temperature=round(rnd.random(), 2),
            top_p=0.7,
            max_tokens=1024
        )
        return q_id, await self._extract_content(response.choices[0].message.content)

    def _to_prompt(self, questions: list):
        prompts = []
        for q in questions:
            q_id = q['id']
            q_text = q['question']
            q_options = q['options']
            prompt_text = ((self._prompt_template.replace("<Question>", q_text)
                            .replace("<Option_1>", q_options[0]).replace("<Option_2>", q_options[1]))
                           .replace("<Option_3>", q_options[2])).replace("<Option_4>", q_options[3])
            prompt_structured = [{"role": "user", "content": prompt_text}]
            prompts.append((q_id, prompt_structured))
        return prompts

    async def _prompt(self, batch):
        q_ids, prompts = zip(*batch)
        tasks = []
        for qid_prompt in batch:
            tasks.append(asyncio.create_task(self._prompt_thread(qid_prompt)))
        results = dict()
        for task in asyncio.as_completed(tasks):
            task = await task
            results[task[0]] = task[1]
        predict_answers = [{'id': _qid, 'predicted_answer': results[_qid]} for _qid in q_ids]
        return predict_answers

    def qa(self, _qs):
        os.makedirs(f'./{self.base_path}/{self._class_type}/{self.language}', exist_ok=True)
        batch_size = 128

        print(colored(
            f'Loading {self.model_name} to generate answers for {self._class_type} using {self.language} prompt...',
            'yellow'))
        print()

        num_of_answers = 0
        for sub_type in _qs:
            for sub_sub_type in _qs[sub_type]:
                questions = _qs[sub_type][sub_sub_type]
                question_batches = [questions[i:i + batch_size] for i in range(0, len(questions), batch_size)]
                for _q_batch in tqdm(question_batches, f'{sub_type} - {sub_sub_type}'):
                    num_of_answers += len(_q_batch)
                    if num_of_answers <= len(self.answers):
                        continue
                    while True:
                        try:
                            _p_batch = self._to_prompt(_q_batch)
                            results = asyncio.run(self._prompt(_p_batch))
                            self.answers.extend(results)
                            with open(
                                    f'./{self.base_path}/{self._class_type}/{self.language}/answers_{self.model_name}.json',
                                    mode='w', encoding='utf8') as f:
                                json.dump(self.answers, f, indent=4)
                            break
                        except KeyboardInterrupt:
                            exit()
                        except:
                            pass
