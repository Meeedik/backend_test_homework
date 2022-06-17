class Contact:
    name: str
    year_birth: int
    is_programmer: bool

    def __init__(self,
                 name: str = 'hi',
                 year_birth: int = 10,
                 is_programmer: bool = True) -> None:
        self.name = name
        self.year_birth = year_birth
        self.is_programmer = is_programmer

    def age_define(self):
        if 1946 < self.year_birth < 1980:
            return 'Олдскул'
        if self.year_birth >= 1980:
            return 'Молодой'
        return 'Старейшина'

    def programmer_define(self):
        if self.is_programmer:
            return 'Программист'
        return 'Нормальный'

    def show_contact(self):
        return (f'{self.name}, '
                f'категория: {self.age_define()}, '
                f'статус: {self.programmer_define()}')

    def print_contact(self):
        print(self.show_contact())


print(Contact.__annotations__)
