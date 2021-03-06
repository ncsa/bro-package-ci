#!/usr/bin/env python3
import os
import sys
from .types import CheckResult
from ..bropkg import get_metadata

NAME = "build_command"
DESCRIPTION = "Check if the package defines a build_command"

def check_build_command(pkg):
    md = get_metadata(pkg)
    if 'build_command' not in md:
        return CheckResult(NAME, DESCRIPTION, True)
    bc = md['build_command']
    msg = "Package contains build command: {!r}".format(bc)
    return CheckResult(NAME, DESCRIPTION, True, info=[msg])
