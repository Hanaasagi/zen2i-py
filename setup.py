import os
import re
import ast
from setuptools import setup

_name = 'zen2i'

_root = os.path.abspath(os.path.dirname(__file__))
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open(os.path.join(_root, '{}/__init__.py'.format(_name))) as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read()).group(1)))


with open(os.path.join(_root, 'README.md')) as f:
    readme = f.read()

_description = """\
兆までの漢数字を半角数字に変換します。 漢数字が続いていたらそれぞれ変換します
"""

setup(
    name=_name,
    version=version,
    description=_description,
    long_description=readme,
    url='https://github.com/Hanaasagi/zen2i-py',
    author='Hanaasagi',
    author_email='ambiguous404@gmail.com',
    license='MIT',
    python_requires='>=3.6',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],

    packages=['zen2i'],
)
