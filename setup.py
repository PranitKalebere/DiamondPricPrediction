from setuptools import find_packages,setup
from typing import List

const = '-e .'

def get_requirements(filepath:str)->List[str]:
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if const in requirements:
            requirements.remove(const)
    return requirements

setup(
    name="Diamond Price Prediction",
    version="0.0.1",
    author = "Pranit Kalebere",
    author_email="pranitkalebere7266@gmail.com",
    install_requires = get_requirements("requirement.txt"),
    packages=find_packages()
)