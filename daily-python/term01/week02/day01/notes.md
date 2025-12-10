Day 01 – Function I & Function II
Concepts Learned
. A function is a reusable block of code that performs a task.
. Functions help avoid repeating code and reduce mistakes.
. Function I (print inside the function):
. The function prints directly and does not return anything.
. Function II (return value):
. The function creates a result and sends it back with return.
. Return lets me store, modify, and reuse the output.
. Printing happens outside the function when using return.
. Parameters = inputs inside the function definition.
. Arguments = actual values used when calling the  
function.

### Function I: Print Inside
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Vy")

. Prints immediately.
. Nothing is saved or returned.
. Good for simple output.

### Function II: Return a Value
def echo_twice(text):
    result = text + " " + text
    return result

output = echo_twice("hello")
print(output)

. The function creates a result.
. return sends that value back.
. I must store the result in a variable.
. Nothing prints unless I choose to print it.

### Local Variables (Inside the Function)
def study(hours):
    label = "hour" if hours == 1 else "hours"
    print(f"I study {hours} {label} everyday.")

. label exists only inside the function (local scope).
. Helps functions calculate and prepare information internally.

Reflection
. Today I learned the difference between printing and returning.
. Understanding return made Python feel more powerful and flexible.
. For the first time, functions feel clear and not confusing.
. I can now build reusable functions and store their results.
. This made me feel like a real programmer because I’m writing functions the way professionals do.



