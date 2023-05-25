# Напишите программу банкомат.
# ✔Начальная сумма равна нулю
# ✔Допустимые действия: пополнить, снять, выйти
# ✔Сумма пополнения и снятия кратны 50 у.е.
# ✔Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔Нельзя снять больше, чем на счёте
# ✔При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔Любое действие выводит сумму денег

class BankingTerminalAccount:
    __MULTIPLICATOR = 50
    __TAX_FOR_THE_RICH = 0.1
    _FEE = 0.015
    __MIN_FEE = 30
    __MAX_FEE = 600
    _RICHNESS_THRESHOLD = 5_000_000
    _BONUS = 0.03



    def __init__(self):
        self.__balance = 0
        self.log = list()

    def __input_sum(self, for_taking=False):
        i = 1
        while i % self.__MULTIPLICATOR != 0:
            i = int(input(f"Введите сумму, кратную {self.__MULTIPLICATOR}: "))
            if for_taking and i > self.__balance:
                i = 1
                print("На балансе недостаточно средств.")
        return i

    def __operations(self, mode):
        txt = ''
        if self.__balance > self._RICHNESS_THRESHOLD:
            txt += f'Снят налог на богатство в размере {self.__balance * self.__TAX_FOR_THE_RICH}. '
            self.__balance -= self.__balance * self.__TAX_FOR_THE_RICH

        if mode == 'put':
            txt += self.__put_money()
        elif mode == 'take':
            txt += self.__take_money()

        if len(self.log) % 3 == 2:
            txt += f'Бонус {self.__balance * self._BONUS} добавлен. '
            self.__balance += self.__balance * self._BONUS

        self.__balance = round(self.__balance, 2)
        txt += f"Текущий баланс = {self.__balance}"
        self.log.append(txt)
        print(txt, '\n')

    def __put_money(self):
        amount = self.__input_sum()
        self.__balance += amount
        return f"Добавлено {amount}. "

    def __take_money(self):
        amount = self.__input_sum(for_taking=True)
        fee = amount * self._FEE
        if fee < self.__MIN_FEE:
            fee = self.__MIN_FEE
        elif fee > self.__MAX_FEE:
            fee = self.__MAX_FEE
        self.__balance -= amount + fee
        return f"Снято {amount} и еще комиссия {fee}. "

    def menu(self):
        while True:
            print("""Выберите одно из действий:
            1. Пополнить
            2. Снять
            3. Посмотреть лог операций
            4. Выйти""")
            match (input()):
                case '1':
                    self.__operations('put')
                case '2':
                    self.__operations('take')
                case '3':
                    print(*self.log, sep='\n')
                case '4':
                    print("До свидания")
                    return


if __name__ == '__main__':
    bank = BankingTerminalAccount()
    bank.menu()
