import json
import os

from config import resources
from opp.reader import read_opp


def reason_attributes(policies, category):
    result = []
    for p in policies:
        for a in p["annotations"]:
            if a["category"] == category:
                result.extend(list(a["attributes"].keys()))
    return list(set(result))


def reason_values(policies, category, attribute):
    result = []
    for p in policies:
        for a in p["annotations"]:
            if a["category"] == category:
                try:
                    result.append(a["attributes"][attribute]["value"])
                except KeyError:
                    pass
    return list(set(result))


def main():
    policies = read_opp()

    categories = list(set([a["category"] for p in policies for a in p["annotations"]]))
    categories_attributes = {c: reason_attributes(policies, c) for c in categories}
    structure = {c: {a: reason_values(policies, c, a) for a in categories_attributes[c]} for c in categories_attributes.keys()}

    with open(os.path.join(resources, "opp_structure.json"), "w") as f:
        json.dump(structure, f, indent=8)


if __name__ == "__main__":
    main()
