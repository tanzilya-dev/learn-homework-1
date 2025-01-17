"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def get_occupation_by_age(age):
    if age < 0:
        return 'Возраст не может быть отрицательным!'
    elif age < 7:
        return 'Ходи пока в детский сад'
    elif age < 18:
        return 'Тебе следует ходить в школу'
    elif age < 22:
        return 'Тебе бы пойти в ВУЗ учиться'
    elif age < 65:
        return 'Иди работать'
    else:
        return 'Пора на пенсию'


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    try:
        age = int(input('Введите свой возраст: '))
        res = get_occupation_by_age(age)
        print(res)
    except (ValueError, TypeError):
        print('Возраст должен целым числом!') 

if __name__ == "__main__":
    main()
