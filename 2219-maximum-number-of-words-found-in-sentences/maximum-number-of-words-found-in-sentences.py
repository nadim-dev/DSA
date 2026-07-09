class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words=1
        for i in sentences:
            max_words=max(len(i.split(" ")),max_words)
        return max_words
