#!/usr/bin/env python
from setuptools import dist
dist.Distribution().fetch_build_eggs(['setuptools_rust'])

from setuptools_rust import Binding, RustExtension
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
    packages=["flitton_fib_rs"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Rust",
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
    ],
    python_requires='>=3',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'fib-number = myfibonacci_py.cmd.fib_numb:fib_numb',
    ],
    },
    rust_extensions=[RustExtension(
    ".flitton_fib_rs.flitton_fib_rs",
        path="Cargo.toml", binding=Binding.PyO3)],
    zip_safe=False,
)
