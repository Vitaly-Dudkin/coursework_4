import os
from pprint import pprint
import requests
from vacancy import Vacancy


class SuperJobs:

    def get_vacancies(self):
        headers = {'X-Api-App-Id': os.getenv('X-Api-App-Id')}

        params = {
            'page': 1,
            'per_page': 1,
            'count': 1
        }

        r = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=headers, params=params).json()
        # vac = [Vacancy(req['title'], req['url'], req['town'], req['town'], req['title']) for req in r]

        return r


one = SuperJobs()
pprint(one.get_vacancies()['objects'][0])
