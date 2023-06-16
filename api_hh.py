import requests
from abc import ABC, abstractmethod

from vacancy import Vacancy


class APItets(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass


class HH(APItets):
    url = 'https://api.hh.ru/'

    def get_vacancies(self):
        params = {
            'text': vacancy,
            'page': 1,
            'per_page': 2,
            'area': 1,
            'experience': 'noExperience',
            'salary': 1,
        }

        api_request = requests.get('https://api.hh.ru/vacancies/', params=params).json()['items']
        vac = [
            Vacancy(req['name'], req['url'], req['area']['name'], req['salary'], req['snippet']['requirement'])
            for req in api_request]
        return vac


test = HH()
print('Введите вакансию, которую хотите найти')
vacancy = input()

for f in test.get_vacancies():
    print(f)
    if f.description:
        print()
