# analyzer.py
import ast

class CodeAnalyzer:
    def __init__(self, code_str):
        try:
            self.tree = ast.parse(code_str)
        except SyntaxError as e:
            print(f"Erro de sintaxe ao analisar o código: {e}")
            self.tree = None

    def extract_functions(self):
        if not self.tree:
            return []
        return [
            node for node in ast.walk(self.tree)
            if isinstance(node, ast.FunctionDef)
        ]
