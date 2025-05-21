import os
import setuptools


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setuptools.setup(
    name="python-whois-am",
    version="0.9.5+am.1",
    description="Whois querying and parsing of domain registration information.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Programming Language :: Python :: 3",
    ],
    keywords="whois, python",
    author="Amine nd",
    author_email="am.js.web@gmail.com",
    url="https://github.com/webemeia/whois",
    license="MIT",
    packages=["whois"],
    package_dir={"whois": "whois"},
    install_requires=["python-dateutil"],
    test_suite="nose.collector",
    tests_require=["nose", "simplejson"],
    include_package_data=True,
    zip_safe=False,
)
