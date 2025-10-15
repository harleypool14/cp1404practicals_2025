"""
Word Occurrences
Estimate: 30 minutes
Actual:  16  minutes
"""

word_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    frequency = word_count.get(word, 0)
    word_count[word] = frequency + 1

max_length = max((len(word) for word in words))
for word in sorted(word_count):
    print(f"{word:{max_length}} : {word_count[word]}")
