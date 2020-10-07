# Copyright (c) 2020-present, The Johann Plugin Example Authors. All Rights Reserved.
# Use of this source code is governed by a BSD-3-clause license that can
# be found in the LICENSE file. See the AUTHORS file for names of contributors.

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="johann_plugin_example",
    description="An example of a plugin for Johann",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jeffrey James",
    author_email="lobotmcj@gmail.com",
    license="BSD",
    url="https://github.com/johannsdg/johann-plugin-example",
    include_package_data=True,
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.6, <4",
    install_requires=["johann>=0.2.0a0", "numpy"],
)
