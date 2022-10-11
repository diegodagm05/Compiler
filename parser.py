# ------------------------------------------------------------
# parser.py
#
# parser for ALi language
# ------------------------------------------------------------
import ply.yacc as yacc

from lexer import tokens

# ----------------------
# GLOBAL RULES 
def p_program(p):
    '''program : global_vars_funs main
               | main'''

def p_global_vars_funs(p):
    '''global_vars_funs : g_vf''' 

def p_g_vf(p):
    '''g_vf : vars functions
            | vars
            | functions'''

def p_main(p):
    '''main : FUNC MAIN '(' ')' '{' main_block '}' '''

# ----------------------
# MAIN FUNCTION RULES 
def p_main_block(p):
    '''main_block : function_block start_function update_function'''

def p_start_function(p):
    '''start_function : VOID FUNC START '(' ')' '{' sft '}' '''

def p_update_function(p):
    '''update_function : VOID FUNC UPDATE '(' ')' '{' uft '}' '''

def p_sft(p):
    '''sft : start_function_statement sft
            | start_function_statement'''

def p_uft(p):
    '''uft : update_function_statement uft
            | update_function_statement'''

def p_start_function_statement(p):
    '''start_function_statement : statements 
                                | gen_canvas
                                | set_canvas_title
                                | set_canvas_bg 
                                | draw_game_object'''

def p_update_function_statement(p):
    '''update_function_statement : statements 
                                | set_canvas_title
                                | set_canvas_bg 
                                | get_window_h
                                | get_window_w
                                | get_game_ev
                                | draw_game_object'''

def p_gen_canvas(p):
    '''gen_canvas : GEN_CANVAS '(' pixel_param ',' pixel_param ',' STRING_CONST ')' ';' '''

def p_set_canvas_title(p):
    '''set_canvas_title : SET_CANVAS_TITLE '(' STRING_CONST ')' ';' '''

def p_set_canvas_bg(p):
    '''set_canvas_bg : SET_CANVAS_BG '(' STRING_CONST ')' ';' '''

def p_get_window_h(p):
    '''get_window_h : GET_WINDOW_H '(' ')' ';' '''

def p_get_window_w(p):
    '''get_window_w : GET_WINDOW_W '(' ')' ';' '''

def p_get_game_ev(p):
    '''get_game_ev : GET_GAME_EV '(' ')' ';' '''

def p_draw_game_object(p):
    '''draw_game_object : DRAW_GAME_OBJECT '(' pixel_param ',' pixel_param ',' pixel_param ',' pixel_param ',' STRING_CONST ')' ';' '''

def p_pixel_param(p):
    '''pixel_param : variable
                    | I_CONST'''

# ----------------------
# STATEMENTS RULES 

def p_function_block(p):
    '''function_block : vars stm
                        | stm '''

def p_stm(p):
    '''stm : statements stm_p '''

def p_stm_p(p):
    '''stm_p : stm
             | empty'''
             
def p_vars(p):
    '''vars : VAR ids ':' type ';' vars_p'''

def p_vars_p(p):
    '''vars_p : vars
              | empty'''

def p_ids(p):
    '''ids : ID ids_p'''

def p_ids_p(p):
    '''ids_p : ',' ids
             | empty'''

def p_type(p):
    '''type : INT 
            | FLOAT
            | CHAR
            | BOOL'''

def p_array_type(p):
    '''array_type : ARRAY '<' type '>' array_indexing'''

def p_functions(p):
    '''functions : return_function functions
                 | void_function functions
                 | return_function
                 | void_function'''

def p_return_function(p):
    '''return_function : type FUNC ID '(' p ')' '{' function_block RETURN expression ';' '}' '''

def p_p(p):
    '''p : params
         | empty'''

def p_void_function(p):
    '''void_function : VOID FUNC ID '(' p ')' '{' function_block '}' '''

def p_statements(p):
    '''statements : assignment ';'
                  | array_assignment
                  | call_to_fun ';'
                  | write 
                  | conditionals
                  | cycles
                  | read'''

def p_conditionals(p):
    '''conditionals : if_statement 
                    | if_else_statement
                    | if_else_if_statement'''

def p_if_statement(p):
    '''if_statement : simple_if_statement'''

def p_simple_if_statement(p):
    '''simple_if_statement : IF '(' expression ')' interior_block'''

def p_if_else_statement(p):
    '''if_else_statement : simple_if_statement simple_else_statement'''

def p_simple_else_statement(p):
    '''simple_else_statement : ELSE interior_block'''

def p_if_else_if_statement(p):
    '''if_else_if_statement : simple_if_statement simple_else_if_statement simple_else_statement
                            | simple_if_statement simple_else_if_statement'''

def p_simple_else_if_statement(p):
    '''simple_else_if_statement : ELIF '(' expression ')' interior_block more_else_if_statement '''

def p_more_else_if_statement(p):
    '''more_else_if_statement : simple_else_if_statement
                              | empty'''


def p_interior_block(p):
    '''interior_block : '{' '}'
                      | '{' stm '}' '''

def p_params(p):
    '''params : ID ':' type ',' params
              | ID ':' type'''

def p_assignment(p):
    '''assignment : ID '=' expression ';'
                  | ID array_type '=' expression ';' '''

def p_array_assignment(p):
    '''array_assignment : ID '=' array_assign_type ';' '''
 
def p_array_assign_type(p): 
    '''array_assign_type : 1d_array_init
                         | 2d_array_init'''

def p_1d_array_init(p):
    '''1d_array_init : '[' exp_1d ']' '''

def p_exp_1d(p):
    '''exp_1d : expression ',' exp_1d
              | expression'''

def p_2d_array_init(p):
    '''2d_array_init : '[' exp_2d ']' '''

def p_exp_2d(p):
    '''exp_2d : 1d_array_init ',' exp_2d
              | 1d_array_init'''

def p_write(p):
    '''write : PRINT '(' write_p ')' ';' '''
 
def p_write_p(p):
    '''write_p : write_param ',' write_p 
               | write_param'''

def p_write_param(p):
    '''write_param : STRING_CONST
                   | variable '''

def p_read(p):
    '''read : READ '(' read_p ')' ';' '''
 
def p_read_p(p):
    '''read_p : STRING_CONST ',' read_p
              | STRING_CONST'''

def p_call_to_fun(p):
    '''call_to_fun : ID '(' ')'
                   | ID '(' call_p ')' '''
def p_call_p(p):
    '''call_p : expression ',' call_p
              | expression'''

def p_cycles(p):
    '''cycles : while
                | for'''

def p_array_indexing(p):
    '''array_indexing : '[' expression ']' 
                      | '[' expression ']'  '[' expression ']' '''

def p_while(p):
    '''while : WHILE '(' expression ')' interior_block'''

def p_for(p):
    '''for : FOR '(' assignment ';' expression ';' assignment ')' interior_block'''

# ----------------------
# EXRPESSIONS RULES 

def p_expression(p):
    '''expression : t_exp
                  | t_exp OR expression'''

def p_t_exp(p):
    '''t_exp : g_exp
             | g_exp AND t_exp'''

def p_g_exp(p):
    '''g_exp : m_exp
          | m_exp op g_exp 
          | '!' g_exp'''

def p_op(p):
    '''op : '>'
          | '<'
          | GREATER_EQ
          | LESS_EQ
          | EQUAL
          | DIFFERENT'''

def p_m_exp(p):
    '''m_exp : term
           | m_exp '+' term
           | m_exp '-' term '''

def p_term(p):
    '''term : factor 
            | term '*' factor
            | term '/' factor'''

def p_factor(p):
    '''factor : '(' expression ')'
              | constants '''

def p_constants(p):
    '''constants : I_CONST
                 | F_CONST
                 | C_CONST
                 | variable
                 | call_to_fun'''

def p_variable(p):
    '''variable : ID array_indexing 
                | ID'''

# ----------------------
# EMPTY & ERROR RULES 
def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    err_string = f"Syntax error in input at line {p.lineno} at character {p.lexpos} unexpected \'{p.value}\' "
    raise Exception(err_string)

parser = yacc.yacc(debug=True)

def test():
    print('Enter file name to be tested (with .al extension)')
    filename = input()
    file = open(filename)
    input_str = file.read()
    file.close()
    parser.parse(input_str)
    print('Accepted code')

if __name__ == "__main__":
    test()