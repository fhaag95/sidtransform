#!/usr/bin/python3
import struct, binascii, sys, click

def format_struct_data(data):
        return binascii.b2a_hex(data).decode("utf-8")

def transform(sid, dashReduction):
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

        return sidhex
        

@click.command()
@click.option("--sid-type", type=click.Choice(["domain", "user"]), required=True, help="Specifies whether a domain SID or a user SID is supplied.")
@click.argument("sid", )
def start(sid_type, sid):
        sid_hex = ""
        if sid_type.lower() == "domain":
                sid_hex = transform(sid, 1)
        else:
                sid_hex = transform(sid, 2)

        print("SID: {}".format(sid))
        print("SID in HEX: {}".format(sid_hex.upper()))

if __name__ == "__main__":
        start()
