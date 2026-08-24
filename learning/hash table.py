class ResizableHashTable:

  def __init__(self, initial_size=4):
    self.size = initial_size
    self.count = 0
    self.buckets = [[] for _ in range(self.size)]

  def _hash(self, key: str) -> int:
    hash_value = 0
    for char in key:
      hash_value = (hash_value * 31 + ord(char)) % self.size
    return hash_value

  def put(self, key: str, value):
      # Step 1: Resize if table is getting crowded (> 75% full)
      if self.count / self.size > 0.75:
          self._resize()

      # Step 2: Calculate target bucket index
      index = self._hash(key)
      bucket = self.buckets[index]

      # Step 3: Check if key exists -> Update value
      for i, (k, v) in enumerate(bucket):
          if k == key:
              bucket[i] = (key, value)
              return  # Stop here! Count doesn't change on update.

      # Step 4: Key wasn't found -> Add new pair & increment count
      bucket.append((key, value))
      self.count += 1

  def _resize(self):
      old_buckets = self.buckets
      self.size *=2
      self.buckets = [[] for _ in range(self.size)]
      self.count = 0
      for bucket in old_buckets:
          for key, value in bucket:
              self.put(key, value)
# --- Simple Test ---
ht = ResizableHashTable(initial_size=2)
print("Initial size:", ht.size)  # Should be 2

# Manually populate old buckets to test your _resize logic
ht.buckets = [[("cat", "feline")], [("dog", "canine")]]
ht.count = 2

ht._resize()

print("New size:", ht.size)  # Should be 4
print("New buckets structure:", ht.buckets)