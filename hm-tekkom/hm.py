import hm_lexer
import hm_parser
import hm_interp

from sys import *

#DENGAN MASUKAN EKSTENSI .HM
lexer = hm_lexer.BasicLexer()
parser = hm_parser.BasicParser()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    hm_interp.BasicExecute(tree, env)
