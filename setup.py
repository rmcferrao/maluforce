from setuptools import setup
# import textwrap
import sys
import os


pyver_install_requires = []
pyver_tests_require = []

here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, 'maluforce', '__version__.py'), 'r') as f:
    exec(f.read(), about)


setup(
    name=about['__title__'],
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    maintainer=about['__maintainer__'],
    maintainer_email=about['__maintainer_email__'],
    packages=['maluforce', ],
    url=about['__url__'],
    license=about['__license__'],
    description=about['__description__'],
    # long_description=textwrap.dedent(open('README.rst', 'r').read()),

    install_requires=[
        'pandas==1.3.2',
        'numpy==1.21.3',
        'simple-salesforce==0.74.2'
    ] + pyver_install_requires,
    keywords=about['__keywords__'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
