class twoDvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"the vector is {self.i}i+{self.j}j")
    def magnitude(self):
        return(self.i**2+self.j**2)**0.5
class Vector3D(twoDvector):   # Inheriting Vector2D
    def __init__(self, i, j, k):
        super().__init__(i, j)   # use parent constructor for x, y
        self.k = k               # add new coordinate

    def show(self):
        print(f"Vector3D = ({self.i}, {self.j}, {self.k})")

    def magnitude(self):
        return (self.i**2 + self.j**2 + self.k**2) ** 0.5

v2 = twoDvector(3,4)
v2.show()
print("2D magnitude:", v2.magnitude())

v3 = Vector3D(1, 2, 3)
v3.show()
print("3D magnitude:", v3.magnitude())
