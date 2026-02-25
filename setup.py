from setuptools import  find_packages, setup
from typing import List


# create a constant to prevent -e. from appearing..
HYPHEN_E_DOT= '-e.'

# function to download the libraries needed in requirements.txt
def get_requirements(file_path:str)->List[str]:
    """
    This function will return the list of requirements
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]
        
        #call constant
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name='MLproject',
    version='0.0.1',
    author='Udeme',
    author_email='demsyclim@gmail.com',
    packages=find_packages(),
    
    # for automatic installation of the packages
    install_requires= get_requirements("requirements.txt")
    
    
    
)