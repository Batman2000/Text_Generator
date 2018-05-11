import argparse
import json
import sys
import random
import numpy
import re
from collections import defaultdict


def loading_model_from_file():
    dictionary_with_model_of_my_text = json.load(input)
    return dictionary_with_model_of_my_text


def generating_text(dictionary_with_model_of_my_text, first_word, length,
                    max_symbols_of_one_paragraph=300):
    """
    Функция, которая на вход получает первое слово, если оно есть,
    и длину последовательности, на основе этого генерирует
    последовательность следующим образом
    берет слово, смотрит на все возможные последующие
    и выбирает с помощью вероятности каждого из них

    first_word: Первое слово
    length: длина генерируемого текста
    max_symbols_of_one_paragraph: максимальное количество символов
    в одном абзаце
    dictionary_with_model_of_my_text: словарь с моделью данного текста
    """
    text = ''
    if first_word is None:
        first_word = random.choice(
            list(dictionary_with_model_of_my_text.keys()))
    for index in range(length):
        text += first_word + ' '
        possibility = list(
            dictionary_with_model_of_my_text[first_word].values())
        possibility_sum = sum(possibility)
        for i in range(len(possibility)):
            possibility[i] = possibility[i]/possibility_sum
        first_word = numpy.random.choice(
            list(dictionary_with_model_of_my_text[first_word].keys()),
            p=possibility)
        if len(text) >= max_symbols_of_one_paragraph:
            output.write(text + '\n')
            text = ''
        """
        Переменная text содержит в себе абзац, который был сгенерирован
        на данный момент.
        В случае, если количество символов превысит максимально допустимое
        (max_symbols_of_one_paragraph), мы выводим наш абзац,
        обнуляем text и начинаем генерацию нового, в случае необходимости
        """
    output.write(text + '\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str,
                        help="place where analise is written",
                        required=True)
    parser.add_argument('--seed', type=str, default=None, help='first_word')
    parser.add_argument('--length', type=int,
                        help='how many words should be generated',
                        required=True)
    parser.add_argument('--output', type=str, default=None, help='output file')
    parser.add_argument("--max-symbols", type=int,
                        help="maximum number of symbols in one paragraph",
                        default=300
                        )

    args = parser.parse_args()

    input = open(args.model, "r")

    if args.output is not None:
        output = open(args.output, "w")
    else:
        output = sys.stdout
    dictionary_with_model_of_my_text = loading_model_from_file()
    generating_text(dictionary_with_model_of_my_text, args.seed, args.length,
                    args.max_asymbols)
    input.close()
    output.close()
