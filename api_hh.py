import requests
from abc import ABC, abstractmethod

from vacancy import Test


class APItets(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass


class HHtest(APItets):
    url = 'https://api.hh.ru/'

    def get_vacancies(self):

        params = {
            'text': 'NAME:Python',
            'page': 0,
            'per_page': 3,
            'area': 1,
            'experience': 'noExperience'
        }

        r = requests.get('https://api.hh.ru/vacancies/', params=params).json()['items']
        vac = [Test(req['name'], req['area']['name']) for req in r]
        return vac


test = HHtest()
for f in test.get_vacancies():
    print(f)

param = {
    'text': 'NAME:JS',
    'page': 0,
    'per_page': 2,
    'area': 1,
    'experience': 'noExperience'
}

q = requests.get('https://api.hh.ru/vacancies/', params=param).json()['items']
