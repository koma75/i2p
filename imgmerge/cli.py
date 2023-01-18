#!/usr/bin/env python
# -*- coding: utf-8 -*-
# BSD 2-Clause License
# 
# Copyright (c) 2022 koma75 <omoikane@path-works.net>
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""Main CLI Setup and Entrypoint."""

from __future__ import absolute_import, division, print_function

# Import the main click library
import click
# Import the sub-command implementations
from .i2p import i2p
# Import the version information
from imgmerge.version import __version__

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=__version__)
def cli():
    """cli tool: Convert set of images to PDF."""
    pass

@cli.command()
@click.argument('img', nargs=-1, type=click.Path(exists=True))
@click.option(
    '--config', '-c', default="./imgmerge.yml",
    type=click.Path(exists=False, dir_okay=False, writable=True, resolve_path=True),
    metavar='<cfg>',
    help='Configuration File (default: imgmerge.yml)'
    )
@click.option(
    '--out', '-o', type=str,
    metavar='<out>',
    help='output filename for the generated PDF'
    )
@click.option(
    '--toc', '-t', type=str,
    metavar='<toc>',
    help='toc file to populate PDF outline'
    )
@click.option(
    '--ext', '-e', type=str,
    multiple=True,
    metavar='<ext>',
    help='file extensions to pick up when parsing directories'
    )
@click.option(
    '--dpi', '-d', type=int,
    metavar='<dpi>',
    help='pixel density of input image in dpi'
    )
@click.option(
    '--verbose', '-v', count=True,
    help='output in verbose mode'
    )
def join(**kwargs):
    """join images into one PDF file"""
    i2p.join(kwargs)
    pass

# Entry point
def main():
    """Main script."""
    cli()

if __name__ == '__main__':
    main()
