from setuptools import setup, find_packages

requires = [
    'flask',
    'flask-sqlalchemy',
    'psycopg2',
]

setup(
    name='flask_lab',
    version='0.0',
    description='A db 4th lab built with Flask',
    author='<Vadym Solovii>',
    author_email='<Vadym.Soloviy.ir.2022@lpnu.ua>',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
)
