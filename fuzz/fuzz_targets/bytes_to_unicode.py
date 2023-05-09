#!/usr/bin/env python3

import atheris
import sys

with atheris.instrument_imports():
    from parso import python_bytes_to_unicode

def TestOneInput(input):
    fdp = atheris.FuzzedDataProvider(input)
    try:
        python_bytes_to_unicode(fdp.ConsumeBytes(fdp.ConsumeIntInRange(1, 4096)))
    except UnicodeDecodeError:
        return

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
