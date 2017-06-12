from distutils.core import setup

setup(
    name='fuzzy-engine',
    version='0.1.0',
    url='https://github.com/pennsignals/fuzzy-engine',
    packages=['fuzzy'],
    include_package_data=True,
    install_requires=[
        'flask',
    ]
)
