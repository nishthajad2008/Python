class BoundedQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = []
    def enqueue(self, item):
        if len(self.items) == self.capacity:
            print("Queue is full!")
        else:
            self.items.append(item)
            return True
    def dequeue(self,):
        if len(self.items) == 0:
            print("Queue is empty!")
        else:
            removed_item = self.items.pop(0)
            return removed_item
if __name__ == "__main__":
    q = BoundedQueue(2)  # Queue can hold max 2 items

    q.enqueue("Apple")
    q.enqueue("Banana")
    q.enqueue("Cherry")  # Should print: "Queue is full!"

    print(q.dequeue())  # Expected: "Apple" (first one in!)
    print(q.dequeue())  # Expected: "Banana"
    print(q.dequeue())  # Should print: "Queue is empty!"

