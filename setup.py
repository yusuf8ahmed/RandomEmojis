from pip._internal.req import parse_requirements
from operator import attrgetter
from os import path
from setuptools import setup, find_packages

def read(fname):
    return open(path.join(path.dirname(__file__), fname)).read()

def from_here(relative_path):
    return path.join(path.dirname(__file__), relative_path)

with open('requirements.txt') as f: 
    requirements = f.readlines() 

# source env/bin/activate

#? test.pypi
# rm -rf build dist shipapp.egg-info
# python setup.py sdist bdist_wheel 
# python3 -m twine upload --skip-existing --repository testpypi dist/*

# pip install --index-url https://test.pypi.org/simple/ --upgrade --no-cache-dir --extra-index-url=https://pypi.org/simple/ shipapp

#? pypi
# rm -rf build dist shipapp.egg-info
# python setup.py sdist bdist_wheel 
# twine upload --skip-existing dist/*

#? git steps
# git init
# git status
# git add .
# git init && git status && git add .
# git commit -m "alpha release v0.0.3.x"
# git push origin master

setup(
    name="randomemojis",
    version="0.3",
    author="Yusuf Ahmed",
    author_email="yusufahmed172@gmail.com",
    packages=find_packages(exclude=['test_files']),
    description="RandomEmojis: Generates random emoji(s) where {x ∈ R+}",
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    url="https://github.com/yusuf8ahmed/RandomEmojis",
    install_requires=[
        "aiocontextvars==0.2.2",
        "attrs==20.2.0",
        "certifi==2020.6.20",
        "chardet==3.0.4",
        "click==7.1.2",
        "contextvars==2.4",
        "idna==2.10",
        "immutables==0.14",
        "importlib-metadata==1.7.0",
        "iniconfig==1.0.1",
        "loguru==0.5.3",
        "lxml==4.5.2",
        "more-itertools==8.5.0",
        "packaging==20.4",
        "pluggy==0.13.1",
        "py==1.9.0",
        "pyparsing==2.4.7",
        "pytest==6.0.2",
        "requests==2.24.0",
        "six==1.15.0",
        "toml==0.10.1",
        "urllib3==1.25.10",
        "zipp==3.1.0"
        ],
    entry_points ={ 
        'console_scripts': [ 
            'emojis = emojis.__main__:cli'
        ] 
    },
    package_data={'': ['requirements.txt']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: End Users/Desktop"
    ],
    keywords ='random emojis',
    python_requires='>=3',
    zip_safe = False
)