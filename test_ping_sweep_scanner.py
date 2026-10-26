import os
import subprocess
import sys
import unittest
from unittest import mock

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import main


def fake_run(cmd, **kwargs):
    ip = cmd[-1]
    code = 0 if ip.endswith(".2") else 1
    return subprocess.CompletedProcess(cmd, code, "", "")


class TestSweep(unittest.TestCase):
    def test_sweep_lists_only_live(self):
        with mock.patch("main.subprocess.run", side_effect=fake_run):
            self.assertEqual(main.sweep("192.168.1", 1, 3), ["192.168.1.2"])

    def test_ping_missing_binary_is_not_live(self):
        with mock.patch("main.subprocess.run", side_effect=FileNotFoundError()):
            self.assertFalse(main.ping_host("192.168.1.1"))


if __name__ == "__main__":
    unittest.main()
