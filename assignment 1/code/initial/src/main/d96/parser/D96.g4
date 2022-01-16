grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: mptype 'main' LB RB LCB body? RCB EOF;

mptype: INTTYPE | VOIDTYPE | CLASS;

body: funcall SM;

exp: funcall | INTLIT;

funcall: ID LB exp? RB;

INTTYPE: 'int';

VOIDTYPE: 'void';

/********************** FRAGMENTS **********************/

fragment DIGIT: [_0-9];
fragment LOWERCASE: [a-z];
fragment UPERCASE: [A-Z];
fragment ALPHABET: [_a-zA-Z];
fragment SCIENTIFIC: ('e' | 'E') ('-')? DIGIT+;
fragment DECIMAL_POINT: DOT (DIGIT)+;

fragment DOUBLE_QUOTE: '"';

fragment STRING_LITERAL: ~[\b\t\f\r\n'\\] | ESCAPE_SEQUENCE;
fragment ESCAPE_SEQUENCE:
	'\\' ('b' | 'f' | 'r' | 'n' | 't' | '\'' | '\\');
fragment ILLEGAL_STRING: '\\' (~[bfrnt'] | '\\');

/********************** COMMENTS **********************/
BLOCK_COMMENT: '##' .*? '##' -> skip;

/********************** LITERALS **********************/

fragment OCTAL: '0' DIGIT+;
fragment BINARY: '0' ('b' | 'B') ('0' | '1')+;
fragment DECIMAL: ('-')? DIGIT+;
fragment HEXADECIMAL: '0' ('x' | 'X') (UPERCASE | DIGIT)+;
INTLIT:
	OCTAL
	| BINARY
	| DECIMAL
	| HEXADECIMAL {self.text = self.text.replace('_','')};

FLOATLIT: ('-')? (DIGIT)+ (
		DECIMAL_POINT (SCIENTIFIC)?
		| SCIENTIFIC
	);

BOOLIT: TRUE | FALSE;

STRLIT:
	DOUBLE_QUOTE STRING_LITERAL* DOUBLE_QUOTE {
	content = str(self.text)
	self.text = content[1:-1]
};

IDX_ARRAY: ARRAY LB (DATALIT (CM DATALIT)*)? RB;

DATALIT: INTLIT | FLOATLIT | BOOLIT | STRLIT | IDX_ARRAY;

/******************** IDENTIFIERS *********************/

ID: ALPHABET (ALPHABET | DIGIT)*;

/********************** KEYWORDS **********************/

BREAK: 'Break';
CONTINUE: 'Continue';
IF: 'If';
ELSEIF: 'Elseif';
ELSE: 'Else';
FOREACH: 'Foreach';
TRUE: 'True';
FALSE: 'False';
ARRAY: 'Array';
IN: 'In';
INT: 'Int';
FLOAT: 'Float';
BOOLEAN: 'Boolean';
STRING: 'String';
RETURN: 'Return';
NULL: 'Null';
CLASS: 'Class';
VAL: 'Val';
VAR: 'Var';
CONSTRUCTOR: 'Constructor';
DESTRUCTOR: 'Destructor';
NEW: 'New';
BY: 'By';

/********************** OPERATORS **********************/

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQ: '==';
NEQ: '!=';
GT: '>';
GTE: '>=';
LT: '<';
LTE: '<=';

SADD: '+.';
SEQ: '==.';

NOT: '!';
AND: '&&';
OR: '||';

ASSIGN: '=';
SCOPE: '::';

/********************** SEPARATORS **********************/

LB: '(';
RB: ')';
LSB: '[';
RSB: ']';
LCB: '{';
RCB: '}';
SM: ';';
CM: ',';
DOT: '.';

/********************** SKIP **********************/

WS: [ \t\r\n\f]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING:
	DOUBLE_QUOTE STRING_LITERAL* ([\b\t\f\n\r"\\] | EOF) {
        unclose_str = str(self.text)
        possible = ['\b', '\t', '\f', '\n', '\r', '"', '\\']
        if unclose_str[-1] in possible:
            raise UncloseString(unclose_str[1:-1])
        else:
            raise UncloseString(unclose_str[1:])
    };
ILLEGAL_ESCAPE:
	DOUBLE_QUOTE STRING_LITERAL* ILLEGAL_STRING {	
		illegal_str = str(self.text)
		raise IllegalEscape(illegal_str[1:])
	};

