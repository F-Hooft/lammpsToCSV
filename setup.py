from setuptools import setup

setup(
    name='lammpsToCSV',
    version='0.1',
    py_modules=['lammpsToCSV'],
    install_requires=[
        'Click',
        'numpy',
        'pandas',
    ],
    entry_points='''
        [console_scripts]
        lammpsToCSV=lammpsToCSV:convert
    ''',
)