"""Things to remember while using pipelines
    1. Several pipes can be linked together.
    2. Items flow one by one through the entire pipeline
    3. Pipeline functionality van be packaged into callable functions."""


def separate_names(names):
    for full_name in names:
        for name in full_name.split(' '):
            yield name


def get_longest(namelist):
    full_names = (name.strip() for name in open(namelist))
    names = separate_names(full_names)
    lengths = ((name, len(name)) for name in names)
    return max(lengths, key=lambda x: x[1])
