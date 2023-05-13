from setuptools import setup,find_packages
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        # here \n is replaced with blanck

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT) # removed -e . from list

    return requirements
    
setup(
name = 'mlproject',
version = '0.01',
author = 'pratik',
author_email = 'pratikchothe1@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)



