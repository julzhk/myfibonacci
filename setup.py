from setuptools import find_packages, setup
with open("readme.md", "r") as fh:
    long_description = fh.read()
setup(
    name="myfibonacci_py",
    version="0.0.1",
    author="julz",
    author_email="axial.nitro0w@icloud.com",
    description="Calculates a Fibonacci number",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/julzhk/myfibonacci",
    install_requires=[],
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'fib-number = myfibonacci_py.cmd.fib_numb:fib_numb',
    ],
    },
)