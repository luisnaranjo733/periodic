from setuptools import setup,find_packages
import os
def read(fname):
    return open(fname).read()
    
setup(
    name = "periodic",
    version = "2.1",
    author = "Jose Luis Naranjo Gomez",
    author_email = "luisnaranjo733@hotmail.com",
    description = ("A periodic table API."),
    license = "GNU GPL",
    keywords = "chem chemistry periodic table finder elements",
    url = "https://github.com/doubledubba/periodic",
    packages = find_packages(),
    package_data = {'': ['*.csv']},
    #long_description=read('README.txt'),
    classifiers=[
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Topic :: Utilities",
    ],

)
