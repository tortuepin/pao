from setuptools import setup, find_packages

setup(
    name="pao",
    version='1,0',
    py_modules=['pao'],
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        pao=pao:main
        ''',
    data_files=[('data', ['pao.txt'])],
)
