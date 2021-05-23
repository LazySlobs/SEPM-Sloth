import operator
from core.speak import voice_assistant_speak

# Source: https://www.codespeedy.com/voice-command-calculator-in-python/

def get_operator_fn(op):
    return {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        'x' : operator.mul,
        '/' :operator.__truediv__,
        'Mod' : operator.mod,
        'mod' : operator.mod,
        '^' : operator.xor,
        }[op]


def eval_binary_expr(op1, oper, op2):
    op1, op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1, op2)


def do_math(voice_data):
    result = eval_binary_expr(*(voice_data.split()))
    voice_data = voice_data.replace("*", "multiplied by")
    voice_data = voice_data.replace("/", "divided by")
    print(voice_data + " = " + str(result))
    voice_assistant_speak(voice_data + " = " + str(result))

if __name__ == '__main__':
  get_operator_fn()
  eval_binary_expr()
  do_math()