from setuptools import setup, find_packages

setup(
    name='surugayaparser',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'BeautifulSoup'
    ]
)
