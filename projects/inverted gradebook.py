def invert_gradebook(scores: dict):
    gradebook = {}
    for i, grade in scores.items():
        if grade not in gradebook:
            gradebook[grade] = [i]
        else:
            gradebook[grade].append(i)
    return gradebook
if __name__ == "__main__":
    data = {"Alice": "A", "Bob": "B", "Charlie": "A", "David": "C", "Eve": "B"}
    print(invert_gradebook(data))


