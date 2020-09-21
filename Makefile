# Copyright (c) 2020-present, The Johann Plugin Example Authors. All Rights Reserved.
# Use of this source code is governed by a BSD-3-clause license that can
# be found in the LICENSE file. See the AUTHORS file for names of contributors.

.PHONY: venv build test logs dev prep clean lint safety requirements

VENV_PATH = ./venv
VENV_PYTHON = $(VENV_PATH)/bin/python3
PRE_COMMIT = $(VENV_PATH)/bin/pre-commit
SAFETY = $(VENV_PATH)/bin/safety
TWINE = $(VENV_PATH)/bin/twine


# Cleanup
clean:
	$(MAKE) clean-files

clean-files:
	rm -rf build dist ./*.egg-info

clean-venv:
	rm -rf venv

clean-all: clean clean-venv

# Johann development - linting
lint:
	@if [ ! -f $(PRE_COMMIT) ]; then $(MAKE) dev-setup; fi
	$(PRE_COMMIT) run check-ast
	$(PRE_COMMIT) run --show-diff-on-failure

lint-all:
	@if [ ! -f $(PRE_COMMIT) ]; then $(MAKE) dev-setup; fi
	$(PRE_COMMIT) run -a check-ast
	$(PRE_COMMIT) run -a --show-diff-on-failure

safety:
	@if [ ! -f $(SAFETY) ]; then $(MAKE) dev-setup; fi
	$(SAFETY) check


# Johann development - other
dev-setup: dev-venv
	$(PRE_COMMIT) install --install-hooks -t pre-commit -t commit-msg -t pre-push

requirements:
	@if [ ! -f $(PRE_COMMIT) ]; then $(MAKE) dev-setup; fi
	-$(PRE_COMMIT) run -a --show-diff-on-failure pip-compile

dev-venv:
	rm -rf venv
	python3 -m venv $(VENV_PATH)
	$(VENV_PYTHON) -m pip install 'wheel>=0.33.6'
	$(VENV_PYTHON) -m pip install -r requirements.txt -r requirements-dev.txt

package:
	@if [ ! -f $(TWINE) ]; then $(MAKE) dev-setup; fi
	$(VENV_PYTHON) setup.py sdist bdist_wheel
	$(TWINE) check dist/*
