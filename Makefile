#!/bin/bash
include .env

build:
	conda build . --output-folder $(LOCAL_FOLDER) --verify
.PHONY: build

install:
	conda install $(TARBALL_PATH)
.PHONY: install
