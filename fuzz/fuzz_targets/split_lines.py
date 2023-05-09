#!/usr/bin/env python3

import atheris
import sys

with atheris.instrument_imports():
    from parso import split_lines

def TestOneInput(input):
    fdp = atheris.FuzzedDataProvider(input)
    split_lines(fdp.ConsumeUnicodeNoSurrogates(fdp.ConsumeIntInRange(1, 4096)))

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
