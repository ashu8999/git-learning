class twodvector:

    def __init__(self, i ,j):
        self.i = i
        self.j = j

        # return f"{i},{j}"

    def show(self):
        print (f"Value of vector{self.i}i, {self.j}j")
    
class threedvector(twodvector):

    def __init__(self, i ,j,k):
        super().__init__(i,j)
        self.k = k

        # return f"{i},{j},{k}"
    def show(self):
        print (f"Value of vector{self.i}i, {self.j}j, {self.k}k")
    

a = twodvector(1, 2)
b = threedvector(1,2,5)

a.show()
b.show()
       
