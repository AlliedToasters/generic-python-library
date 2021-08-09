from setuptools import find_packages, setup
import sys
import os

#build = os.environ.get("JENKINS_PATCH_VERSION", "dev")
# logic for release number
#if build == "dev":
#    patch_no = 0
#else:
#    patch_no = build
    #this offsets since the builder is only aware of
    #a monotonically increasing build number
#    patch_no = int(patch_no)

#version = "0.1.{}".format(patch_no)

version = "0.0.1"

requirements = [
    "numpy"
]

dev_requirements = [
    "pytest",
    "pytest-runner"
]

setup(
    name="generic-library",
    version=version,
    author="Michael Klear",
    author_email="michael.r.klear@gmail.com",
    url="https://github.com/alliedtoasters/some-repo-here",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    setup_requires=requirements + ["pytest-runner"],
    tests_require=requirements + dev_requirements,
)
