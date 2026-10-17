
class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if len(s) < total_len:
            return []

        target = {}
        for word in words:
            target[word] = target.get(word, 0) + 1

        result = []

        for offset in range(word_len):
            left = offset
            right = offset
            seen = {}
            count = 0

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word not in target:
                    seen.clear()
                    count = 0
                    left = right
                    continue

                seen[word] = seen.get(word, 0) + 1
                count += 1

                while seen[word] > target[word]:
                    left_word = s[left:left + word_len]
                    seen[left_word] -= 1
                    count -= 1
                    left += word_len

                if count == word_count:
                    result.append(left)

                    left_word = s[left:left + word_len]
                    seen[left_word] -= 1
                    count -= 1
                    left += word_len

        return sorted(result)