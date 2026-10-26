# https://codeforces.com/problemset/problem/1685/B
from typing import List

dict_words_priority = {
    'AB': 0,
    'BA': 1,
    'A': 2,
    'B': 3
}


def key_word(word):
    return dict_words_priority[word]


class Solution:
    dict_words = {0: 'A', 1: 'B', 2: 'AB', 3: 'BA'}

    def convert_integers_to_vocabulary(self, integers: List[int], start: int,
                                       end: int) -> List[str]:
        vocabulary = []
        for ind in range(start, end):
            while integers[ind] > 0:
                vocabulary.append(self.dict_words[ind])
                integers[ind] = integers[ind] - 1

        return vocabulary

    def convert_sentence_to_list(self, s: str) -> List[str]:
        list_word = []
        ind = 0
        while ind < (n := len(s) - 1):
            if (n - ind) >= 1 and s[ind:ind + 2] == self.dict_words[3]:
                list_word.append(self.dict_words[3])
                ind = ind + 2
            elif (n - ind) >= 1 and s[ind:ind + 2] == self.dict_words[2]:
                list_word.append(self.dict_words[2])
                ind = ind + 2
            elif s[ind:ind + 1] == self.dict_words[1]:
                list_word.append(self.dict_words[1])
                ind = ind + 1
            elif s[ind:ind + 1] == self.dict_words[0]:
                list_word.append(self.dict_words[0])
                ind = ind + 1
        return list_word

    def convert_sentence_to_list_single(self, s: str) -> List[str]:
        list_word = []
        ind = 0
        n = len(s)
        while ind < n:
            if s[ind:ind + 1] == self.dict_words[1]:
                list_word.append(self.dict_words[1])
                ind = ind + 1
            elif s[ind:ind + 1] == self.dict_words[0]:
                list_word.append(self.dict_words[0])
                ind = ind + 1
        return list_word

    def remove_matching_from_vocabulary(self, vocabulary: List[str],
                                        list_word: List[str], match_len: int):
        ind = 0
        n = len(list_word)
        while ind < n and len(list_word[ind]) == match_len:
            if list_word[ind] in vocabulary:
                vocabulary.remove(list_word[ind])
                list_word.remove(list_word[ind])

            ind = ind + 1

    def solution(self, integers: List[int], sentence: str):
        vocabulary_double = self.convert_integers_to_vocabulary(integers, 2, 4)
        list_word = self.convert_sentence_to_list(sentence)

        list_word.sort(key=key_word)

        self.remove_matching_from_vocabulary(vocabulary_double, list_word, 2)

        vocabulary_single = self.convert_integers_to_vocabulary(integers, 0, 2)

        list_word = self.convert_sentence_to_list_single("".join(list_word))

        self.remove_matching_from_vocabulary(vocabulary_single, list_word, 1)

        print(vocabulary_single)
        print(list_word)



if __name__ == "__main__":
    integers = [2, 2, 3, 1]
    sentence = 'BAABBABBAA'

    solution = Solution()

    print(solution.solution(integers, sentence))
