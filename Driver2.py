import sys
import subprocess
from antlr4 import *
from antlr4.tree.Tree import ParseTree, TerminalNode
from CASSLexer import CASSLexer
from CASSParser import CASSParser
from MyCASSVisitor import MyCassVisitor

node_counter = 0

def walk_tree(node, parser, dot_lines, parent_id=None):
    """
    Recursively walk the parse tree to build up DOT lines.
    """
    global node_counter
    node_id = node_counter
    node_counter += 1

    # Determine node label
    if isinstance(node, TerminalNode):
        # Terminal node (tokens)
        token_text = node.getText()
        label = token_text.replace('"', '\\"')
    else:
        # Non-terminal node (rules)
        rule_index = node.getRuleIndex()
        rule_name = parser.ruleNames[rule_index]
        label = rule_name

    # Create the DOT node line
    dot_lines.append(f'  node{node_id} [label="{label}"];')

    # If there is a parent, create an edge
    if parent_id is not None:
        dot_lines.append(f'  node{parent_id} -> node{node_id};')

    # Recurse on children
    child_count = node.getChildCount()
    for i in range(child_count):
        child = node.getChild(i)
        walk_tree(child, parser, dot_lines, node_id)

def generate_dot_file(tree, parser, output_dot):
    """
    Generate a DOT file for the given parse tree and parser.
    """
    global node_counter
    node_counter = 0

    dot_lines = ["digraph ParseTree {", "  rankdir=TB;"]
    walk_tree(tree, parser, dot_lines)
    dot_lines.append("}")

    with open(output_dot, "w", encoding="utf-8") as f:
        f.write("\n".join(dot_lines))

def main(file_path):
    # 1) Create the lexer, parser, and parse tree
    input_stream = FileStream(file_path, encoding="utf-8")
    lexer = CASSLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CASSParser(token_stream)

    # 2) Parse the file
    tree = parser.prog()

    # 3) Generate a DOT file
    output_dot = "parse_tree.dot"
    generate_dot_file(tree, parser, output_dot)

    # 4) Call GraphViz to render it as a PNG
    subprocess.run(["dot", "-Tpng", output_dot, "-o", "parse_tree.png"], check=True)

    print("Parse tree DOT file: parse_tree.dot")
    print("Parse tree image: parse_tree.png")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python parse_and_visualize.py <python_file_to_parse>")
        sys.exit(1)
    main(sys.argv[1])
