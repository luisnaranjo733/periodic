from setuptools import setup,find_packages
#from distutils.core import setup
import os

def read(fname):  # TODO: Implement this
    fpath = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), fname)
    return open(fpath).read()
    
setup(
    name = "periodic",
    version = '2.1',
    author = 'Jose Luis Naranjo Gomez',
    author_email = 'luisnaranjo733@hotmail.com',
    description = ("A periodic table API."),
    license = "GNU GPL",
    keywords = "chem chemistry periodic table finder elements",
    url = "https://github.com/doubledubba/periodic",
    packages = ['periodic'],
    package_data = {'': ['table.db', 'README.rst']},
    entry_points = {
    'console_scripts': ['periodic = periodic.table:interactive_shell']
    },
    install_requires = ['SQLAlchemy==0.7.7'],
    #long_description=read('README.txt'),
    classifiers=[
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Topic :: Utilities",
    ],

)
