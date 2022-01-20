/********************** ID 1952386 **********************/

grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: stmt_ClassDeclaration+ EOF;


/********************** PARSERS **********************/

// Arithmetic operators
exp_IntFloat: exp_0;
exp_0: exp_0 (ADD | SUB) exp_1 | exp_1;
exp_1: exp_1 (MUL | DIV | MOD) exp_2 | exp_2;
exp_2: ID | INTLIT | FLOATLIT | exp_MemberAccess | exp_Method | exp_Idx | LB exp_0 RB;


// Boolean operators
exp_Bool: exp_TermBool (AND | OR) exp_Bool | (NOT)? exp_TermBool;
exp_TermBool: STATIC? ID | BOOLLIT | exp_MemberAccess | LB exp_Bool RB;

// String operators
exp_Str: (exp_TermStr (SEQ | SADD) exp_Str) | exp_TermStr;
exp_TermStr: STATIC? ID | STRLIT | exp_MemberAccess | LB exp_Str RB;

//  Relational operators
exp_EqualAndNotEqual: exp_TermEQANEQ (EQ | NEQ) exp_TermEQANEQ;
exp_TermEQANEQ:
	LB expr RB
	| INTLIT
	| BOOLLIT
	| (STATIC)? ID
	| LB exp_EqualAndNotEqual RB;

exp_LessLargeEqual:
	exp_TermLRE (GT | LT | LTE | GTE) exp_TermLRE;
exp_TermLRE: LB expr RB | INTLIT | FLOATLIT | (STATIC)? ID;

exp_RelationalOperation: exp_EqualAndNotEqual | exp_LessLargeEqual;

// Index operators
exp_Idx: (exp_Method | ID) exp_TermIdx;
exp_TermIdx:
	LSB idx_Operators RSB
	| exp_TermIdx LSB idx_Operators RSB
	| exp_TermIdx LSB exp_Idx RSB;
idx_Operators: STATIC? ID | INTLIT | expr | exp_Idx | LB exp_Idx RB;


//  Member access
exp_InstanceAttributeAccess: exp_InstanceAttributeAccess DOT ID | exp_InstanceAttributeAccessTerm;
exp_InstanceAttributeAccessTerm: (LB exp_ClassObject RB | ID | SELF | exp_StaticAttributeAccess | exp_StaticMethodInvocation);


//exp_StaticAttributeAccess: (LB exp_ClassObject RB | ID) SCOPE STATIC ID;
exp_StaticAttributeAccess: ID SCOPE STATIC ID;

exp_InstanceMethodInvocation: exp_InstanceMethodInvocation DOT ID LB list_Expr RB | exp_InstanceMethodInvocationTerm;
exp_InstanceMethodInvocationTerm: (LB exp_ClassObject RB | ID | SELF | exp_StaticAttributeAccess | exp_StaticMethodInvocation);


exp_StaticMethodInvocation: ID SCOPE STATIC ID LB list_Expr RB;

exp_InstanceAttributeMethod:
	exp_InstanceAttributeMethod (DOT ID | DOT ID LB list_Expr RB)
	| exp_InstanceAttributeMethodTerm;
exp_InstanceAttributeMethodTerm: exp_InstanceAttributeAccess | exp_InstanceMethodInvocation;


exp_MemberAccess: exp_InstanceAttributeMethod | exp_StaticAttributeAccess | exp_StaticMethodInvocation;

// Object creation
exp_ObjCreation: NEW ID LB list_Expr RB | LB exp_ObjCreation RB;
exp_ClassObject: ID | exp_ObjCreation;
// Method
exp_Method: ID LB (list_Expr) RB;

// Final defination for expression
expr:
    exp_ObjCreation
	| exp_MemberAccess
	| exp_IntFloat
	| exp_Bool
	| exp_Str
	| exp_Idx
	| exp_RelationalOperation
	| datalit
	;

list_Expr: (expr (CM expr)*)?;

/********************** STATEMENTS **********************/


// Variable and Constant Declaration
type_Data: INT | FLOAT | BOOLEAN | STRING | array_Type;
array_Type: 'Array' LSB type_Data CM INTLIT RSB;
seq_ID: ID (CM ID)*;
stmt_VarDeclaration: (VAL | VAR)? (STATIC)? seq_ID COLON type_Data (
		ASSIGN list_Expr
	)? SM;

// Assignment statement
lhs: ID | expr;
stmt_Assign: lhs ASSIGN expr SM;

// If statement
stmt_If: IF LB expr RB stmt_Block* (ELSEIF LB expr RB  stmt_Block*)* (ELSE stmt_Block*)?;

// For/In statement
stmt_ForIn: FOREACH LB ID IN expr '..' expr (BY expr)? RB stmt_Block ;

// Block statement
stmt_Block: LCB (list_Stmt) RCB ;

// Method Invocation statement
stmt_MethodInvocation: (exp_InstanceMethodInvocation | exp_StaticMethodInvocation | exp_Method) SM;

// Continue statement
stmt_Continue: CONTINUE SM;

// Return statement
stmt_Return: RETURN expr? SM;

// Break statment
stmt_Break: BREAK SM;

// Final description of statement
stmt:
	stmt_VarDeclaration
	| stmt_Assign
	| stmt_If
	| stmt_ForIn
	| stmt_Block
	| stmt_MethodInvocation
| stmt_Continue | stmt_Return | stmt_Break | stmt_MethodDeclaration | stmt_Class;
list_Stmt : stmt*;

/********************** CLASSES **********************/

stmt_Class: class_Construction | class_Destruction | class_Declaration;
stmt_ClassDeclaration:
	CLASS ID (COLON ID)? LCB (
		stmt_VarDeclaration
		| stmt_MethodDeclaration
	)* RCB;
stmt_MethodDeclaration:
	STATIC? ID LB (list_Parameters)? RB stmt_Block;

class_Declaration: CLASS ID (COLON ID)? LCB list_Stmt RCB;
class_Construction: CONSTRUCTOR LB (list_Parameters)? RB  stmt_Block;
class_Destruction: DESTRUCTOR RB LB stmt_Block;


list_Parameters: seq_Parameters (SM seq_Parameters)*;
seq_Parameters: seq_ID COLON type_Data;

/********************** FRAGMENTS **********************/

fragment DIGIT: [0-9];
fragment DIGIT_19: [1-9];
fragment OCTAL_DIGIT: [0-7];
fragment LOWERCASE: [a-z];
fragment UPERCASE: [A-Z];
fragment ALPHABET: [_a-zA-Z];
fragment SCIENTIFIC: ('e' | 'E') ('-')? DIGIT+;
fragment DECIMAL_POINT: DOT (DIGIT)+;

fragment DOUBLE_QUOTE: '"';
fragment ILLEGAL_STRING: '\\' (~[bfrnt'] | '\\');
fragment QUOTE_IN_STR: '\'"';
fragment ESC_SEQ: '\\' [bfrnt'\\];
fragment VALID_STRING:
	~[\b\f\n\r\t\\"']
	| ESC_SEQ
	| QUOTE_IN_STR;

/********************** COMMENTS **********************/

BLOCK_COMMENT: '##' .*? '##' -> skip;

/********************** LITERALS **********************/

fragment OCTAL: '0' OCTAL_DIGIT ('_'? OCTAL_DIGIT)* ;
fragment BINARY: '0' ('b' | 'B') ('0' | '1') ('_'? ('0' | '1'))*;
fragment DECIMAL: (('-')? DIGIT_19 ('_'? (DIGIT))*) | '0';
fragment HEXADECIMAL: '0' ('x' | 'X')  (UPERCASE | DIGIT) ('_'? (UPERCASE | DIGIT))*;
INTLIT: (OCTAL | BINARY | DECIMAL | HEXADECIMAL) {self.text = self.text.replace('_','')};

FLOATLIT: DECIMAL (DECIMAL_POINT (SCIENTIFIC)? | SCIENTIFIC) {self.text = self.text.replace('_','')};
// 21/1/2022
BOOLLIT: TRUE | FALSE;

STRLIT: DOUBLE_QUOTE VALID_STRING* DOUBLE_QUOTE
{
	content = str(self.text)
	self.text = content[1:-1]
}
//TODO ?
;

idx_arraylit: ARRAY LB (datalit (CM datalit)*)? RB;

datalit: INTLIT | FLOATLIT | BOOLLIT | STRLIT | idx_arraylit;

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

SELF: 'Self';
STATIC: '$';

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

COLON: ':';
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

/******************** IDENTIFIERS *********************/

ID: [^a-zA-Z_][A-Za-z0-9_]*;

/********************** SKIP **********************/

WS: [ \t\r\n\f]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING:DOUBLE_QUOTE VALID_STRING*
{
        raise UncloseString(self.text[1:])
};
ILLEGAL_ESCAPE: DOUBLE_QUOTE VALID_STRING* ILLEGAL_STRING
{
		illegal_str = str(self.text)
		raise IllegalEscape(illegal_str[1:])
};

