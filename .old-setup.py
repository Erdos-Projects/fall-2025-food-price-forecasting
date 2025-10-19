from setuptools import setup, find_packages

setup(
    name='food_price_forecasting',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
