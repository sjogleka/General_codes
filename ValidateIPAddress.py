from ipaddress import ip_address, IPv6Address
class Solution:
    def validIPAddress(self, IP: str) -> str:
        try:
            return "IPv6" if type(ip_address(IP)) is IPv6Address else "IPv4"
        except ValueError:
            return "Neither"


import re

IP4 = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
IP6 = re.compile(r"([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}\s*)(?!.)")


def ip4(s):
    val = re.match(IP4, s)
    if val is None:
        return False

    for num in s.split("."):
        if int(num) > 256:
            return False
    return True


def ip6(s):
    val = re.match(IP6, s)
    if val is None:
        return False
    return True


def main():
    lines = ['121.18.19.20','0.12.12.34','121.234.12.12','23.45.12.56','0.1.2.3','1:22:333:4444']

    for line in lines:
        if ip4(line.strip()):
            print("IPv4")
        elif ip6(line):
            print("IPv6")
        else:
            print("Neither")


if __name__ == "__main__":
    main()
