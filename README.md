# SID Transform
This repo contains a small script that can be used to transform a SID into its hex representation. 

Given an example domain SID of *S-1-5-21-237813920-1760564327-87643179* the tool transforms this SID into its hex representation *010500000000000515000000A0C02C0E6714F0682B543905*

The script is able to perform the transformation on domain SIDs and user SIDs.

Transformations are done according to: https://devblogs.microsoft.com/oldnewthing/20040315-00/?p=40253

## Usage

```
Usage: sidtransform.py [OPTIONS] SID

Options:
  --sid-type [domain|user]  Specifies whether a domain SID or a user SID is
                            supplied.  [required]
  --help                    Show this message and exit.
```
