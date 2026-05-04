from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        n = len(s)

        word_map = Counter(words)
        result = []

        # Try all starting offsets
        for i in range(word_len):
            left = i
            curr_count = {}
            count = 0

            for j in range(i, n - word_len + 1, word_len):
                word = s[j:j + word_len]

                if word in word_map:
                    curr_count[word] = curr_count.get(word, 0) + 1
                    count += 1

                    # If too many of a word → shrink window
                    while curr_count[word] > word_map[word]:
                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        count -= 1
                        left += word_len

                    # If valid window found
                    if count == word_count:
                        result.append(left)

                else:
                    # Reset window
                    curr_count.clear()
                    count = 0
                    left = j + word_len

        return result