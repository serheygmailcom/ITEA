
print("""

##################
TASK WITH CARS
##################
""")


class Cars:
    def __init__(self, model, horse_power):
        self._model=model
        self._horse_power=horse_power

    def signal(self):
        print("Beep")

    def __str__(self):
        return f"self.*arg"

class Light(Cars):
    def __init__(self, model, horse_power, acceleration_to_100kmph):
        self._acceleration = acceleration_to_100kmph
        super().__init__(model, horse_power)

class Heavy(Cars):
    def __init__(self, model, horse_power, cargo_capacity):
        self._cargo_capacity = cargo_capacity
        super().__init__(model, horse_power)

    def signal(self):
        print("BEEEP!")

l_car1=Light("Lanos",100, 12)
h_car1=Heavy("Kamaz", 1000, 10000)


print(l_car1._acceleration)
print(vars(h_car1))

l_car1.signal()
h_car1.signal()

print("""

##################
TASK WITH SHOPS
##################
""")


class Shop:
    def __init__(self, name):
        self._name=name
        self._goods_sold=0

#'', 0, [], None

    def set_sold(self, x):
        self._goods_sold += x

    def get_sold(self, x):
        return self._goods_sold

    def __str__(self):
        return f'Number of sold items by {self._name} is: {self._goods_sold}'

    def __add__(self, other):
         total = self._goods_sold + other._goods_sold
         return f'Total number of goods sold by all shops is: {total}'


novus=Shop('NOVUS')
silpo=Shop('SILPO')

silpo.set_sold(500)
silpo.set_sold(200)
novus.set_sold(10000)

print(novus)
print(silpo)
print(novus + silpo)


print("""

##################
TASK WITH DOTS
##################
""")

class Dot():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return self.x + other.x, self.y + other.y, self.z + other.z
    def __sub__(self, other):
        return self.x - other.x, self.y - other.y, self.z - other.z
    def __mul__(self, other):
        return self.x * other.x, self.y * other.y, self.z * other.z
    def __div__(self, other):
        return self.x / other.x, self.y / other.y, self.z / other.z


    def __eq__(self, other):
        return f'''x coordinates are equals: {self.x == other.x}
y coordinates are equals:  {self.y == other.y}
z coordinates are equals: {self.z == other.z}
'''


    def get_x_coord(self):
        return self.x

    def get_y_coord(self):
        return self.y

    def get_z_coord(self):
        return self.z


    def set_x_coord(self, val):
        self.x = val

    def set_y_coord(self, val):
        self.y = val

    def set_z_coord(self, val):
        self.z=val


d1=Dot(7,2,3)
d2=Dot(7,8,9)

print(d1 == d2)

d2.set_z_coord(1000)
print(d2.get_z_coord())

print(d1*d2)