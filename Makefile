.PHONY: help setup venv dependencies freeze run-server clean clean-cache clean-venv

.DEFAULT: help

# ----------------------- #
# Define some variables   #
# ----------------------- #
REQUIREMENTS = requirements.txt
VENV ?= venv

VENV_ACTIVATE = $(VENV)/bin/activate
PYTHON = $(VENV)/bin/python3
PIP = $(PYTHON) -m pip

# ----------------------- #
# Help                    #
# ----------------------- #

help:
	@echo "----------------HELP-------------------"
	@echo "To set up the project, type: make setup"
	@echo "---------------------------------------"

# ----------------------- #
# Setup                   #
# ----------------------- #

setup: clean-venv venv dependencies

venv:
	test -d $(VENV) || python3 -m venv $(VENV)
	. $(VENV_ACTIVATE)
	$(PIP) install --upgrade pip

dependencies: venv $(REQUIREMENTS)
	$(PIP) install -r $(REQUIREMENTS)

freeze: $(REQUIREMENTS)
	$(PIP) freeze > $(REQUIREMENTS)

# ----------------------- #
# Run server              #
# ----------------------- #

run-server:
	. $(VENV_ACTIVATE)
	$(PYTHON) manage.py runserver

# ----------------------- #
# Clean                   #
# ----------------------- #

clean: clean-cache clean-venv

clean-cache:
	rm -rf .pytest_cache

clean-venv:
	rm -rf $(VENV)
