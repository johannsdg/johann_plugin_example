[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Johann Plugin Example

This repository is an example "plugin" for Johann consisting of the following:

- Celery tasks which can be used in Johann Scores both inside and outside this plugin
- Plugin-specific Scores that encode new scenarios/experiments
- Plugin-specific configuration variables
- Additions to Johann's core configuration variables
- Plugin-specific pip dependencies

This project does not contain, but the Johann plugin system also supports:

- Python modules that add new capabilities to Johann (e.g., an additional host control
  mechanism such as SSH or the VMware API)

## Structure of a Johann plugin

In order to keep the Johann plugin ecosystem consistent and compatible:

- Plugin repositories should be named _johann_extension_name_ , e.g.,
  `johann_plugin_example`
- Plugins must provide a single package named _johann_extension_name_, e.g.,
  `johann_plugin_example`
- Plugins must create pypi-style distributions that can be installed via pip
- Any Score files must be included in the distribution (e.g., via MANIFEST.in), and
  should be contained in a `scores` subfolder of the package
- It is **strongly** recommended that any publicly available plugins be BSD or MIT
  licensed
- Plugins should support the same versions of Python as Johann, namely Python 3.6+
- Plugin repositories should utilize the Developer Certificate of Origin (DCO) for each
  commit
  - This can be accomplished via the `-s` flag to git commit
