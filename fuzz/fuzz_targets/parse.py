#!/usr/bin/env python3

import atheris
import sys

with atheris.instrument_imports():
    from parso import parse, load_grammar

def TestOneInput(input):
    fdp = atheris.FuzzedDataProvider(input)
    node = parse(fdp.ConsumeUnicodeNoSurrogates(fdp.ConsumeIntInRange(1, 4096)))
    [issue for issue in load_grammar().iter_errors(node)]


def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
