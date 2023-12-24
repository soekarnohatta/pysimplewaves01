import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "pysimplewaves",
    version = "0.0.1",
    author = "nayef",
    author_email = "nayefhaidir@outlook.co.id",
    description = "simple wave modelling in python",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://nayefhaidir.me",
    project_urls = {
        "Bug Tracker": "https://github.com",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "wave"},
    packages = setuptools.find_packages(where="wave"),
    python_requires = ">=3.6"
)