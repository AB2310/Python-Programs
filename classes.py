class Mca:
    rep1 = 'Sivananth'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def duty(self):
        print('Attendence')
p1 = Mca('Revathi', 21)
p2 = Mca('Gracen', 23)
print(p1.rep1)
p1.duty()
print(p2.name)
print(p2.age)