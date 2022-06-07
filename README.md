# Software and Systems Laboratory Version Utility

> Utility tool to bump versions of projects

## Table of Contents

- [Software and Systems Laboratory Version Utility](#software-and-systems-laboratory-version-utility)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Install](#install)
  - [Command Line Options](#command-line-options)

## About

This is a tool to be used on Software and Systems Laboratory (SSL) software
projects for managing versions in different build systems.

## Install

We are releasing this software on GitHub alone as other solutions exist for
this problem.

## Command Line Options

```shell
usage: Utility tool to handle versions of Software and Systems Laboratory (SSL) projects

This utility is meant to be used as a development dependency to version bump a project, or to retrieve the version number for a SSL project.

options:
  -f FILE, --file FILE  Filepath to change project version. DEFAULT: pyproject.toml
  -h, --help            show this help message and exit
  -r, --read-version    Flag to read version value from file: DEFAULT: False
  -s SET_VERSION, --set-version SET_VERSION
                        Set version of project to a value. DEFAULT: None
  -v, --version         Print version of the tool

Author(s): Software and Systems Laboratory - Loyola University Chicago```
