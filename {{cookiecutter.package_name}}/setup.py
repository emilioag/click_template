from setuptools import setup, find_packages

setup(
    name=script,
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        {{cookiecutter.script_name}}=script.main:main
    ''',
)