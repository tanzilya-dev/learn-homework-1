"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {"Как дела?": "Хорошо!", 
                         "Что делаешь?": "Программирую",
                         "Сколько раз ты сегодня чихнул?": 0}

def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    while True:
        question = input('Введите вопрос: ')
        answer = questions_and_answers.get(question)
        if answer is not None:
            print(answer)
        else:
            break        

    
if __name__ == "__main__":
    ask_user(questions_and_answers)
