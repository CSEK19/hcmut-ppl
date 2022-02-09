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


expr: exp_0;
exp_0: exp_1 (SADD | SEQ) exp_1 | exp_1;
exp_1: exp_2 exp_RelationalOperand exp_2 | exp_2;
exp_2: exp_2 (AND | OR) exp_3 | exp_3;
exp_3: exp_3 (ADD | SUB) exp_4 | exp_4;
exp_4: exp_4 (MUL | DIV | MOD) exp_5 | exp_5;
exp_5: NOT exp_5 | exp_6;
exp_6: SUB exp_6 | exp_7;
exp_7: exp_7 LSB expr RSB | exp_8;
exp_8: exp_8 DOT ID (LB list_Expr? RB)? | exp_9;
exp_9: ID SCOPE STATIC_ID (LB list_Expr? RB)? | exp_10;
exp_10: NEW exp_10 LB list_Expr? RB | exp_11;
exp_11: ID | SELF | NULL | lit_Data | LB expr RB;


exp_RelationalOperand: LT | LTE | GT | GTE | EQ | NEQ;



// Index operators
exp_Idx: (ID | exp_StaticAttributeAccess | exp_InstanceAttributeAccess) idx_Operators;
idx_Operators: LSB expr RSB idx_Operators?;


//  Member access
exp_IdxMemberAccess: LB ID idx_MemberAccessOperators RB;
idx_MemberAccessOperators: LSB expr RSB idx_MemberAccessOperators?;
scalar_Variable: ID | SELF | exp_StaticAttributeAccess | exp_StaticMethodInvocation | exp_ObjCreation | exp_IdxMemberAccess;

exp_InstanceAttributeAccess: exp_InstanceAttributeAccess DOT ID | exp_InstanceAttributeAccessTerm;
exp_InstanceAttributeAccessTerm: scalar_Variable DOT ID LB list_Expr? RB | scalar_Variable | LB scalar_Variable RB;

exp_InstanceMethodInvocation: exp_InstanceMethodInvocation DOT ID (LB list_Expr? RB)? | exp_InstanceMethodInvocationTerm;
exp_InstanceMethodInvocationTerm: exp_11 | exp_InstanceAttributeAccess;

exp_StaticAttributeAccess: ID SCOPE STATIC_ID;
exp_StaticMethodInvocation: ID SCOPE STATIC_ID LB list_Expr? RB;

// Object creation
exp_ObjCreation: NEW ID LB list_Expr? RB | LB exp_ObjCreation RB;

// List of expressions
list_Expr: expr (CM expr)*;

/********************** STATEMENTS **********************/

// Variable and Constant Declaration
type_Data: ID | INT | FLOAT | BOOLEAN | STRING | array_Type;
type_DataArray: INT | FLOAT | BOOLEAN | STRING | array_Type;
array_Type: ARRAY LSB type_DataArray CM INTLIT RSB;
seq_ID: (STATIC_ID | ID) (CM (STATIC_ID | ID))*;
list_Attribute: (STATIC_ID | ID) list_AttributeTerm expr | seq_ID COLON type_Data;
list_AttributeTerm: CM (STATIC_ID | ID) list_AttributeTerm expr CM | COLON type_Data ASSIGN;
stmt_AttributeDeclaration: (VAL | VAR)? list_Attribute SM;


// Assignment statement
lhs:  ID | exp_InstanceAttributeAccess | exp_StaticAttributeAccess | exp_Idx;
stmt_Assign: lhs ASSIGN expr SM;

// If statement
stmt_If: IF LB expr RB stmt_Block+ (ELSEIF LB expr RB  stmt_Block+)* (ELSE stmt_Block+)?;

// For/In statement
stmt_ForIn: FOREACH LB ID IN expr DOUBLE_DOT expr (BY expr)? RB stmt_Block ;

// Block statement
stmt_Block: LCB (list_Stmt) RCB ;

// Method Invocation statement
stmt_MethodInvocation: (exp_InstanceMethodInvocation  | exp_StaticMethodInvocation) SM;

// Continue statement
stmt_Continue: CONTINUE SM;

// Return statement
stmt_Return: RETURN expr? SM;

// Break statment
stmt_Break: BREAK SM;

list_AttributeMethod: ID list_AttributeMethodTerm expr | ID (CM ID)* COLON type_Data;
list_AttributeMethodTerm: CM ID list_AttributeMethodTerm expr CM | COLON type_Data ASSIGN;
stmt_MethodVarDeclaration: (VAL | VAR)? list_AttributeMethod SM;

// Final description of statement
stmt:
	stmt_MethodVarDeclaration
	| stmt_Assign
	| stmt_If
	| stmt_ForIn
	| stmt_Block
	| stmt_MethodInvocation
	| stmt_Continue
	| stmt_Return
	| stmt_Break
	| stmt_ClassMethod;
list_Stmt : stmt*;

/********************** CLASSES **********************/

stmt_ClassMethod:  class_Construction | class_Destruction;
stmt_ClassDeclaration: CLASS ID (COLON ID)? LCB (stmt_AttributeDeclaration | stmt_MethodDeclaration | stmt_ClassMethod)* RCB;
stmt_MethodDeclaration: (STATIC_ID | ID) LB (list_Parameters)? RB stmt_Block;

class_Construction: CONSTRUCTOR LB (list_Parameters)? RB  stmt_Block;
class_Destruction: DESTRUCTOR LB RB stmt_Block;


list_Parameters: seq_Parameters (SM seq_Parameters)*;
seq_Parameters: seq_IDParameters COLON type_Data;
seq_IDParameters: ID (CM ID)*;

/********************** RULES **********************/

lit_Array: ARRAY LB (expr (CM expr)*)? RB;

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
DOUBLE_DOT: '..';

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
fragment SCIENTIFIC: ('e' | 'E') ('-' | '+')? DIGIT+;
fragment DECIMAL_POINT: DOT DIGIT*;

fragment DOUBLE_QUOTE: '"';
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
FLOATLIT: ((('0' | DECIMAL) (DECIMAL_POINT | SCIENTIFIC | DECIMAL_POINT SCIENTIFIC)) | DECIMAL_POINT SCIENTIFIC) {self.text = self.text.replace('_','')};
STRLIT: DOUBLE_QUOTE VALID_STRING* DOUBLE_QUOTE{
	content_str = str(self.text)
	self.text = content_str[1:-1]
};
ZERO: '0' | '00' | '0b0' | '0B0' | '0x0' | '0X0';

/******************** IDENTIFIERS *********************/

STATIC_ID: STATIC [0-9a-zA-Z_]+;
ID: [a-zA-Z_][0-9a-zA-Z_]*;

/********************** SKIP **********************/

WS: [ \t\r\n\f]+ -> skip; // skip spaces, tabs, newlines

UNCLOSE_STRING: DOUBLE_QUOTE VALID_STRING*{
        unclose_str = str(self.text)
        raise UncloseString(unclose_str[1:])
};

ERROR_CHAR: . {raise ErrorToken(self.text)};

ILLEGAL_ESCAPE: DOUBLE_QUOTE VALID_STRING* ILLEGAL_STRING{
		illegal_str = str(self.text)
		raise IllegalEscape(illegal_str[1:])
};
