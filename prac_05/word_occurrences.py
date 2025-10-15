"""
Word Occurrences
Estimate: 30 minutes
Actual:    minutes
"""

word_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    frequency = word_count.get(word, 0)
    word_count[word] = frequency + 1

for word in sorted(word_count):
    print(f"{word:} : {word_count[word]}")
