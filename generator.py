import argparse
import json
import sys
import random
import numpy
import re
from collections import defaultdict


def main_generator(count, length):
    """
    Функция, которая на вход получает первое слово, если оно есть,
    и длину последовательности, на основе этого генерирует
    последовательность следующим образом
    берет слово, смотрит на все возможные последующие
    и выбирает с помощью вероятности каждого из них

    count: Первое слово
    length: длина генерируемого текста
    possibility: вероятность слова идти после данного
    dictn: словарь, в котором все хранится
    mas: массив в котором хранятся слова, идущие после данного
    """
    dictn = json.load(input)
    if count is None:
        count = random.choice(list(dictn.keys()))
    for index in range(length):
        output.write(count + ' ')
        possibility = []
        for i in (list(dictn[count].keys())):
            possibility.append(dictn[count][i])
        tmp_sum = sum(possibility)
        for i in range(len(possibility)):
            possibility[i] = possibility[i]/tmp_sum
        count = numpy.random.choice(list(dictn[count].keys()), p=possibility)
    output.write('\n')


if(__name__ == "__main__"):
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str,
                        help="place where analise is written")
    parser.add_argument('--seed', type=str, default=None, help='first_word')
    parser.add_argument('--length', type=int,
                        help='how many words should be generated')
    parser.add_argument('--output', type=str, default=None, help='output file')
    args = parser.parse_args()
    input = open(args.model, "r")
    output = sys.stdout
    if(args.output is not None):
        output = open(args.output, "w")
    main_generator(args.seed, args.length)
    input.close()
    output.close()
