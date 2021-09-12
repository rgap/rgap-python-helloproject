import setuptools

with open("README.md", "r") as fh:
    readme = fh.read()

short_description = (
    "A pip-installable package example."
)
setuptools.setup(
    name='helloproject',
    version='2.0',
    author='Rel Guzman',
    author_email='rel.guzmanapaza@sydney.edu.au',
    description=short_description,
    long_description=readme,
    long_description_content_type="text/markdown",
    url='https://github.com/rgap/helloproject',
    keywords=['example'],
    packages=setuptools.find_packages(".")# find_packages(exclude=("notebooks", "docs", "scripts")),
    license="GPL",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "numpy >= 1.18.1",
    ]
)