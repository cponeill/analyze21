from setuptools import setup

setup(
    name='analyze21',
    version='0.1',
    py_modules=['analyze21'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        analyze21=analyze21:cli
    ''',
)
