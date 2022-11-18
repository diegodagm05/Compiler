from collections import deque
from func_dir import FuncDirEntry
from runtime_memory import RuntimeMemory
from quadruple import Quadruple, quadruple_operations
from semantic_rules import semantics, CompilationResults
from parser import ali_parser

def calculate_function_resources(scope: FuncDirEntry) -> list:
    resources = [
        [scope.num_vars_int, scope.num_vars_float, scope.num_vars_char, scope.num_vars_bool],
        [scope.num_temps_int, scope.num_temps_float, scope.num_temps_char, scope.num_temps_bool],
        scope.num_pointer_temps
    ]
    for param in scope.params_list:
        if param == 'i':
            resources[0][0] += 1
        elif param == 'f':
            resources[0][1] += 1
        elif param == 'c':
            resources[0][2] += 1
        elif param == 'b':
            resources[0][3] += 1
    return resources


def virtual_machine(compilation_results: CompilationResults) -> None:
    # print(compilation_results.func_dir)
    # print(compilation_results.consts_table)
    runtime_memory = RuntimeMemory(compilation_results.consts_table, compilation_results.func_dir)
    quadruples : list[Quadruple] = compilation_results.quadruples
    ip = 0
    call_stack = deque()
    # for i, quad in enumerate(quadruples):
    #     print(f'{i}. {quad}')
    print('--ALi CONSOLE OUTPUT--')
    while True:
        current_quad = quadruples[ip]
        # print("-----------------------------------------")
        # print(f"Quad # {ip} \n Processing {current_quad}  ")
        # print(f'current memory -> \n{runtime_memory.current_mem_segment}')
        # print(f'const memory segment -> \n{runtime_memory.constant_memory_segment}')
        # print(f'global mem segment -> \n{runtime_memory.global_memory_segment}')
        if current_quad.op_code == quadruple_operations['endprogram']:
            break 
        elif current_quad.op_code == quadruple_operations['+']:
            left_operand = runtime_memory.retrieve_content(current_quad.operator1)
            right_operand = runtime_memory.retrieve_content(current_quad.operator2)
            result = left_operand + right_operand
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['-']:
            left_operand = runtime_memory.retrieve_content(current_quad.operator1)
            right_operand = runtime_memory.retrieve_content(current_quad.operator2)
            result = left_operand - right_operand
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['*']:
            left_operand = runtime_memory.retrieve_content(current_quad.operator1)
            right_operand = runtime_memory.retrieve_content(current_quad.operator2)
            result = left_operand * right_operand
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['/']:
            left_operand = runtime_memory.retrieve_content(current_quad.operator1)
            right_operand = runtime_memory.retrieve_content(current_quad.operator2)
            result = left_operand / right_operand
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['&&']:
            left_operand = runtime_memory.retrieve_content(current_quad.operator1)
            right_operand = runtime_memory.retrieve_content(current_quad.operator2)
            result = left_operand and right_operand
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['||']:
            left_operand = runtime_memory.retrieve_content(current_quad.operator1)
            right_operand = runtime_memory.retrieve_content(current_quad.operator2)
            result = left_operand or right_operand
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['==']:
            left_operand = runtime_memory.retrieve_content(current_quad.operator1)
            right_operand = runtime_memory.retrieve_content(current_quad.operator2)
            result = (left_operand == right_operand)
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['!=']:
            left_operand = runtime_memory.retrieve_content(current_quad.operator1)
            right_operand = runtime_memory.retrieve_content(current_quad.operator2)
            result = left_operand != right_operand
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['>']:
            left_operand = runtime_memory.retrieve_content(current_quad.operator1)
            right_operand = runtime_memory.retrieve_content(current_quad.operator2)
            result = left_operand > right_operand
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['<']:
            left_operand = runtime_memory.retrieve_content(current_quad.operator1)
            right_operand = runtime_memory.retrieve_content(current_quad.operator2)
            result = left_operand < right_operand
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['<']:
            left_operand = runtime_memory.retrieve_content(current_quad.operator1)
            right_operand = runtime_memory.retrieve_content(current_quad.operator2)
            result = left_operand < right_operand
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['>=']:
            left_operand = runtime_memory.retrieve_content(current_quad.operator1)
            right_operand = runtime_memory.retrieve_content(current_quad.operator2)
            result = left_operand >= right_operand
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['<=']:
            left_operand = runtime_memory.retrieve_content(current_quad.operator1)
            right_operand = runtime_memory.retrieve_content(current_quad.operator2)
            result = left_operand <= right_operand
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['=']:
            result = runtime_memory.retrieve_content(current_quad.operator1)
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['!']:
            result = runtime_memory.retrieve_content(current_quad.operator1)
            result = not result
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['print']:
            print_content = runtime_memory.retrieve_content(current_quad.result)
            print(print_content)
            ip += 1
        # TODO: Our 'read' operation will in reality involve handling game events
        elif current_quad.op_code == quadruple_operations['read']:
            pass
        elif current_quad.op_code == quadruple_operations['goto']:
            ip = current_quad.result
        elif current_quad.op_code == quadruple_operations['gotot']:
            true_test = runtime_memory.retrieve_content(current_quad.operator1)
            if true_test:
                ip = current_quad.result
            else:
                ip += 1
        elif current_quad.op_code == quadruple_operations['gotof']:
            false_test = runtime_memory.retrieve_content(current_quad.operator1)
            if false_test == False:
                ip = current_quad.result
            else:
                ip += 1
        elif current_quad.op_code == quadruple_operations['gosub']:
            call_stack.append(ip+1)
            runtime_memory.sleep_current_memory()
            ip = current_quad.result
        elif current_quad.op_code == quadruple_operations['era']:
            scope = compilation_results.func_dir.get_scope(current_quad.result)
            resources = calculate_function_resources(scope)
            runtime_memory.create_mem_segment(resources)
            ip += 1
        elif current_quad.op_code == quadruple_operations['parameter']:
            # We need to specifically access the current memory to retrieve the values and copy them to our activation record before it is set as the current memory
            copy_value = runtime_memory.current_mem_segment.retrieve_content(current_quad.operator1)
            runtime_memory.activation_record.assign_content(current_quad.result, copy_value)
            ip += 1
        elif current_quad.op_code == quadruple_operations['endfunc']:
            runtime_memory.destroy_current_mem_segment()
            previous_call = call_stack.pop()
            ip = previous_call
        elif current_quad.op_code == quadruple_operations['return']:
            result = runtime_memory.retrieve_content(current_quad.operator1)
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['verify']:
            index_to_verify = runtime_memory.retrieve_content(current_quad.operator1)
            lower_bound = current_quad.operator2
            upper_bound = current_quad.result
            if index_to_verify >= lower_bound and index_to_verify < upper_bound:
                ip += 1
            else:
                raise Exception(f'Index \'{index_to_verify}\' out of bounds. Expected index to be in range \'{lower_bound} - {upper_bound}\'')
        elif current_quad.op_code == quadruple_operations['add_base_address']:
            base_address = current_quad.operator1
            add_value = runtime_memory.retrieve_content(current_quad.operator2)
            result = base_address + add_value
            runtime_memory.current_mem_segment.assign_content(current_quad.result, result, storing_vaddress=True)
            ip += 1
        elif current_quad.op_code == quadruple_operations['multiply_displacement']:
            index_expression = runtime_memory.retrieve_content(current_quad.operator1)
            mutiplier = current_quad.operator2
            result = index_expression * mutiplier
            runtime_memory.current_mem_segment.assign_content(current_quad.result, result)
            ip += 1 
        else:
            raise RuntimeError('Unknown action for virtual machine')

if __name__ == '__main__':
    print('Enter file name to be tested (with .al extension)')
    filename = input()
    file = open(filename)
    input_str = file.read()
    file.close()
    ali_parser.parse(input_str)
    compilation_results : CompilationResults = semantics.get_compilation_results()
    virtual_machine(compilation_results)

