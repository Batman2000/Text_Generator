from src import train

def test_normalize_empty():
    empty_dict = {}
    train.possibilities_normalization(empty_dict)
