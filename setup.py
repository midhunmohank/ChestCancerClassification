import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

__version__ = "0.1.0"


REPO_NAME = "ChestCancerClassification"
AUTHOR_USERNAME = "midhunmohank"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "mmohan05@outlook.com"

setuptools.setup(
    name= SRC_REPO,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="Chess Cancer Classification with CNN and Transfer Learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url= f"https://githib.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues",
    },
    packages= setuptools.find_packages(where="src")

)