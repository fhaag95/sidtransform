# SID Transform
This repo contains a small script that can be used to transform a domain SID into its hex representation. 

Given an example SID of *S-1-5-21-237813920-1760564327-87643179* the tool transforms this SID into its hex representation *010500000000000515000000A0C02C0E6714F0682B543905*

The script expects a domain SID, **not** an user SID. 

Transformations are done according to: https://devblogs.microsoft.com/oldnewthing/20040315-00/?p=40253

## Usage

```sidtransform.py <SID string>```
