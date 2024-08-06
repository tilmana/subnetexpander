import ipaddress
import argparse

parser = argparse.ArgumentParser(description="Get IPs from one or more subnets passed via an argument directly or read from a file.")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-s', '--subnet', help='Subnet to pass directly')
group.add_argument('-f', '--file', help='File to read subnet(s) from')

args = parser.parse_args()

if args.subnet:
    subnet = args.subnet
    ips = [str(ip) for ip in ipaddress.IPv4Network(subnet)]
    for ip in ips:
        print(ip)

if args.file:
    subnets = []
    f1 = open(args.file, "r")
    f1lines = f1.readlines()
    for line in f1lines:
        subnets.append(line.strip("\n"))
    for subnet in subnets:
        ips = [str(ip) for ip in ipaddress.IPv4Network(subnet)]
        for ip in ips:
            print(ip)
