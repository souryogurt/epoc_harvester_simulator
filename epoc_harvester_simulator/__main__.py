# -*- coding: utf-8 -*-
"""Application that simmulates data send from native epoc_harvester application."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import sys

__all__ = ['main']


def main():
    """Entry point."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verbose', action='store_true', help='be verbose')
    args = parser.parse_args()
    if args.verbose:
        print('I am verbose')


if __name__ == "__main__":
    sys.exit(main())
