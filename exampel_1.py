class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float
                 ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories
    def get_message(self):
        return (f'Тип тренировки: {self[0]}; '
                f'Длительность: {self[1]:.3f} ч.; '
                f'Дистанция: {self[2]:.3f} км; '
                f'Ср. скорость: {self[3]:.3f} км/ч; '
                f'Потрачено ккал: {self[4]:.3f}.')
class Training:
    """Базовый класс тренировки."""
    LEN_STEP = 0.65
    M_IN_KM = 1000
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM
    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration
    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass
    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage.get_message((self.__class__.__name__,
                                        self.duration,
                                        self.get_distance(),
                                        self.get_mean_speed(),
                                        self.get_spent_calories()))
class Running(Training):
    """Тренировка: бег."""
    coeff_calorie_1 = 18
    coeff_calorie_2 = 20
    MIN_IN_HOURS = 60
    def __init__(self, action, duration, weight):
        super().__init__(action, duration, weight)
    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return ((self.coeff_calorie_1 * self.get_mean_speed()
                - self.coeff_calorie_2)
                * self.weight / self.M_IN_KM
                * (self.duration * self.MIN_IN_HOURS))


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    coeff_calorie_3 = 0.035
    coeff_calorie_4 = 0.029
    MIN_IN_HOURS = 60
    def __init__(self, action, duration, weight, height: int):
        super().__init__(action, duration, weight)
        self.height = height
        
    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return ((self.coeff_calorie_3 * self.weight
                + (self.get_mean_speed() ** 2 // self.height)
                * self.coeff_calorie_4 * self.weight) * self.duration
                * self.MIN_IN_HOURS)


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP = 1.38
    coeff_calorie_5 = 1.1
    coeff_calorie_6 = 2.0
    def __init__(self, action, duration, weight,
                 length_pool: int, count_pool: int):
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool
    def get_mean_speed(self) -> float:
        """Получить среднюю скорость плавания."""
        return (self.length_pool * self.count_pool
                / self.M_IN_KM / self.duration)
    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return ((self.get_mean_speed() + self.coeff_calorie_5)
                * self.coeff_calorie_6 * self.weight)


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    type_of_training = {'SWM': Swimming,
                        'RUN': Running,
                        'WLK': SportsWalking}
    return type_of_training[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info)
if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]
    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)