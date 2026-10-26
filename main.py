"""Ping sweep scanner: ping a /24 range and list live hosts (subprocess ping)."""
import argparse
import platform
import subprocess
import sys


def ping_host(ip, timeout=1):
    if platform.system() == "Windows":
        cmd = ["ping", "-n", "1", "-w", str(timeout * 1000), ip]
    else:
        cmd = ["ping", "-c", "1", "-W", str(timeout), ip]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 5)
    except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
        return False
    return result.returncode == 0


def sweep(prefix, start=1, end=254, timeout=1):
    live = []
    for i in range(start, end + 1):
        ip = f"{prefix}.{i}"
        if ping_host(ip, timeout):
            live.append(ip)
    return live


def main(argv=None):
    p = argparse.ArgumentParser(description="Ping a /24 range, e.g. prefix 192.168.1.")
    p.add_argument("--prefix", required=True, help="first three octets, e.g. 192.168.1")
    p.add_argument("--start", type=int, default=1)
    p.add_argument("--end", type=int, default=254)
    args = p.parse_args(argv)
    for ip in sweep(args.prefix, args.start, args.end):
        print(f"LIVE  {ip}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
