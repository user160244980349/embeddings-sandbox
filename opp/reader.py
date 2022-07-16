import csv
import json
import os
import re

from pprint import pprint
from config import datasets, resources
from tools.fsys import files
from tools.text import remove_html, remove_spec_chars, remove_spaces, \
    remove_newlines_completely, remove_dashes, remove_urls, remove_digits


def clear_segment(text):
    segment_text = remove_newlines_completely(text)
    segment_text = remove_urls(segment_text)
    segment_text = remove_html(segment_text)
    segment_text = remove_digits(segment_text)
    segment_text = remove_dashes(segment_text)
    segment_text = remove_spec_chars(segment_text)
    segment_text = remove_spaces(segment_text)
    return segment_text.lower().strip()


def construct_annotations(reader, segments):
    return [
        {
            "category": row[5].strip(),
            "segment_text": segments[int(row[4])].strip(),
            "attributes": json.loads(row[6])
        }
        for row in reader
    ]


def construct_data(sanitized, annotated):
    id1 = re.match(r"^.*/(\d+)_.*$", sanitized).group(1)
    id2 = re.match(r"^.*/(\d+)_.*$", annotated).group(1)
    if id1 != id2:
        raise Exception(f"Ids of a files couple are not equal! {id1} != {id2}")

    name = re.match(r"^.*\d+_(.*)\.csv$", annotated).group(1)

    with open(sanitized) as f:
        segments_texts = [clear_segment(s) for s in f.read().split("|||")]

    with open(annotated, mode="r") as f:
        reader = csv.reader(f)
        annotations_records = construct_annotations(reader, segments_texts)

    return {
        "id": id1,
        "name": name,
        "annotations": annotations_records
    }


def read_opp():
    sanitized = files(os.path.join(datasets, "OPP-115/sanitized_policies"), r"(\d+)_.*")
    annotations = files(os.path.join(datasets, "OPP-115/consolidation/threshold-0.75"
                                               "-overlap-similarity"), r"(\d+)_.*")

    sanitized.sort()
    annotations.sort()

    couples = list(zip(sanitized, annotations))

    return [construct_data(*c) for c in couples]


def prepare_data():
    sanitized = files(os.path.join(datasets, "OPP-115/sanitized_policies"), r"(\d+)_.*")
    segments_texts = []

    for s in sanitized:
        with open(s, "r") as f:
            segments_texts.extend([clear_segment(s) for s in f.read().split("|||")])

    with open(os.path.join(resources, "opp115"), "w") as f:
        f.write(" ".join(segments_texts))
