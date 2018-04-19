import json
import argparse
import sys
import re
from collections import defaultdict


def main_action(is_lower):
    """
    Функция, записывающая весь текст в виде словаря из словарей

    dictn: Словарь, который мы и запишем в файл
    words: Список слов в данной строке
    is_lower: флажок, показывающий нужно ли приводить к lowercase
    last_word_of_last_line: последнее слово в предыдущей строке
    """
    dictn = defaultdict(lambda: defaultdict(int))
    last_word_of_last_line = ""
    for line in input:
        if is_lower is True:
            line = line.lower()
        words = [last_word_of_last_line]
        words += re.findall(r"\w+", line)
        for i in range(len(words) - 1):
            first_word = words[i]
            second_word = words[i+1]
            dictn[first_word][second_word] += 1
        last_word_of_last_line = words[-1]
    json.dump(dictn, output)


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
    main_action(is_lower)
    input.close()
    output.close()
