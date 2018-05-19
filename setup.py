from setuptools import setup

__version__ = '0.0.1'
__author__ = 'MohanSha'

requirements = [
    'selenium==2.53.6',
    'clarifai==2.0.32',
    'pyvirtualdisplay',
    'emoji'
]

description = 'Instagram Like, Comment and Follow Automation Script'

setup(
    name='instagram_py',
    version=__version__,
    author=__author__,
    author_email='mohansha@outlook.com',
    url='https://github.com/MohanSha/InstaPy',
    py_modules='instapy',
    description=description,
    install_requires=requirements
)
