"""
# pyTDGL

Time-dependent Ginzburg-Landau in Python.
"""

from setuptools import setup, find_packages

DESCRIPTION = "pyTDGL: Time-dependent Ginzburg-Landau in Python."
LONG_DESCRIPTION = __doc__

NAME = "tdgl"
AUTHOR = "Logan Bishop-Van Horn"
AUTHOR_EMAIL = "logan.bvh@gmail.com"
URL = "https://github.com/loganbvh/py-tdgl"
LICENSE = "MIT"
PYTHON_VERSION = ">=3.7, <=3.10"

INSTALL_REQUIRES = [
    "dill",
    "h5py",
    "matplotlib",
    "meshpy",
    "numpy",
    "optimesh",
    "pint",
    "pytest",
    "pytest-cov",
    "scipy",
    "shapely",
    "tqdm",
]

EXTRAS_REQUIRE = {
    "dev": [
        "black",
        "pre-commit",
    ],
    "docs": [
        "sphinx",
        "sphinx_rtd_theme",
        "sphinx-autodoc-typehints",
        "nbsphinx",
        "pillow",  # required for image scaling in RTD
    ],
    # "jax": [
    #     "jax[cpu]",
    # ],
}

CLASSIFIERS = [
    "Development Status :: 2 - Pre-Alpha",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Operating System :: MacOS",
    "Operating System :: POSIX",
    "Operating System :: Unix",
    "Operating System :: Microsoft :: Windows",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Topic :: Scientific/Engineering",
    "Topic :: Scientific/Engineering :: Physics",
]

PLATFORMS = ["Linux", "Mac OSX", "Unix", "Windows"]
KEYWORDS = "superconductor vortex Ginzburg-Landau"

exec(open("tdgl/version.py").read())

setup(
    name=NAME,
    version=__version__,  # noqa: F821
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    platforms=PLATFORMS,
    python_requires=PYTHON_VERSION,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
)