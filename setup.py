# setup.py responsible for creating this ML application as a package
from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    returns the requirements needed
    '''
    requirements=[]
    with open(file_path) as files:
        requirements=files.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='ML-Backbone-Project',
    version='0.0.1',
    author='Maran',
    author_email='maranarunmozhi@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)