from setuptools import setup, find_packages

setup(
    name="github_readme_generator",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "gh-readme=github_readme_generator.generator:main",
        ],
    },
    install_requires=[
        "PyYAML>=5.3.1",
    ],
)
