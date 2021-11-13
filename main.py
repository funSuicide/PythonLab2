import re
import json


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

    def __init__(self, telephone: str, height: float, snils: str, passport_number: str, age: int, address: str,
                 occupation: str, political_views: str,
                 worldview: str):
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
        if re.match(r"^\d{6}$", self.__snils) is not None:
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
