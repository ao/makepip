import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='makepip',  
    version='0.3',
    author="Andrew O",
    author_email="support@ataiva.com",
    description="A pip that helps you make others pips!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://ataiva.com/makepip/",
    packages=["makepip"],
    entry_points = {
        "console_scripts": ['makepip = makepip.makepip:main']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
