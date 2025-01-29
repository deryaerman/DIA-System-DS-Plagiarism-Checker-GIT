import sys
import subprocess
from antlr4 import FileStream, CommonTokenStream
from CASSLexer import CASSLexer
from CASSParser import CASSParser
from MyCASSVisitor import MyCassVisitor

def main():
    if len(sys.argv) < 2:
        print("Usage: python driver.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    # 1) Lex & parse
    input_stream = FileStream(input_file)
    lexer = CASSLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CASSParser(token_stream)

    parse_tree = parser.prog()  # or whatever your top rule is

    # 2) Transform to CASS
    visitor = MyCassVisitor()
    cass_root = visitor.visit(parse_tree)
    count = cass_root.get_node_count()

    # 3) Print or visualize
    print("=== CASS String ===")
    print(f"{count}\\t" + cass_root.to_cass_string())

    # 4) Create DOT & PNG
    dot_lines = cass_root.to_dot()  # Call to_dot() without extra arguments
    with open("cass.dot", "w") as f:
        f.write("\n".join(dot_lines))

    subprocess.run(["dot", "-Tpng", "cass.dot", "-o", "cass.png"], check=True)
    print("PNG saved as cass.png")

if __name__ == "__main__":
    main()
