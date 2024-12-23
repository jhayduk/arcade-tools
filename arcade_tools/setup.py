from setuptools import setup, find_packages

setup(
    name='arcade-tools',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pygame==2.6.1'
    ],
    author='John Hayduk',
    author_email='john.hayduk@gmail.com',
    description='A collection of utilities and tools for a collection of arcade hobby projects.',
    url='https://github.com/jhayduk/arcade-tools',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)
