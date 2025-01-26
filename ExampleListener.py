# Generated from Example.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExampleParser import ExampleParser
else:
    from ExampleParser import ExampleParser

# This class defines a complete listener for a parse tree produced by ExampleParser.
class ExampleListener(ParseTreeListener):

    # Enter a parse tree produced by ExampleParser#start_.
    def enterStart_(self, ctx:ExampleParser.Start_Context):
        pass

    # Exit a parse tree produced by ExampleParser#start_.
    def exitStart_(self, ctx:ExampleParser.Start_Context):
        pass


    # Enter a parse tree produced by ExampleParser#expr.
    def enterExpr(self, ctx:ExampleParser.ExprContext):
        pass

    # Exit a parse tree produced by ExampleParser#expr.
    def exitExpr(self, ctx:ExampleParser.ExprContext):
        pass


    # Enter a parse tree produced by ExampleParser#atom.
    def enterAtom(self, ctx:ExampleParser.AtomContext):
        pass

    # Exit a parse tree produced by ExampleParser#atom.
    def exitAtom(self, ctx:ExampleParser.AtomContext):
        pass



del ExampleParser