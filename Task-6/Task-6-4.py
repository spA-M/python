class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Текущая скорость автомобиля {self.name} равна {self.speed} км/час'



class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} равна {self.speed} км/час')

        if self.speed > 60:
            return f"Автомобиль {self.name} превышает скорость ограниченную 60 км/час"

        else:
            return f"Автомобиль {self.name} движется в пределах скоростных ограничений"



class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} равна {self.speed} км/час')

        if self.speed > 40:
            return f"Автомобиль {self.name} превышает скорость ограниченную 40 км/час"

        else:
            return f"Автомобиль {self.name} движется в пределах скоростных ограничений"

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'Машина {self.name} является полицейской машиной'
        else:
            return f'Машина {self.name} не является полицейской машиной'

bmw = SportCar(300, 'Черный', 'BMW', False)
reno = TownCar(50, 'Серебристый', 'RENO', False)
ford = WorkCar(70, 'Коричневый', 'Ford', True)
toyota = PoliceCar(150, 'Синяя',  'Toyota', True)
print(ford.turn_left())
print(f'Когда {toyota.turn_right()}, за ней {bmw.stop()}')
print(f'{ford.go()} и {ford.show_speed()}')
print(f'Является ли {toyota.name} полицейской машиной? {toyota.is_police}')
print(bmw.show_speed())
print(reno.show_speed())
print(toyota.police())
print(ford.show_speed())