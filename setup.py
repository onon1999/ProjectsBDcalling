

from setuptools import setup, find_packages

setup(
    name='your_package_name',
    version='0.1.0',
    packages=find_packages(),
    author='onon1999',
    author_email='onontaj1999@gmail.com',
    description='A short description of your package',
    url='https://github.com/yourusername/your_package_name',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        # Example dependencies
        'requests',
        'numpy>=1.20.0',
    ],
)

