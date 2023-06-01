from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="fontespass_passwordgenerator",
    version="0.0.1",
    author="Marcio Fontes",
    author_email="devfontesmarcio@gmail.com",
    description="The fontespass_passwordgenerator package is designed to provide functionality "
                "for generating secure passwords.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dev-marciofontes",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
