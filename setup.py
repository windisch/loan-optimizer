from setuptools import setup

setup(
    name="loan-optimizer",
    version="0.0.1",
    packages=["loan_optimizer"],

    # dependencies
    install_requires=[
        'numpy>1.14.0,<2.0.0',
    ],
    tests_require=[
        "pytest",
        'pytest-runner',
    ],

    # metadata for upload to PyPI
    author="Tobias Windisch",
    author_email="tobias.windisch@posteo.de",
    description="Python helper to optimize loans",
    license="GNU GPL3",
    keywords="loans",
    url="https://github.com/windisch/loan-optimizer",
)
