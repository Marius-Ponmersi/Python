class Road:
    __length = 5000
    __width = 20

    def square(self, __length, __width):
        self.__length = __length
        self.__width = __width
        depth = 1    # толщина асфальта в см
        m = 25     # масса асфальта для покрытия 1 кв.м. в кг
        massa = __length * __width * depth * m / 1000
        return massa

r = Road()
print(f"Масса асфальта для покрытия дороги равна {r.square(r._Road__length, r._Road__width)} тонн")
print(f"Масса асфальта для покрытия дороги равна {r.square(4000, 20)} тонн")
