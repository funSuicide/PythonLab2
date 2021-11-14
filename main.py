import re
import json
import argparse
from tqdm import tqdm


class Validator:
    __telephone: str
    __height: float
    __snils: str
    __passport_number: str
    __age: int
    __address: str
    __occupation: str
    __political_views: str
    __worldview: str
    __occupation_invalid = ['Монах',
                            'Маг',
                            'Паладин',
                            'Кодер']
    __political_views_invalid = ['поддерживает Имперский легион',
                                 'патриот независимой Темерии', 'поддерживает Братьев Бури',
                                 'согласен с действиями Гарроша Адского Крика на посту вождя Орды']
    __worldview_invalid = ['Культ Вечного Огня',
                           'Культ богини Мелитэле',
                           'Культ пророка Лебеды',
                           'Культ Механикус',
                           'Храм Трибунала',
                           'Девять божеств',
                           'Культ проклятых',
                           'Светское гачимученничество']

    def __init__(self, telephone: str, height: float, snils: str, passport_number: str, age: int, occupation: str,
                 political_views: str,
                 worldview: str, address: str):
        self.__telephone = telephone
        self.__height = height
        self.__snils = snils
        self.__passport_number = passport_number
        self.__age = age
        self.__address = address
        self.__occupation = occupation
        self.__political_views = political_views
        self.__worldview = worldview

    def check_telephone(self) -> bool:
        """
        Проверка корректности номера телефона
        Если строка удовлетворяет шаблону +?-(???)-???-??-??, где ? - [0-9] возвращает True, иначе False

        :return: bool
        Булевый результат проверки
        """
        if re.match(r"^\+(\d)-\((\d{3})\)-(\d{3})-(\d{2})-(\d{2})$", self.__telephone) is not None:
            return True
        return False

    def check_height(self) -> bool:
        """"
        Проверка корректности роста
        Если строка содержит дробное число с разделителем возвращает True, иначе False

        :return: bool
        Булевый результат проверки
        """
        if re.match(r"^\d{1,2}\.\d{1,2}$", str(self.__height)) is not None and (float(self.__height) > 1.50) and \
                (float(self.__height) < 2.20):
            return True
        return False

    def check__snils(self) -> bool:
        """
        Проверка корректности СНИЛС
        Если строка содержит 11 цифр [0-9] возвращает True, иначе False

        :return: bool
        Булевый результат проверки
        """
        if re.match(r"^\d{11}$", self.__snils) is not None:
            return True
        return False

    def check_passport_number(self) -> bool:
        """
        Проверка корректности номера паспорта
        Если строка содержит 6 цифр [0-9] возвращает True, иначе False

        :return: bool
        Булевый результат проверки
        """
        if re.match(r"^\d{6}$", str(self.__passport_number)) is not None:
            return True
        return False

    def check_age(self) -> bool:
        """
        Проверка корректности возраста
        Если строка содержит 2 цифры [0-9] и удовлетворяет условию возвращает True, иначе False

        :return: bool
        Булевый результат проверки
        """
        if re.match(r"^\d{2}$", str(self.__age)) is not None and (int(self.__age) > 18) and (int(self.__age) < 70):
            return True
        return False

    def check_address(self) -> bool:
        """
        Проверку корректности адреса.
        Если строка начинается с ул. или с Алллея возвращает True, иначе False.

        :return: bool
        Булевый результат проверки
        """
        if re.match(r"(ул\.\s[\w .-]+\d+)", self.__address) is not None and re.match(r"^Аллея\s[\w .-]+\d+$",
                                                                                     self.__address) is None:
            return True
        return False

    def check_occupation(self) -> bool:
        """
        Проверка корректности записи профессии
        Если строка начинается с букв [A-Z][А-Я], не содержит цифр
        и не входит в невалидные значения возвращает True, иначе False.

        :return: bool
        Булевый результат проверки
        """
        if self.__occupation not in self.__occupation_invalid and re.match(r"^([A-Z]|[А-Я])[\D]+$", self.__occupation) \
                is not None:
            return True
        return False

    def check_political_views(self) -> bool:
        """
        Проверка корренктности записи политических взглядов
        Если строка содержит только буквы [А-Я][а-я] и не входит в невалидные значения возвращает True, иначе False.

        :return:
        Булевый результат проверки
        """
        if self.__political_views not in self.__political_views_invalid and \
                re.match(r"^[\D]+$", self.__political_views) is not None:
            return True
        return False

    def check_worldview(self) -> bool:
        """
        Проверка корректности записи мировозрения
        Если строка содержит только буквы [А-Я][а-я] и не входит в невалидные значения возвращает True, иначе False.

        :return:
        Булевый результат проверки
        """
        if self.__worldview not in self.__worldview_invalid and \
                re.match(r"^[\D]+$", self.__worldview) is not None:
            return True
        return False

    def check_all(self) -> int:
        """
        Выполнение всех проверок класса

        :return: int
        Целочисленный результат (номер невалидного значения)
        """
        if not self.check_telephone():
            return 0
        elif not self.check_height():
            return 1
        elif not self.check__snils():
            return 2
        elif not self.check_passport_number():
            return 3
        elif not self.check_age():
            return 4
        elif not self.check_occupation():
            return 5
        elif not self.check_address():
            return 6
        elif not self.check_political_views():
            return 7
        elif not self.check_worldview():
            return 8
        else:
            return 9


class ReadFile:
    """
    Объект ReadFile считывает и хранит данные из выбранного файла.
    Attributes
      ----------
      __data - хранит данные, считанные из файла
    """

    __data: object

    def __init__(self, path: str):
        """
        __init__ - инициализирует экземпляр класса ReadFromFile
        Parameters
        ----------
        path : str
        Путь до выбранного файла
        """
        self.__data = json.load(open(path, encoding='windows-1251'))

    @property
    def data(self) -> object:
        """
        data - метод получения данных файла
        :return: object
        Возвращает тип object
        """
        return self.__data


parser = argparse.ArgumentParser(description='main')
parser.add_argument('-input', dest="file_input", default='92.txt', type=str)
parser.add_argument('-output', dest="file_output", default='92_output.txt', type=str)
args = parser.parse_args()
output = open(args.file_output, 'w')
file = ReadFile(args.file_input)
checkers = [0, 0, 0, 0, 0, 0, 0, 0, 0]
number_of_valid_records = 0
with tqdm(file.data, desc='Прогресс валидации', colour="#FFFFFF") as progressbar:
    for elem in file.data:
        check_element = Validator(elem['telephone'], elem['height'], elem['snils'], elem['passport_number'],
                                  elem['age'],
                                  elem['occupation'], elem['political_views'], elem['worldview'], elem['address'])
        valid_values = check_element.check_all()
        if valid_values == 9:
            output.write("telephone: " + elem["telephone"] + "\n" + "height:" + str(elem["height"]) + "\n" +
                         "snils: " + elem["snils"] + "\n" + "passport_number:" + str(elem["passport_number"]) + "\n" +
                         "age: " + str(elem["age"]) + "\n" + "occupation: " + elem["occupation"]
                         + "\n" + "political_views: " + elem["political_views"] + "\n" + "worldview: " + elem[
                             "worldview"] +
                         "\n" + "address: " + elem["address"] + "\n" + "__________________________________________\n")
            number_of_valid_records += 1
        else:
            checkers[valid_values] += 1
        progressbar.update(1)
number_of_invalid_records = checkers[0] + checkers[1] + checkers[2] + checkers[3] + checkers[4] + checkers[5] + \
                            checkers[6] + checkers[
                                7] + checkers[8]
print("Общее число корректных записей:", number_of_valid_records, )
print("Общее число некорректных записей:", number_of_invalid_records)
print("Ошибки в telephone:", checkers[0])
print("Ошибки в height:", checkers[1])
print("Ошибки в snils:", checkers[2])
print("Ошибки в passport_number:", checkers[3])
print("Ошибки в age:", checkers[4])
print("Ошибки в occupation:", checkers[5])
print("Ошибки в political_views:", checkers[6])
print("Ошибки в worldview:", checkers[7])
print("Ошибки в address:", checkers[8])
output.close()
