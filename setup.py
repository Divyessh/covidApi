import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as req:
    require = req.read()
    listOfReq = require.split('\n')

setuptools.setup(
    name="Covid-Api", 
    version="0.0.1",
    author="Divyessh Maheshwari",
    author_email="divyesshm@gmail.com",
    license = "GNU License",
    description="an API that is used for getting the updates of covid 19 from jhu - https://github.com/CSSEGISandData/COVID-19 - Worldwide Data repository",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Divyessh/covidApi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires= listOfReq,
)