"""Contrôles structurels simples pour respecter l'esprit du sujet."""
import ast
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "deeper"


class TestForbiddenSyntax(unittest.TestCase):
    def test_no_loops_or_comprehensions_in_exercises(self):
        forbidden = (ast.For, ast.AsyncFor, ast.While, ast.ListComp,
                     ast.SetComp, ast.DictComp, ast.GeneratorExp, ast.Break,
                     ast.Continue)
        for path in SOURCE_DIR.rglob("*.py"):
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            offenders = [node for node in ast.walk(tree) if isinstance(node, forbidden)]
            self.assertEqual(offenders, [], f"Construction interdite dans {path.relative_to(ROOT)}")

    def test_no_power_operator_in_exercises(self):
        for path in SOURCE_DIR.rglob("*.py"):
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            powers = [node for node in ast.walk(tree)
                      if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Pow)]
            self.assertEqual(powers, [], f"Opérateur ** interdit dans {path.relative_to(ROOT)}")


if __name__ == "__main__":
    unittest.main()
