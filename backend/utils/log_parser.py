import re
import json
import csv
from typing import List, Dict


def detect_and_parse(path: str) -> List[Dict]:
    lines = open(path, 'r').read().splitlines()
    if lines and 'HTTP/' in lines[0]:
        return parse_apache(lines)
    if lines and lines[0].strip().startswith('{'):
        return parse_json(lines)
    return parse_tsv(lines)


def parse_apache(lines):
    pattern = re.compile(r"(?P<ip>\S+) - - \[(?P<time>.+?)\] \"(?P<method>\S+) (?P<url>\S+)\S* \S+\" (?P<status>\d{3})")
    records = []
    for line in lines:
        m = pattern.search(line)
        if m:
            records.append({
                'timestamp': m.group('time'),
                'ip': m.group('ip'),
                'method': m.group('method'),
                'url': m.group('url'),
                'status': int(m.group('status')),
                'raw_log': line
            })
    return records


def parse_json(lines):
    records = []
    for line in lines:
        try:
            obj = json.loads(line)
            records.append({
                'timestamp': obj.get('ts'),
                'ip': obj.get('id.orig_h'),
                'method': obj.get('method'),
                'url': obj.get('uri'),
                'status': obj.get('status_code'),
                'raw_log': line
            })
        except json.JSONDecodeError:
            continue
    return records


def parse_tsv(lines):
    reader = csv.DictReader(lines, delimiter='\t')
    records = []
    for obj in reader:
        records.append({
            'timestamp': obj.get('ts'),
            'ip': obj.get('src'),
            'method': obj.get('method'),
            'url': obj.get('path'),
            'status': int(obj.get('status', 0)),
            'raw_log': '\t'.join(obj.values())
        })
    return records