#!/usr/bin/env python3
import ast
import argparse
import sys

def list_defs(source_path):
    """
    Parse the Python file at source_path and yield (name, lineno) for every def.
    """
    with open(source_path, 'r', encoding='utf-8') as f:
        tree = ast.parse(f.read(), filename=source_path)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            yield node.name, node.lineno

def main():
    parser = argparse.ArgumentParser(
        description="List all function definitions in a Python file."
    )
    parser.add_argument(
        "source",
        help="Path to the .py file to scan"
    )
    parser.add_argument(
        "-n", "--no-lineno",
        action="store_true",
        help="Omit line numbers"
    )
    args = parser.parse_args()

    try:
        for name, lineno in list_defs(args.source):
            if args.no_lineno:
                print(name)
            else:
                print(f"{name}  (line {lineno})")
    except FileNotFoundError:
        sys.exit(f"Error: file not found: {args.source}")
    except SyntaxError as e:
        sys.exit(f"Syntax error in {args.source}: {e}")

if __name__ == "__main__":
    main()
