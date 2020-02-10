import setuptools


__packagename__ = 'herpetologist'

setuptools.setup(
    name = __packagename__,
    packages = setuptools.find_packages(),
    version = '0.0.4',
    python_requires = '>=3.6.*',
    description = 'Dynamic parameter type checking for Python 3.6 and above. This able to detect deep nested variables.',
    author = 'huseinzol05',
    author_email = 'husein.zol05@gmail.com',
    url = 'https://github.com/huseinzol05/herpetologist',
    license = 'MIT',
    classifiers = [
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
