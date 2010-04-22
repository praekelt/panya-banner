from setuptools import setup, find_packages

setup(
    name='django-banner',
    version='dev',
    description='Django banner app.',
    author='Praekelt Consulting',
    author_email='dev@praekelt.com',
    url='https://github.com/praekelt/django-banner',
    packages = find_packages(),
    include_package_data=True,
)

