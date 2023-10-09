x,y = 5,3
op =  "add"

if op == "add":
    print(x+y)
elif op == "mul":
    print(x*y)

match op:
    case "add":
        print(x+y)
    case "mul":
        print(x*y)

#Good alternative
functions  = {
    "add": lambda x,y : x+y,
    "mul": lambda x,y : x*y
}

print(functions["add"](5,3))

#using proper functions
def add(x,y):
    return x+y
def mul(x,y):
    return x*y

functions = {
    "add":add,
    "mul":mul,
}

print(functions["mul"](5,3))

#emulating match/case pattern
from collections import defaultdict

cases = defaultdict(lambda *args: lambda *a: "Invalid option",{
    "add":add,
    "mul":mul,
})

print(cases["add"](5,3))
#passing parameters
def handle_event(e):
    print(f"Handling event in 'handler_event' with {e}")
    return e

def handle_other_event(e):
    print(f"Handling event in 'handle_other_event' with {e}")
    return e

functions = {
    "event1": lambda arg: handle_event(arg["some_key"]),
    "event2": lambda arg: handle_other_event(arg["some_other_key"]),
}

event = {
    "some_key":"value",
    "some_other_key":"different value",
}

print(functions["event1"](event))
print(functions["event2"](event))

#Real world code call it [parse_args.py]
import argparse

functions = {
    "add":add,
    "mul":mul,
}

parser = argparse.ArgumentParser()
parser.add_argument(
    "operation",
    choices=["add","mul"],
    help="operation to perform (add,mul)",
)

parser.add_argument(
    "x",
    type=int,
    help="first number"
)

parser.add_argument(
    "y",
    type=int,
    help="second number",
)

args = parser.parse_args()
answer = functions.get(args.operation,)(args.x,args.y)
print(answer)