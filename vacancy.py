# @total_ordering
class Test:
    # vacancy_id, salary, description
    def __init__(self, name_vacancy, city):
        self.name_vacancy = name_vacancy
        self.city = city
        # self.vacancy_id = vacancy_id
        # self.salary = salary
        # self.description = description

    def str(self):
        return f"Город : {self.city}\n" \
               f"Вакансия: {self.name_vacancy}"