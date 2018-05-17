import json
import argparse
import sys
import re
from collections import defaultdict


def writinig_model_of_text_into_file(is_lower):
    """
    Функция, записывающая модель текста в виде словаря из словарей в
    нужный файл,
    при этом приводя к нижнему регистру при необходимости

    is_lower: флажок, показывающий нужно ли приводить к lowercase
    """
    dict_with_model_of_my_text = defaultdict(
        lambda: defaultdict(int))
    last_word_of_last_line = ""
    for line in input:
        if is_lower is True:
            line = line.lower()
        words = [last_word_of_last_line]
        words += re.findall(r"\w+", line)
        for i in range(len(words) - 1):
            dict_with_model_of_my_text[words[i]][words[i+1]] += 1
        last_word_of_last_line = words[-1]
    for word in list(dict_with_model_of_my_text.keys()):
        words_occurrence_sum = sum(list(
            dict_with_model_of_my_text[word].values()))
        for next_word in dict_with_model_of_my_text[word].keys():
            dict_with_model_of_my_text[word][next_word] /= words_occurrence_sum
    json.dump(dict_with_model_of_my_text, output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str,
                        help="place where analise is written",
                        required=True)
    parser.add_argument('--i', '--input-dir', type=str,
                        default=None,
                        help="source of data")
    parser.add_argument('--lc', action='store_true',
                        default=False,
                        help='going to lowercase')
    args = parser.parse_args()
    input = sys.stdin if args.i is None else open(args.i, "r")
    output = open(args.model, "w")
    is_lower = args.lc
    writinig_model_of_text_into_file(is_lower)
    input.close()
    output.close()
