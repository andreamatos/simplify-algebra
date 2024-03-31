import json
from sympy import simplify
from sympy.parsing.sympy_parser import parse_expr


def simplify_expression(expression):
    try:
        expr = parse_expr(expression)
        simplified_expr = simplify(expr)
        return simplified_expr
    except Exception as e:
        return f"Error: {e}"


def main():
    with open("expressions.json") as file:
        data = json.load(file)
        expressions = data["expressions"]

    for index, expression in enumerate(expressions, start=1):
        print(f"Expression {index}: {expression}")
        simplified_expression = simplify_expression(expression)
        print("Simplified expression:", simplified_expression)
        print()


if __name__ == "__main__":
    main()
