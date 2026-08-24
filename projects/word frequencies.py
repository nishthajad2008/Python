def top_three_words(text: str):
    words = text.split()
    counts = {}

    # 1. Count frequencies
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    # 2. Convert dictionary to list of tuples: [('cat', 4), ('dog', 3), ...]
    items_list = list(counts.items())

    # 3. Sort by count (x[1]) from highest to lowest (reverse=True)
    sorted_items = sorted(items_list, key=lambda x: x[1], reverse=True)

    # 4. Return the top 3
    return sorted_items[:3]


# --- Test ---
print(top_three_words("cat dog cat mouse cat dog bird dog cat"))
# Output: [('cat', 4), ('dog', 3), ('bird', 1)] (or 'mouse')