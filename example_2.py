class InfoMessage:
    """adsada"""
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories
    def get_message(self):
        return (f'Тип тренировки: {self.training_type},'
                f'Длительность: {self.duration.} ч.;'
                f'Дистанция: {self.distance} км;'
                f'Ср. скорость: {self.speed} км/ч;'
                f'Потрачено ккал: {self.calories}.')
class Training:
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
    LEN_STEP = 0.65
    M_IN_KM = 1000
    def get_distance(self) -> float:
        return self.action * self.LEN_STEP / self.M_IN_KM
    def get_mean_speed(self) -> float:
        return self.get_distance() / self.duration
    def get_spent_calories(self) -> float:
        pass
    def show_training_info(self) -> InfoMessage:
        return InfoMessage(
            training_type=self.__class__.__name__,
            duration=self.duration,
            distance=self.get_distance(),
            speed=self.get_mean_speed(),
            calories=self.get_spent_calories()
            )
class Running(Training):
    def __init__(self,
                action: int,
                duration: float,
                weight: float) -> None:
        super().__init__(action,
                        duration,
                        weight)
    def get_spent_calories(self) -> float:
        coeff_calorie_1 = 18
        coeff_calorie_2 = 20
        return(coeff_calorie_1 * self.get_mean_speed() - coeff_calorie_2) * self.weight / self.M_IN_KM * self.duration
class SportsWalking(Training):
    def __init__(self,
                action: int,
                duration: float,
                weight: float,
                height: float) -> None:
        super().__init__(action,
                        duration,
                        weight)
        self.height = height
    coeff_calorie_3 = 0.035
    coeff_calorie_4 = 0.029
    def get_spent_calories(self) -> float:
        return(self.coeff_calorie_3 * self.weight + (self.get_mean_speed()**2 // self.height)
        * self.coeff_calorie_4 * self.weight) * self.duration
class Swimming(Training):
    def __init__(self,
                action: int,
                duration: float,
                weight: float,
                lenght_pool: float,
                count_pool: int) -> None:
        super().__init__(action,
                        duration,
                        weight)
        self.lenght_pool = lenght_pool
        self.count_pool = count_pool
    LEN_STEP = 1.38
    def get_mean_speed(self) -> float:
        return self.get_distance() * self.count_pool / self.M_IN_KM / self.duration
    def get_spent_calories(self) -> float:
        return (self.get_mean_speed() + 1.1) * 2 * self.weight
def read_package(workout_type: str, data: list) -> Training:
    workout_class_type = {'RUN': Running,
                          'WLK': SportsWalking,
                          'SWM': Swimming }
    data_check = workout_class_type[workout_type](*data)
    return data_check
def main(training: Training) -> None:
    info = training.show_training_info()
    print(info.get_message())
if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]
    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)