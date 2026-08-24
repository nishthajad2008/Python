class VectorND:

  def __init__(self, components):
    self.components = list(components)

  def __repr__(self):
    return f"VectorND({self.components})"

  @classmethod
  def zeros(cls, dimension):
     return cls([0]*dimension)
  def __add__(self,other):
      if len(self.components) != len(other.components):
          raise ValueError ('Vectors must have the same dimension')
      new_components = [a + b for a, b in zip(self.components, other.components)]
      return VectorND(new_components)
  def dot(self,other):
      if len(self.components) != len(other.components):
          raise ValueError ('Vectors must have the same length')
      return sum([a*b for a, b in zip(self.components, other.components)])

# --- Test Code ---
v1 = VectorND([1, 2, 3])
print(v1)

v_zero = VectorND.zeros(4)
print(v_zero)