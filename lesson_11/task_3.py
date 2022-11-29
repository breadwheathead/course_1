"""
Создать собственный класс-исключение, который должен проверять содержимое списка на
наличие только чисел. Проверить работу исключения на реальном примере. Запрашивать у
пользователя данные и заполнять список необходимо только числами. Класс-исключение
должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока
пользователь сам не остановит работу скрипта, введя, например, команду «stop». При этом
скрипт завершается, сформированный список с числами выводится на экран.
Подсказка: для этого задания примем, что пользователь может вводить только числа и
строки. Во время ввода пользователем очередного элемента необходимо реализовать
проверку типа элемента. Вносить его в список, только если введено число. Класс-исключение
должен не позволить пользователю ввести текст (не число) и отобразить соответствующее
сообщение. При этом работа скрипта не должна завершаться

"""


class OnlyNumbersError(Exception):
    pass


def request_numbers_infinity():
    numbers = []
    while True:
        num = input('введите число или нажмите q для выхода: ')
        try:
            if num.isdigit():
                numbers.append(num)
            elif num == 'q':
                return numbers
            else:
                raise OnlyNumbersError
        except OnlyNumbersError as e:
            print('Только числа!')


if __name__ == '__main__':
    print(*request_numbers_infinity())