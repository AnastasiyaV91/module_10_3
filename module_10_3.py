import threading                          # Импортируем из модуля многопоточности threading
from random import randint                # Модуль случайных целых чисел randint
from time import sleep                    # Модуль для задержки sleep

class Bank:
    def __init__(self):                   # Конструктор класса Bank
        self.balance = 0                      # Баланс счета (изначально нулевой)
        self.lock = threading.Lock()          # Замок блокировки потоков

    def deposit(self):                                                # Функция пополнения счета
        for i in range(100):                                          # Цикл пополнения счета 100 раз
            money_in = randint(50, 500)                         # Получаем случайное число от 50 до 500
            self.balance = self.balance + money_in                    # Пополняем баланс
            print(f"Пополнение: {money_in}. Баланс: {self.balance}")  # Выводим сообщение в консоль
            if self.balance >= 500 and self.lock.locked():            # Если счет не отрицательный и счет закрыт,
                self.lock.release()                                   # замок открываем
            sleep(0.001)                                              # Задержка

    def take(self):                                                    # Функция списания со счета
        for k in range(100):                                           # Цикл списания со счета 100 раз
            money_out = randint(50, 500)                         # Получаем случайное число от 50 до 500
            print(f"Запрос на {money_out}")                            # Выводим сообщение в консоль
            if money_out <= self.balance:                              # Если запрос меньше текущего баланса счета, то
                self.balance = self.balance - money_out                # списываем средства со счета
                print(f"Снятие: {money_out}. Баланс: {self.balance}")  # Выводим сообщение в консоль
            else:                                                      # Иначе
                print("Запрос отклонён, недостаточно средств")         # Выводим сообщение в консоль и
                self.lock.acquire()                                    # закрываем замок
            sleep(0.001)                                               # Задержка

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')