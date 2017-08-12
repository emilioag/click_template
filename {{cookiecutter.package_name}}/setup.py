from setuptools import setup

setup(
    name='{{cookiecutter.script_name}}',
    version='0.1',
    py_modules=['{{cookiecutter.package_name}}'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        {{cookiecutter.script_name}}=script.main:main
    ''',
)