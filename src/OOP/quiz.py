# Напишите класс викторины с методами:
# 5.1 Начало работы викторины(задаётся вопрос, читается информация с консоли)
# 5.2 Определяет правильный ли ответ
# 5.3 Выводит правильный ответ, если пользователь ошибся. Если нет, то выводит верный ответ.
# 5.4 Считает количество правильных ответов
# 5.5 Выводит результат викторины(правильных ответов N из NN)
# https://i.imgur.com/B7sSdaW.png
# Какая река самая длинная в мире? Нил
# Какой химический символ у серебра? Ag
# Какой самый большой орган в теле человека? Кожа
# Чему равен квадратный корень из 64? 8
# Какая столица Португалии? Лиссабон
import json

def main() -> None:
    with open('quiz.json', 'r', encoding='utf-8') as file:
        quiz_data = json.load(file)

    quiz = Quiz(quiz_data)
    quiz.start_quiz()

class Quiz:
    def __init__(self, quiz_data: list[dict[str, str]]) -> None:
        self.quiz_data = quiz_data
        self.score_correct = 0
        self.score_all = len(quiz_data)

    def start_quiz(self) -> None:
        """Запуск викторины"""
        for question in self.quiz_data:
            self.question = question
            user_answer = input(f'{self.question["question"]}\n').lower()
            self.print_answer(user_answer)
            self.count_correct_answer()
        self.print_result_quiz()

    def check_answer(self, user_answer: str) -> bool:
        """Определяем правильный ли ответ"""
        return user_answer == self.question['correct_answer']

    def print_answer(self, user_answer: str) -> None:
        """Печать правильного/неправильного ответа, если неправильный - печать правильного"""
        self.correct_answer = self.check_answer(user_answer)
        if self.correct_answer:
            print('Верный ответ!')
            return
        print(f'Неправильно. Правильный ответ: {self.question["correct_answer"]}')
        return

    def count_correct_answer(self) -> None:
        """Считает кол-во правильных ответов"""
        if self.correct_answer:
            self.score_correct += 1

    def print_result_quiz(self) -> None:
        """Печать результата викторины"""
        print(f'Правильных ответов: {self.score_correct} из {self.score_all}')


if __name__ == '__main__':
    main()
