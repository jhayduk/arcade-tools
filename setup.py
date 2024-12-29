from setuptools import setup

setup(
    name='arcade-tools',
    version='0.1.1',
    packages=["arcade_tools"],
    package_dir={"": "src"},
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
