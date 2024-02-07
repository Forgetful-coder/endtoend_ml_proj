from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirments(file_path:str)->List[str]:
    '''
    this function will return requiremnets


    '''
    requires=[]
    with open(file_path) as file_obj:
        requires = file_obj.readlines()
        requires = [req.replace('\n','') for req in requires]

        if HYPEN_E_DOT in requires:
            requires.remove(HYPEN_E_DOT)
    
    return requires





setup(

    name = 'mlproj',
    verison = '0.0.1',
    author='Aayush',
    author_email='aayushaggarwal243@gmail.com',
    packages=find_packages(),
    install_requires = get_requirments('requirements.txt')

)