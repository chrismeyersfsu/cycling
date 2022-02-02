#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import sys
import datetime
import codecs
import glob
from pathlib import Path


def transform_name_to_time(fname):
    fpath = Path(fname)

    ET.register_namespace('', "http://www.topografix.com/GPX/1/1")
    tree = ET.parse(str(fpath))
    root = tree.getroot()

    first_time_number = None
    epoch = datetime.datetime.now() - datetime.timedelta(days=10)

    metadata = root.find('.//{*}metadata')
    root.remove(metadata)

    for parent in root.findall('.//{*}trkpt'):
        e = parent.find('.//{*}name')
        print(f"{e.tag}, {e.attrib}, {e.text}")
        e.tag = 'time'
        print(e.text)
        if not first_time_number:
            first_time_number = int(e.text)

        time_number = int(e.text)
        time_number_normalized = time_number - first_time_number

        ts = epoch + datetime.timedelta(seconds=(time_number_normalized*5))
        e.text = str(ts.replace(tzinfo=datetime.timezone.utc).isoformat(timespec='milliseconds'))

        child = ET.Element("NewNode")
        child.tag = 'ele'
        child.text = '12'
        parent.append(child)

        parent.remove(e)
        parent.append(e)

    new_fpath = Path(fpath.parent).joinpath(f"{fpath.stem}_rlv_ready{fpath.suffix}")
    with open(new_fpath, 'wb') as f:
        xml_serialized = ET.tostring(root, encoding='utf-8', xml_declaration=True)
        f.write(codecs.BOM_UTF8)
        f.write(xml_serialized)


def gpx_iterator(dir):
    fpath = Path(dir)
    for e in glob.iglob(f"{str(fpath)}/*.gpx"):
        if e.endswith('rlv_ready.gpx'):
            continue
        yield e

def run(path):
    """
    Given a directory. Find all *.gpx files that aren't *rlv_ready.gpx and convert them to <file>_rlv_ready.gpx
    Basically, just convert the <name><name> to <time></time> and add an elevation tag <ele></ele>.

    Note: Order matters with tags <ele></ele> MUST come before <time></time> for rlv studio to be satisfied.
    """
    for e in gpx_iterator(path):
        transform_name_to_time(e)

run(sys.argv[1])
