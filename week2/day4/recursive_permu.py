import unittest




import unittest


def get_permutations(string):
    # Base case
    if len(string) <= 1:
        return set([string])

    all_chars_except_last = string[:-1]
    # print("all_chars_except_last",all_chars_except_last)
    last_char = string[-1]
    # print("last_char",last_char)
    # Recursive call: get all possible permutations for all chars except last
    permutations_of_all_chars_except_last = get_permutations(all_chars_except_last)
    print(" permutations_of_all_chars_except_last", permutations_of_all_chars_except_last)
    
    permutations = set()
    for permutation_of_all_chars_except_last in permutations_of_all_chars_except_last:
        # print("in for1",permutation_of_all_chars_except_last)
        for position in range(len(all_chars_except_last) + 1):
            # print("in for",position)
            # print(" permutation_of_all_chars_except_last[:position],last_char,permutation_of_all_chars_except_last[position:]", permutation_of_all_chars_except_last[:position], last_char,permutation_of_all_chars_except_last[position:])
            permutation = (permutation_of_all_chars_except_last[:position]
                + last_char
                + permutation_of_all_chars_except_last[position:]
            )
            # print("permutations",permutation)
            permutations.add(permutation)
        # print("-------------------------------------")
        # print(permutations)
    return permutations


















# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('cat')
        expected = set(['cat','cta','atc','act','tac','tca'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)



















# Tests

class Test(unittest.TestCase):

    # def test_empty_string(self):
    #     actual = get_permutations('')
    #     expected = set([''])
    #     self.assertEqual(actual, expected)

    # def test_one_character_string(self):
    #     actual = get_permutations('a')
    #     expected = set(['a'])
    #     self.assertEqual(actual, expected)

    # def test_two_character_string(self):
    #     actual = get_permutations('ab')
    #     expected = set(['ab', 'ba'])
    #     self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)
    
    
    # def test_empty_string(self):
    #     actual = get_permutations('abcd')
    #     expected = set(['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb',
    #              'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca',
    #              'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba',
    #              'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba'])
    #     self.assertEqual(actual, expected)



unittest.main(verbosity=2)