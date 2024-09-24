#!/usr/bin/env python3

import re
from collections import Counter

def syslog_analysis():
    err = r'\berror\b'
    warn = r'\bwarning\b'

    path = "/var/log/syslog"

    errors = []
    warnings = []

    with open(path, 'r') as file:
        for line in file:
            if re.search(err, line, re.IGNORECASE):
                errors.append(line.strip())
            if re.search(warn, line, re.IGNORECASE):
                warnings.append(line.strip())

    return errors, warnings

def report(errors, warnings):
    err_counter = len(errors)
    warn_counter = len(warnings)

    most_common = Counter(errors + warnings).most_common(5)

    return err_counter, warn_counter, most_common

def main():
    errors, warnings = syslog_analysis()
    err_counter, warn_counter, most_common = report(errors, warnings)

    print("Script successfully analyzed '/var/log/syslog' file.")
    print("====================================================\n")
    print(f"Errors: {err_counter}\nWarnings: {warn_counter}\n")
    print("The most common errors and warnings are:\n")

    for err_warn, count in most_common:
        print(f"{err_warn} - {count} times\n")

if __name__ == "__main__":
    main()
