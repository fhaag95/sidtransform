#!/usr/bin/python3
import struct
import binascii
import sys

def format_struct_data(data):
        return binascii.b2a_hex(data).decode("utf-8")

def transform(sid):
        sidhex = ""
        numDashes = sid.count("-") - 1
        parts = sid.split("-")

        # revision
        sidhex += format_struct_data(struct.pack(">B", int(parts[1])))
        # number of dashes minus one (needs to be minus two if user SID is supplied)
        sidhex += format_struct_data(struct.pack(">B", numDashes))

        sidhex += "{0:012x}".format(int(parts[2]))


        for i in parts[3:]:
                sidhex += format_struct_data(struct.pack("<I", int(i)))

        print("SID: {}".format(sid))
        print("SID in HEX: {}".format(sidhex.upper()))

if __name__ == "__main__":
        if len(sys.argv) < 2:
                print("Usage: sidtransform.py <SID string>")
                sys.exit()

        transform(sys.argv[1])
