from setuptools import find_packages,setup
from typing import List 

HYPHEN_E = '-e . '
def get_requirements(file_path: str ) -> List[str]  : 
    requirements = []
    i = 0 
    with open(file_path) as file_obj : 
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements] 
        
        if HYPHEN_E in requirements : 
            requirements.remove(HYPHEN_E)
    return requirements


setup(
    name = "MLProject" , 
    version = "0.0.1" ,
    author = "KushThakral" ,
    author_email="kushthakral1234567@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

)