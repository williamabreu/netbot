# Usage: 
#
# -- Build the project for distribution:
#   python3 setup.py sdist bdist_wheel
# 
# -- Run unit tests:
#   python3 setup.py test
# 
# -- Run inside venv:
#   python setup.py develop 
#   venv/bin/netbot


from netbot import __version__
import setuptools


setuptools.setup(
    name='netbot',
    version=__version__,
    license='MIT License',
    author='William Abreu',
    author_email='contato@williamabreu.net',
    description='Python module for network management',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/williamabreu/netbot',
    install_requires=open('requirements.txt').read().splitlines(),
    platforms='any',
    packages=setuptools.find_packages('.', exclude=('netbot.tests',)),
    python_requires='>=3.7',
    test_suite='netbot.tests',
    keywords='',
    entry_points={
        'console_scripts': [
            'netbot=netbot.__main__:main'
        ]
    },
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking',
        'Topic :: Utilities',
    ],
)
