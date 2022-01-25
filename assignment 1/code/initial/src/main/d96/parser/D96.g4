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
exp_2: SUB exp_2 | exp_3;
exp_3: ID | ZERO | INTLIT | FLOATLIT | exp_MemberAccess | exp_Method | exp_Idx | LB exp_0 RB;


// Boolean operators
exp_Logical: exp_LogicalTerm (AND | OR) exp_Logical;
exp_LogicalTerm: (STATIC_ID | ID) | BOOLLIT | exp_MemberAccess | LB exp_LogicalTerm RB;


exp_LogicalNot: NOT exp_LogicalNot | exp_LogicalNotTerm;
exp_LogicalNotTerm: (STATIC_ID | ID) | BOOLLIT | exp_MemberAccess | LB exp_LogicalNotTerm RB ;

exp_Bool: exp_Logical | exp_LogicalNot;

// String operators
exp_Str: (exp_TermStr (SEQ | SADD) exp_Str) | exp_TermStr;
exp_TermStr: (STATIC_ID | ID) | STRLIT | exp_MemberAccess | LB exp_Str RB;

//  Relational operators
exp_EqualAndNotEqual: exp_TermEQANEQ (EQ | NEQ) exp_TermEQANEQ;
exp_TermEQANEQ:
	LB expr RB
	| ZERO
	| INTLIT
	| BOOLLIT
	| (STATIC_ID | ID)
	| LB exp_EqualAndNotEqual RB;

exp_LessLargeEqual:
	exp_TermLRE (GT | LT | LTE | GTE) exp_TermLRE;
exp_TermLRE: LB expr RB | ZERO | INTLIT | FLOATLIT | (STATIC_ID | ID);

exp_RelationalOperation: exp_EqualAndNotEqual | exp_LessLargeEqual;

// Index operators
exp_Idx: (exp_Method | ID) exp_TermIdx;
exp_TermIdx:
	LSB idx_Operators RSB
	| exp_TermIdx LSB idx_Operators RSB
	| exp_TermIdx LSB exp_Idx RSB;
idx_Operators: (STATIC_ID | ID) | ZERO | INTLIT | expr | exp_Idx | LB exp_Idx RB;


//  Member access
exp_InstanceAttributeAccess: exp_InstanceAttributeAccess DOT ID | exp_InstanceAttributeAccessTerm;
exp_InstanceAttributeAccessTerm: exp_ClassObject | ID | SELF | exp_StaticAttributeAccess | exp_StaticMethodInvocation;



exp_StaticAttributeAccess: ID SCOPE STATIC_ID;

exp_InstanceMethodInvocation: exp_InstanceMethodInvocation DOT ID LB list_Expr? RB | exp_InstanceMethodInvocationTerm;
exp_InstanceMethodInvocationTerm: exp_ClassObject | ID | SELF | exp_StaticAttributeAccess | exp_StaticMethodInvocation;


exp_StaticMethodInvocation: ID SCOPE STATIC_ID LB list_Expr? RB;

exp_InstanceAttributeMethod: exp_InstanceAttributeMethod (DOT ID | DOT ID LB list_Expr? RB) | exp_InstanceAttributeMethodTerm;
exp_InstanceAttributeMethodTerm: exp_InstanceAttributeAccess | exp_InstanceMethodInvocation;


//exp_MemberAccess: exp_InstanceAttributeMethod | exp_StaticAttributeAccess | exp_StaticMethodInvocation;
exp_MemberAccess: exp_StaticMethodInvocation |exp_StaticAttributeAccess | exp_InstanceAttributeMethod;

// Object creation
exp_ObjCreation: NEW ID LB list_Expr? RB | LB exp_ObjCreation RB;
exp_ClassObject: ID | exp_ObjCreation;
// Method
exp_Method: ID LB list_Expr? RB;

// Final defination for expression
expr:
    exp_ObjCreation
	| exp_MemberAccess
	| exp_IntFloat
	| exp_Bool
	| exp_Str
	| exp_Idx
	| exp_RelationalOperation
	| lit_Data
	;

list_Expr: expr (CM expr)*;

/********************** STATEMENTS **********************/

// Variable and Constant Declaration
type_Data: INT | FLOAT | BOOLEAN | STRING | array_Type;
array_Type: ARRAY LSB type_Data CM INTLIT RSB;
seq_ID: (STATIC_ID | ID) (CM (STATIC_ID | ID))*;
list_Attribute: (STATIC_ID | ID) list_AttributeTerm expr | seq_ID COLON type_Data;
list_AttributeTerm: CM (STATIC_ID | ID) list_AttributeTerm expr CM | COLON type_Data ASSIGN;
stmt_AttributeDeclaration: (VAL | VAR)? list_Attribute SM;

//stmt_VarDeclaration: (VAL | VAR)? seq_ID COLON type_Data (ASSIGN list_Expr)? SM;


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
	stmt_AttributeDeclaration
	| stmt_Assign
	| stmt_If
	| stmt_ForIn
	| stmt_Block
	| stmt_MethodInvocation
	| stmt_Continue | stmt_Return | stmt_Break | stmt_MethodDeclaration | stmt_ClassMethod;
list_Stmt : stmt*;

/********************** CLASSES **********************/

stmt_ClassMethod: class_Construction | class_Destruction;
stmt_ClassDeclaration: CLASS ID (COLON ID)? LCB (stmt_AttributeDeclaration | stmt_MethodDeclaration | stmt_ClassMethod)* RCB;
stmt_MethodDeclaration: (STATIC_ID | ID) LB (list_Parameters)? RB stmt_Block;

//class_Declaration: CLASS ID (COLON ID)? LCB list_Stmt RCB;
class_Construction: CONSTRUCTOR LB (list_Parameters)? RB  stmt_Block;
class_Destruction: DESTRUCTOR LB RB stmt_Block;


list_Parameters: seq_Parameters (SM seq_Parameters)*;
seq_Parameters: seq_ID COLON type_Data;

/********************** RULES **********************/

lit_Array: ARRAY LB (lit_Data (CM lit_Data)*)? RB;

lit_Data: ZERO | INTLIT | FLOATLIT | BOOLLIT | STRLIT | lit_Array;
BOOLLIT: TRUE | FALSE;
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
fragment STATIC: '$';
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

/********************** FRAGMENTS **********************/

fragment DIGIT: [0-9];
fragment DIGIT_01: [0-1];
fragment DIGIT_07: [0-7];
fragment DIGIT_17: [1-7];
fragment DIGIT_19: [1-9];
fragment LOWERCASE: [a-z];
fragment UPERCASE: [A-Z];
fragment UPERCASE_AF: [A-F];
fragment ALPHABET: [_a-zA-Z];
fragment SCIENTIFIC: ('e' | 'E') ('-')? DIGIT+;
fragment DECIMAL_POINT: DOT DIGIT*;

DOUBLE_QUOTE: '"';
fragment ILLEGAL_STRING: '\\' ~[bfrnt'\\];

fragment QUOTE_IN_STR: '\'"';
fragment ESC_SEQ: '\\' [bfrnt'\\];
fragment VALID_STRING:
	~[\b\f\r\n\t\\"]
	| ESC_SEQ
	| QUOTE_IN_STR;
/********************** COMMENTS **********************/

BLOCK_COMMENT: '##' .*? '##' -> skip;

/********************** LITERALS **********************/

fragment OCTAL: '0' DIGIT_17 ('_'? DIGIT_07)* ;
fragment BINARY: '0' ('b' | 'B') '1' ('_'? DIGIT_01)*;
fragment DECIMAL: DIGIT_19 ('_' DIGIT | (DIGIT))*;
fragment HEXADECIMAL: '0' ('x' | 'X') (DIGIT_19 | UPERCASE_AF) ( '_'? (DIGIT | UPERCASE_AF))*;
INTLIT: (OCTAL | BINARY | DECIMAL | HEXADECIMAL) {self.text = self.text.replace('_','')};
FLOATLIT: ((DECIMAL (DECIMAL_POINT | SCIENTIFIC | DECIMAL_POINT SCIENTIFIC)) | DECIMAL_POINT SCIENTIFIC) {self.text = self.text.replace('_','')};
STRLIT: DOUBLE_QUOTE VALID_STRING* DOUBLE_QUOTE
//{
//	content = str(self.text)
//	self.text = content[1:-1]
//}
//TODO ?
;
ZERO: '0' | '00' | '0b0' | '0B0' | '0x0' | '0X0';
/******************** IDENTIFIERS *********************/

STATIC_ID: STATIC [0-9a-zA-Z_]+;
ID: [a-zA-Z_][a-zA-Z0-9_]*;

/********************** SKIP **********************/

WS: [ \t\r\n\f]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: DOUBLE_QUOTE VALID_STRING* ([\r\n]|EOF){
        text = str(self.text)
        if (text[-1] == '\r') or (text[-1] == '\n'):
            raise UncloseString(text[1:-1])
        else:
            raise UncloseString(text[1:])
};

ILLEGAL_ESCAPE: DOUBLE_QUOTE VALID_STRING* ILLEGAL_STRING{
		illegal_str = str(self.text)
		raise IllegalEscape(illegal_str[1:])
};
