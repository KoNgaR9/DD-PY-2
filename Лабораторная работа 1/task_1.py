# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Teacher:
    """
    Класс описывает модель учителя.
    """
    def __init__(self, speciality: str, experience: int):
        """ Инициализация экземпляра класса.
        :param speciality: обозначает специализацию учителя (предметная область)
        :param experience: обозначает опыт учителя (кол-во полных отработанных лет по специальности
        """
        if experience > 55:
            raise ValueError("Слишком пожилой учитель")
        if experience < 20:
            raise ValueError("Слишком молодой учитель или недопустимый возврас")
        self.experience = experience
        self.speciality = speciality

    def teaching(self) -> str:
        """
        Метод для обозначения основной деятельности учителя.
        :return возвращает название урока, которое может провести учитель (по своей специализации)
        """
        pass

    def training(self) -> int:
        """
        Метод для обозначения повышения квалификации учителя.
        :return возвращает кол-во часов, проведенных на повышении квалификации
        """
        pass


class Student:
    """
    Класс описывает модель ученика.
    """
    def __init__(self, age: int, favorite_science: str):
        """ Инициализация экземпляра класса.
         :param age: возраст ученика
         :param favorite_science: любимая дисциплина (урок) ученика
         """
        if age > 19:
            raise ValueError("Недопустимый возраст ученика")
        if age < 5:
            raise ValueError("Недопустимый возраст ученика")
        self.age = age
        self.favorite_science = favorite_science

    def studying(self):
        """
        Метод для обозначения основной деятельности ученика.
        """
        pass

    def exam(self, subject: str, number_exam: int):
        """
        Метод для обозначения конечного этапа обучение
        :param subject: обозначение предмета сдачи экзамена
        :param number_exam: обозначение кол-ва экзаменов
        """
        pass


class Workbook:
    """
    Класс описывает модель учебника.
    """

    def __init__(self, science: str, pages: int):
        """ Инициализация экземпляра класса.
        :param science: предметная область учебника
        :param pages: кол-во страниц учебника
        """
        self.science = science
        self.pages = pages
        if pages > 5000:
            raise ValueError("Недопустимое кол-во страниц для учебника")
        if pages < 20:
            raise ValueError("Недопустимое кол-во страниц для учебника")

    def read(self, current_page: int) -> int:
        """
        Метод для обозначения прочтения учебника.
        :param current_page: текущая страница учебника
        :return: возвращает переменную с типом int
        """
        pass

    def new_page(self):
        """
        Метод для перелистывания страницы.
        """
        pass

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
