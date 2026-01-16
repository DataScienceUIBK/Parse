import json
import os
from prettytable import PrettyTable


def main():
    table = PrettyTable(['group', 'ambiguity', 'readability', 'correctness'])

    for group in ['1', '2', '3', '4']:
        quality_assess_dict = {'ambiguity': 0, 'readability': 0, 'correctness': 0}
        json_files = os.listdir(f'./groups/group_{group}/evaluations')
        for json_file in json_files:
            with open(f'./groups/group_{group}/evaluations/{json_file}', 'r') as f:
                data = json.load(f)
            for q in data:
                for quality_key in quality_assess_dict.keys():
                    quality_assess_dict[quality_key] += q[quality_key]
        for quality_key in quality_assess_dict.keys():
            quality_assess_dict[quality_key] = round(quality_assess_dict[quality_key] / (len(data) * 3), 3)
        table.add_row([f'Group {group}'] + list(quality_assess_dict.values()))
    print(table)


if __name__ == '__main__':
    main()