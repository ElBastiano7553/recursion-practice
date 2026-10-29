"""Vérifie quelques constructions interdites dans les fichiers de l'exercice."""
import ast
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
SOURCE_DIR = ROOT / "deeper"
FORBIDDEN_NODES = (
    ast.For,
    ast.AsyncFor,
    ast.While,
    ast.ListComp,
    ast.SetComp,
    ast.DictComp,
    ast.GeneratorExp,
    ast.Break,
    ast.Continue,
)

def main() -> int:
    failed = False
    for path in sorted(SOURCE_DIR.rglob("*.py")):
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except (OSError, SyntaxError) as exc:
            print(f"ERREUR {path.relative_to(ROOT)}: {exc}")
            failed = True
            continue
        for node in ast.walk(tree):
            relative = path.relative_to(ROOT)
            if isinstance(node, FORBIDDEN_NODES):
                print(f"Interdit {relative}:{getattr(node, 'lineno', '?')} — {type(node).__name__}")
                failed = True
            if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Pow):
                print(f"Interdit {relative}:{node.lineno} — opérateur **")
                failed = True
    if failed:
        return 1
    print("OK : pas de boucle, compréhension, break/continue ou opérateur ** détecté dans deeper/.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
