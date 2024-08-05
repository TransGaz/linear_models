class House:
    @classmethod
    def final_price(cls):
        pass


class Client:
    """"
    Класс Client,  хранящий информацию о клиенте
    """

    default_name = 'John Doe'
    default_age = 99

    def __init__(self, bank, name: str = default_name, age: int = default_age):
        """ Метод инициализирующий клиента и передает информацию об нем"""
        self.name = name
        self.age = age
        self.__account = bank.add_account(client=self)
        self.__house = None

    def info(self):
        """ Метод предоставляющий базовую информацию о клиенте"""
        return f" Клиент- имя: {self.name}, возраст: {self.age}, дом: {self.__house}, счет: {self.__account}"

    def __str__(self):
        return self.info()

    @staticmethod
    def default_info(default_name=default_name, default_age=default_age):
        """ Метод который выводит информацию по умолчанию о клиенте"""
        print(f"{default_name}, {default_age}")

    def __make_deal(self, house: House, price: float):
        """ Метод, который отвечает за техническую реализацию покупки дома:
            Уменьшает количество денег на счету и присваивает ссылку на только что купленный дом
        """
        self.__house = house
        self.__account.amount -= price

    def earn_money(self, amount: float) -> None:
        """ Метод увеличивающий сумму денег на счету клиента."""
        self.__account.amount += amount
        print(f'Клиент {self.name} пополнил свой счет на {amount}. Общий баланс счета {self.__account.amount}')

    def buy_house(self, house: House) -> None:
        """ Метод который будет проверять, что у человека достаточно денег для покупки, и совершать сделку."""

        price = House.final_price()
        if price > self.__account.amount:
            print('Внимание! У клиента недостаточно средств.')
        else:
            self.__make_deal(house=house, price=price)
            print('Сделка проведена успешно!')










