from functools import total_ordering


@total_ordering
class Vacancy:
    # vacancy_id, salary, description
    def __init__(self, name_vacancy, vacancy_url, city, salary, description):
        self.set_vacancy_info(name_vacancy, vacancy_url, city)
        self.name_vacancy = name_vacancy
        self.vacancy_url = vacancy_url
        self.city = city
        self.salary = salary
        self.description = description

    def __str__(self):
        return f"Город: {self.city}\n" \
               f"Ссылка: {self.vacancy_url}\n" \
               f"Вакансия: {self.name_vacancy}\n" \
               f"Зарплата: {self.salary}\n" \
               f"Описание: {self.description}"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.salary == other.salary

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.salary > other.salary

    @staticmethod
    def set_vacancy_info(name_vacancy, vacancy_url, city):
        if not isinstance(name_vacancy, str):
            raise 'Название вакансии должно быть строкой'
        if 'https:/' not in vacancy_url:
            raise 'Ссылка на вакансию не правильная'
        if not city.isalpha():
            raise 'В название города должны быть только буквы'


