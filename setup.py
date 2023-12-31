from setuptools import setup, find_packages

setup(
    name='bce-srm',
    version='0.0.1',
    description='This is a project developed by Serem for development purposes',
    author='teddylee777',
    author_email='gangh9230@gmail.com',
    url='https://github.com/teddylee777/teddynote',
    install_requires=['tqdm', 'pandas', 'scikit-learn',],
    packages=find_packages(exclude=[]),
    keywords=['teddynote', 'teddylee777', 'python datasets', 'python tutorial', 'pypi'],
    python_requires='>=3.6',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
