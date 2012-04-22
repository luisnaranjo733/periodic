from setuptools import setup,find_packages
import os
def read(fname):
    return open(fname).read()
    
setup(
    name = "periodic",
    version = "2.0",
    author = "Jose Luis Naranjo Gomez",
    author_email = "luisnaranjo733@hotmail.com",
    description = ("A periodic table API."),
    license = "GNU GPL",
    keywords = "chem chemistry periodic table finder elements",
    url = "https://github.com/doubledubba/chem",
    packages=['periodic'],
    long_description=read('README.txt'),
    classifiers=[
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Topic :: Utilities",
    ],
)
