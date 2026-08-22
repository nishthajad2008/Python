def word_count(text: str):
    words = text.split()
    counts = {}
    for i in words:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    print(counts)
word_count("apple banana apple strawberry banana apple")

