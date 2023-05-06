import re
from codecs import open
from setuptools import setup


with open('build.gradle', 'r') as f:
    version = re.search(r'^version\s*=\s*[\'"]([^\'"]*)[\'"]',
                        f.read(), re.MULTILINE).group(1)

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='pop-fundamentals',
    version=version,
    description='Implementation of algorithms, data structures and problems',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/6harat/pop-fundamentals',
    author='6harat',
    author_email='bharat.gulati.certi@gmail.com',
    packages=['py_dsa'],
    license='MIT License',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.10',
    ],
    install_requires=[],
)
