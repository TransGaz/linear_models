from HomeTask_hw_03_pythonOOP import *

if __name__ == "__main__":
    #Создайте два банка: green_bank и red_bank
    green_bank = Bank()
    red_bank = Bank()

    #Вызовите справочный метод default_info() для класса Client()
    Client.default_info()

    #Создайте объект student класса Client и определите его как клиента банка green_bank
    student = Client(name='Шурик ', age=18, bank=green_bank)

    #Создайте объект teacher класса Client и определите его как клиента банка red_bank
    teacher = Client(name='Иванов Иван Иванович', age=39, bank=red_bank)

    #Создайте объект класса SmallHouse
    sm_house = SmallHouse(11005.0)

    #Выведите справочную информацию о созданном объекте student
    student.info()

    #Выведите справочную информацию о созданном объекте teacher
    print(teacher)

    #Попробуйте для объекта student купить созданный дом, убедитесь в получении предупреждения
    student.buy_house(sm_house)
    #
    # Поправьте финансовое положение объекта student - вызовите метод earn_money()
    # Снова попробуйте купить дом

    # student голоден и раздает рекламку
    student.earn_money(100)
    student.buy_house(sm_house)

    # student учит питон потом пишет краулер и подрабатывает в маке
    student.earn_money(500)
    student.buy_house(sm_house)

    # student учит ML и подрабатывает аналитиком
    student.earn_money(1500)
    student.buy_house(sm_house)

    # student учит ООП и доучивает МЛ, подрабатывает, иногда ходит на пары

    student.earn_money(2500)
    student.buy_house(sm_house)

    # student доучивает все что недоучил, пишет курсач и подрабатывает в мега-супер-пупер стартапе , берет кредит
    student.earn_money(6406)
    student.buy_house(sm_house)

    #Посмотрите, как изменилось состояние объекта student
    print(student)

    # student чуть поседел от ,бурных перемен,сдал курсач, знает питон, ООП, МЛ, счастлив но опять голоден.
