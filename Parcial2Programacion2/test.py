import funciones2

def test_is_mutant_true():
    adn_list = [
        "AAAAAA",
        "TTTTTT",
        "CCCCCC",
        "GGGGGG",
        "AAAAAA",
        "TTTTTT"
    ]
    assert funciones2.is_mutant(adn_list) == True

def test_is_mutant_false():
    adn_list = [
        "AAAATG",
        "ATCTTT",
        "CTCCCG",
        "GGTGAG",
        "ATAAAA",
        "GAGTTT"
    ]
    assert funciones2.is_mutant(adn_list) == False