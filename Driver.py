import sys
from antlr4 import *
from ExampleLexer import ExampleLexer
from ExampleParser import ExampleParser
from antlr4.tree.Trees import Trees


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = ExampleLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExampleParser(stream)
    tree = parser.start_()

    #with open('output.txt', 'w') as f:
      #  f.write(tree.toStringTree(recog=parser))

    print(Trees.toStringTree(tree, None, parser))

if __name__ == '__main__':
    main(sys.argv)