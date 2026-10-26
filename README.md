# ping-sweep-scanner

Ping a /24 range (via the system `ping` command, cross-platform flags) and
list the live hosts. No invented results — a host is live only if `ping`
actually succeeds.

## How to run

```bash
python3 main.py --prefix 192.168.1 --start 1 --end 20
```

## Example output (sample from test fixture data)

```text
LIVE  192.168.1.2
```

Tests mock `subprocess.run`, so they run without network access.
Only scan networks you own or are authorised to scan.
