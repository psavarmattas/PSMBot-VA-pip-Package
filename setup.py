import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "PSMBot",
    version = "1.0",
    scripts = ["PSMBot"],
    author = "Puranjay Savar Mattas",
    author_email = "puranjaysavarmattas@gmail.com",
    description = "A package to help you easily make a Virtual Assistant",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "",
    home_page = "",
    license = "Apache License 2.0",
    platform = "Any",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'speechrecognition', 
        'pyttsx3',
        'pywhatkit',
        'wikipedia',
        'pyjokes',
        'wolframalpha',
        'datetime',
    ],
    python_requires='>=3.8',
)