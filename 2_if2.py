"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def strings_check(str1, str2):
    if not(isinstance(str1, str) and isinstance(str2, str)):
        return 0
    if str1 == str2:
        return 1
    elif len(str1) > len(str2):
        return 2
    elif str2 == 'learn':
        return 3 


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(strings_check('Hi', 55))
    print(strings_check('Hi', 'Hi'))
    print(strings_check('Hello', 'Hi'))
    print(strings_check('Hi', 'learn'))
    
if __name__ == "__main__":
    main()
