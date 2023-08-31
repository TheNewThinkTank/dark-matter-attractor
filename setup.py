import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dark_matter_tools",  # "dm_pkg_thenewthinktank"
    version="0.0.4",
    author="Gustav C. Rasmussen",
    description="Dark matter data classes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheNewThinkTank/dark-matter-attractor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
