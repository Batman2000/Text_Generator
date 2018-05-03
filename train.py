import json
import argparse
import sys
import re
from collections import defaultdict


def writinig_text_into_file(is_lower):
    """
    Функция, записывающая весь текст в виде словаря из словарей в нужный файл,
     при этом приводя к нижнему регистру при необходимости

    is_lower: флажок, показывающий нужно ли приводить к lowercase
    """
    dictionary_with_model_of_my_text = defaultdict(
        lambda: defaultdict(int))
    last_word_of_last_line = ""
    for line in input:
        if is_lower is True:
            line = line.lower()
        words = [last_word_of_last_line]
        words += re.findall(r"\w+", line)
        for i in range(len(words) - 1):
            first_word = words[i]
            second_word = words[i+1]
            dictionary_with_model_of_my_text[first_word][second_word] += 1
        last_word_of_last_line = words[-1]
    json.dump(dictionary_with_model_of_my_text, output)


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
    input = sys.stdin
    if args.i is not None:
        input = open(args.i, "r")
    output = open(args.model, "w")
    is_lower = False
    if args.lc is not False:
        is_lower = True
    writinig_text_into_file(is_lower)
    input.close()
    output.close()
