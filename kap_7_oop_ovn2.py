import math

# 2.1 Figurer
# I boken beskrivs klasser för flera olika geometriska figurer. För att koppla ihop
# hela avsnittet kring OOP utfå från dessa och skapa dig en figurmodul som innehåller
# alla dessa utifrån den basklass som finns på sidan 200 i boken. Modifiera subklasserna
# när det är nödvändigt. Skapa även en ny subklass Rektangel som har sin startpunkt i
# övre vänstra hörnet och har en höjd och en bredd och metoder motsvarande dem i klassen
# Cirkel. Se till så att alla figurer har fungerande utskrifts och kopieringsmetoder.

# Skapa ett testprogram där du skapar olika figurer och sedan använder de olika
# metoderna för att förändra, kopiera och skriva ut på olika sett. Placera lämpligen
# figurerna i en lista för att sedan enkelt kunna behandla alla i en följd.


# 2.2 Area & omkrets.
# Lägg till metoder för att beräkna arean och omkretsen på cirkeln och rektangeln. Uppdatera vid behov utskrifts och kopieringsmetoderna. Formler för beräkning:
# Cirkel: Omkrets 2*pi*r, Arean pi*r^2.
# Rektangel: Omkrets 2*(l+b), Arean l*b.

# Uppdatera även testprogrammet så att du testar de nya metoderna.
# Tänk på att importera pi från modulen math.


class Base:
    def __init__(self, name="noname"):
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def copy_from(self, o):
        self.__name = o.name

    def __str__(self):
        return f"{self.__name} - Base()"

    name = property(get_name, set_name)


class Line(Base):
    def __init__(self, name="noname"):
        super().__init__(name)
        self.__p0 = Point()
        self.__p1 = Point()

    def get_p0(self):
        return self.__p0

    def get_p1(self):
        return self.__p1

    def set_p0(self, p0):
        self.__p0 = p0

    def set_p1(self, p1):
        self.__p1 = p1

    def copy_from(self, l):
        super().copy_from(l)
        self.__p0.copy_from(l.p0)
        self.__p1.copy_from(l.p1)

    def length(self):
        return math.sqrt(
            math.pow(self.p1.x - self.p0.x, 2) + math.pow(self.p1.y - self.p0.y, 2)
        )

    def __str__(self):
        return_string = (
            f"{self.name} - Line from: \n\t"
            f"{self.p0}\n"
            f"\t To: \n\t"
            f"{self.p1}\n"
            f"\t Length: \n\t\t"
            f"{self.length()}"
        )
        return return_string

    p0 = property(get_p0, set_p0)
    p1 = property(get_p1, set_p1)


class Point(Base):
    def __init__(self, x=0.0, y=0.0, name="noname"):
        super().__init__(name)
        self.__x = x
        self.__y = y

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def set(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def copy_from(self, p):
        super().copy_from(p)
        self.__x = p.x
        self.__y = p.y

    def __str__(self):
        if self.name == "noname":
            return f"\tPoint({self.__x}), {self.__y}"
        else:
            return f"{self.name} - Point( {self.__x}, {self.__y})"

    x = property(get_x, set_x)
    y = property(get_y, set_y)


class Circle(Point):
    def __init__(self, x=0.0, y=0.0, r=1.0, name="noname"):
        super().__init__(x, y, name)
        self.__r = r

    def set_r(self, r):
        self.__r = r

    def get_r(self):
        return self.__r

    def copy_from(self, c):
        super().copy_from(c)
        self.r = c.r

    def area(self):
        return math.pi * math.pow(self.r, 2)

    def circumference(self):
        return 2 * math.pi * self.r

    def __str__(self):
        return_string = (
            f"{self.name} - Circle({self.x}, {self.y}, {self.r})"
            f"\n\t\tArean är {self.area()}"
            f"\n\t\tOmkretsen är {self.circumference()}"
        )
        return return_string

    r = property(get_r, set_r)


class Rektangel(Point):
    def __init__(self, x=0.0, y=0.0, h=0.0, b=0.0, name="noname"):
        super().__init__(x, y, name)
        self.__h = h
        self.__b = b

    def set_h(self, h):
        self.__h = h

    def set_b(self, b):
        self.__b = b

    def get_h(self):
        return self.__h

    def get_b(self):
        return self.__b

    def copy_from(self, r):
        super().copy_from(r)
        self.__h = r.h
        self.__b = r.b

    def area(self):
        return self.h * self.b

    def circumference(self):
        return 2 * self.h + 2 * self.b

    def __str__(self):
        return_string = (
            f"{self.name} - Rektangel({self.x}, {self.y}, {self.h}, {self.b})"
            f"\n\t\tArean är {self.area()}"
            f"\n\t\tOmkretsen är {self.circumference()}"
        )

        return return_string

    h = property(get_h, set_h)
    b = property(get_b, set_b)


shapes = []

shapes.append(Point(0.0, 1.0, "p0"))
shapes.append(Point(4.0, 4.0, "p1"))
shapes.append(Circle(2.0, 1.0, 3.0, "c0"))
shapes.append(Rektangel(2.0, 1.0, 3.0, 4.5, "r0"))
shapes.append(Line("l0"))
shapes.append(Line("l1"))
shapes[4].set_p0(shapes[0])
shapes[4].set_p1(shapes[1])
r1 = Rektangel()
r1.copy_from(shapes[3])
r1.name = "r1"
shapes.append(r1)

for shape in shapes:
    print(shape)
