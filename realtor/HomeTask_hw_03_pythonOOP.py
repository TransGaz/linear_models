class House:
    """ Класс содержащий информацию о домах"""

    default_discount = 0

    def __init__(self, price: float, area: float):
        """ Инициализация обьекта дом с заданной площадью и ценой"""
        self._price = price
        self._area = area

    def final_price(self, discount: int | float = 0) -> int | float:
        """Рассчитывает цену дома с учетом информации о дисконте."""
        final_price = self._price * (100 - discount) * 0.01
        return final_price


class SmallHouse(House):
    """Дочерний класс Дома: предназначен для работы с домами площадью 42 кв.м."""

    def __init__(self, price: float, area: float = 42.0):
        super().__init__(price, area)


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
        """Справочный метод: выводит информацию о клиенте."""
        print(self.__str__())

    def __str__(self):
        return f'Клиент: {self.name}, Возраст: {self.age}, Доступные средства: {self.__account.amount} руб.'

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

        price = house.final_price()

        if price > self.__account.amount:
            print('Внимание! У клиента недостаточно средств.')
        else:
            self.__make_deal(house=house, price=price)
            print('Сделка проведена успешно!')


class Account:
    """Класс Account хранящий информацию о cчетах  клиентов"""
    default_amount = 0

    def __init__(self, client: Client, amount: float = default_amount):
        """ Метод инициализирующий счет клиента и передает информацию об нем"""
        self.client = client
        self.amount = amount

    def __str__(self):
        return f'{self.client}'

    def __iadd__(self, other):
        self.amount += other
        return self.amount

    def __isub__(self, other):
        if other > self.amount:
            print('Недостаточно средств. Сумма не может уходить в минус!')
        else:
            self.amount -= other


class Bank:
    """ Класс Bank хранящий информацию о банковских реквизитах  клиентов"""

    def __init__(self):
        """Инициализирует хранение счетов в пустом списке."""
        self.__accounts = []

    def add_account(self, client: Client):
        """Метод добавляющий нового клиента в банк."""
        if client.name not in [acnt.client.name for acnt in self.__accounts]:
            client_account = Account(client=client)
            self.__accounts.append(client_account)
            print(f'Для клиента {client.name} был создан банковский счет!')
            return client_account
        else:
            raise ValueError(f' У клиента {client.name} имеется банковсий счет!')

    def __str__(self):
        banks_accnts = [accnt.client.name for accnt in self.__accounts]
        return 'Клиенты банка: ' + str(banks_accnts)
    
