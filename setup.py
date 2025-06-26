from setuptools import find_packages,setup
from typing import List

HIPN_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
    """This function take file path and give the list of requirements"""

    requirements = []

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [line.replace("\n"," ") for line in requirements]

    if HIPN_E_DOT in requirements:
        requirements.remove(HIPN_E_DOT)

    return requirements    

setup(
    name="ML project",
    version="0.0.1",
    description="this is an ml project",
    author="Lohith HS",
    maintainer_email="lohithls14@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)