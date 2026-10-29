"""Tests publics d'entraînement dérivés des exemples du sujet."""
import unittest

from deeper.descent.depth_gauge import depth_sum
from deeper.descent.oxygen import oxygen
from deeper.descent.signal import signal_power
from deeper.descent.echoes import echo
from deeper.descent.beacon import countdown_beacon
from deeper.core.layers import layer_sum
from deeper.core.deepest import deepest_digit
from deeper.core.gates import gate_gcd
from deeper.core.binary import to_binary
from deeper.core.abyss import ackermann
from deeper.core.tower import hanoi


class TestDescent(unittest.TestCase):
    def test_depth_sum_examples(self):
        self.assertEqual(depth_sum(5), 15)
        self.assertEqual(depth_sum(0), 0)
        self.assertEqual(depth_sum(10), 55)
        self.assertEqual(depth_sum(3), 6)

    def test_oxygen_examples(self):
        self.assertEqual(oxygen(5), 120)
        self.assertEqual(oxygen(0), 1)
        self.assertEqual(oxygen(7), 5040)

    def test_signal_power_examples(self):
        self.assertEqual(signal_power(2, 3), 8)
        self.assertEqual(signal_power(-2, 3), -8)
        self.assertEqual(signal_power(-2, 4), 16)
        self.assertEqual(signal_power(-2, -3), -0.125)
        self.assertEqual(signal_power(5, 0), 1)

    def test_echo_examples(self):
        self.assertEqual(echo(3), 2)
        self.assertEqual(echo(10), 55)
        self.assertEqual(echo(13), 233)

    def test_beacon_examples(self):
        self.assertEqual(countdown_beacon(3), "3,2,1,0")
        self.assertEqual(countdown_beacon(0), "0")
        self.assertEqual(countdown_beacon(5), "5,4,3,2,1,0")

    def test_invalid_depth_sum(self):
        with self.assertRaises(ValueError):
            depth_sum(-1)

    def test_invalid_oxygen(self):
        with self.assertRaises(ValueError):
            oxygen(-3)

    def test_invalid_echo(self):
        with self.assertRaises(ValueError):
            echo(-7)

    def test_invalid_beacon(self):
        with self.assertRaises(ValueError):
            countdown_beacon(-1)

    def test_invalid_signal_power(self):
        with self.assertRaises(ValueError):
            signal_power(0, 0)


class TestCore(unittest.TestCase):
    def test_digit_examples(self):
        self.assertEqual(layer_sum(123), 6)
        self.assertEqual(layer_sum(0), 0)
        self.assertEqual(layer_sum(-456), 15)
        self.assertEqual(layer_sum(9999), 36)
        self.assertEqual(deepest_digit(132), 3)
        self.assertEqual(deepest_digit(0), 0)
        self.assertEqual(deepest_digit(-456), 6)
        self.assertEqual(deepest_digit(9999), 9)

    def test_gcd_examples(self):
        self.assertEqual(gate_gcd(48, 18), 6)
        self.assertEqual(gate_gcd(7, 13), 1)
        self.assertEqual(gate_gcd(-24, 36), 12)
        self.assertEqual(gate_gcd(100, 50), 50)

    def test_binary_examples(self):
        self.assertEqual(to_binary(4), "100")
        self.assertEqual(to_binary(10), "1010")
        self.assertEqual(to_binary(0), "0")
        self.assertEqual(to_binary(255), "11111111")

    def test_ackermann_examples(self):
        self.assertEqual(ackermann(0, 5), 6)
        self.assertEqual(ackermann(1, 2), 4)
        self.assertEqual(ackermann(2, 3), 9)

    def test_invalid_binary(self):
        with self.assertRaises(ValueError):
            to_binary(-1)

    def test_invalid_ackermann_negative_m(self):
        with self.assertRaises(ValueError):
            ackermann(-1, 2)

    def test_invalid_ackermann_negative_n(self):
        with self.assertRaises(ValueError):
            ackermann(1, -2)

    def test_hanoi_output(self):
        from contextlib import redirect_stdout
        from io import StringIO

        output = StringIO()
        with redirect_stdout(output):
            self.assertIsNone(hanoi(2, "A", "C", "B"))
        self.assertEqual(output.getvalue(),
                         "disk 1: A -> B\ndisk 2: A -> C\ndisk 1: B -> C\n")

        output = StringIO()
        with redirect_stdout(output):
            with self.assertRaises(ValueError):
                hanoi(-1, "A", "C", "B")
        self.assertEqual(output.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
