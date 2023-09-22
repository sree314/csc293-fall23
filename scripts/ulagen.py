#!/usr/bin/python3
#
# ulagen.py
#
# Generates a ULA host address given a network prefix
#

import argparse
import ipaddress
import random

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Generate a IPv6 ULA host address given a network prefix")
    p.add_argument("network", help="IPv6 Network in addr/prefixlen form (including subnet), e.g. fd00::1/64")
    p.add_argument("--minrange", help="Minimum range for host address", type=int, default=256)

    args= p.parse_args()

    net = ipaddress.IPv6Network(args.network)
    assert net.prefixlen >= 64, "Prefix cannot be less than 64"
    hostrange = 128 - net.prefixlen
    host = random.randint(args.minrange, 2**hostrange) # skip the first 256, for legacy reasons
    print(str(net[host])+"/"+str(net.prefixlen))
