from setuptools import find_packages, setup

project = "Foo"
version = "0.1.0"

setup(
    name = project,
    version = version,
    description = "",
    author = "Foo Corp",
    packages = find_packages(exclude=["*.tests"]),
    include_packages_data = True,
    zip_safe = False,
    install_requires = [
        "Flask==3.0.0",
        "pydantic==2.4.2"
    ]
)
