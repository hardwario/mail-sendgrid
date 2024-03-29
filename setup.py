import setuptools
import os
import re
import codecs

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


name = 'mail-sendgrid'

setuptools.setup(
    name=name,
    version=find_version(name.replace('-', '_'), '__init__.py'),
    description='Cli tool for send mail over sendgrid',
    author='HARDWARIO s.r.o.',
    author_email='ask@hardwario.com',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/hardwario/mail-sendgrid',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
    ],
    keywords='cooper influxdb iot',
    platforms='any',
    packages=setuptools.find_packages(),
    install_requires=read('requirements.txt'),
    entry_points={
        'console_scripts': [
            '%s=%s:main' % (name, name.replace('-', '_'))
        ]
    },
    test_suite="tests"
)
