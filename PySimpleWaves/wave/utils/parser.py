import re


def wave_parser(text: str):
    pattern = re.compile(r'([+-]?\d*\.?\d*) *(cos|sin)\((.*?)\)')
    match = pattern.match(text)

    if match:
        amplitude = float(match.group(1)) if match.group(1) else 1.0
        function_type = match.group(2)
        argument = match.group(3)
        omega = parse_wave_args(argument)[1]
        k = parse_wave_args(argument)[0]
        phi = parse_wave_args(argument)[2]
        operand_one = extract_operators(argument)[0]
        operand_two = extract_operators(argument)[1]

        return [amplitude, function_type, argument, k, omega, phi, operand_one, operand_two]
    else:
        return [0, "Nil", "Nil", "0", 0, 0, 0, "+", "+"]

def parse_wave_args(text: str):
    terms = text.replace('+', ' +').replace('-', ' -').split()
    x_coefficient = 0
    t_coefficient = 0
    constant_term = 0

    for term in terms:
        if 'x' in term:
            x_coefficient += float(term.strip('x'))
        elif 't' in term:
            t_coefficient += float(term.strip('t'))
        else:
            constant_term += float(term)

    return [x_coefficient, t_coefficient, constant_term]

def extract_operators(expression):
    pattern = re.compile(r'[+-]')
    matches = pattern.findall(expression)
    if len(matches) == 1:
        matches.append('+')

    return matches