from setuptools import setup, find_packages


description = (
    'Sphinx extension for Data Dictionary and Database Diagram'
)

with open('README.rst', 'r', encoding='utf8') as f:
    long_description = f.read()

requires = [
    'Sphinx>=0.6',
    'PyYAML >= 3.12',
    'jsonschema >= 2.5.1',
    'recommonmark >= 0.4.0',
]

keywords = [
    'sphinx',
    'sphinxcontrib',
    'data dictionary',
    'database diagram',
]

setup(
    name='sphinxcontrib-dd',
    version='0.1.7+abc',
    url='https://github.com/julot/sphinxcontrib-dd',
    license='MIT',
    author='Andy Yulius',
    author_email='andy.julot@gmail.com',
    description=description,
    long_description=long_description,
    keywords=' '.join(keywords),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Extension',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    namespace_packages=['sphinxcontrib'],
)
