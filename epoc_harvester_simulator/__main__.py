# -*- coding: utf-8 -*-
"""Application that simmulates data send from native epoc_harvester application."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import sys
import os

import asyncio
import websockets
import json

from pkg_resources import resource_filename, Requirement


__all__ = ['main']

async def send_data(uri, sample):
    async with websockets.connect(uri) as websocket:
        now = 0.0
        while True:
            max_timestamp = 0.0
            for line in sample.splitlines():
                dump = json.loads(line) 
                for i, frame in enumerate(dump["frames"]):
                    ts = dump["frames"][i]["TIMESTAMP"]
                    max_timestamp = max(max_timestamp, ts)
                    dump["frames"][i]["TIMESTAMP"] = ts + now
                await websocket.send(json.dumps(dump))
            now +=max_timestamp

def main():
    """Entry point."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verbose', action='store_true', help='be verbose')
    args = parser.parse_args()
    if args.verbose:
        print('I am verbose')

    data_path = resource_filename(Requirement.parse("epoc_harvester_simulator"), "data")
    sample_file = os.path.join(data_path, 'sample.json')
    sample = None
    with open(sample_file) as sample_file:
        sample = sample_file.read()

    asyncio.get_event_loop().run_until_complete(send_data('ws://localhost:5000/headset', sample))

if __name__ == "__main__":
    sys.exit(main())
