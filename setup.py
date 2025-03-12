from setuptools import find_packages, setup
from typing import List

hy = '-e .'
def get_requirements(file_path:str)->List[str]:
    req = []
    with open(file_path) as file_object:
        req=file_object.readlines()
        requi = [r.replace("\n", '') for r in req]
        if hy in req:
            req.remove(hy)

setup(
    name = 'fraud deteaction', 
    author = 'Akanksha',
    author_email = 'akanksha.angurala@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)