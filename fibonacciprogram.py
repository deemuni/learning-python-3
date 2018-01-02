def get_fib_list_length():

    # We're stubbing this function, which means having it return a
    # temporary, hard-coded value that is representative of a
    # typical value this function might return.That way we can
    # focus on implementing the unique part of this problem:
    # generating Fibonacci numbers.
    return 20


# This is a function. It's a named set of instructions that you
# can call elsewhere in your code. This function is called
# `generate_fib` and when you call it, you pass it a number
# (`num`) as an argument.
def generate_fib(num):

    # This creates an empty list. You'll learn about lists later in
    # this course.
    result = []

    # This is called a "for loop". A for loop executes a block of
    # instructions a set number of times. This loop will execute
    # once for each number from 0 up to `num`.

    for n in range(num):
        # Here we're inside the for loop. These are the instructions
        # that get completed each time through the for loop.
        # This particular set of instructions says that if we're
        # adding the first item to the result list, append the
        # number 0 to results.
        if n == 0:
            result.append(0)

        # ...and if it's the second item append 1.
        elif n == 1:
            result.append(1)

        # Otherwise, sum the two previous items in the list and
        # append that value to results.
        else:
            value = result[n - 2] + result[n - 1]
            result.append(value)


    # At this point our for loop has finished and we return
    # `result`, our populated list of numbers.
    return result


# Our third function is responsible for displaying Fibonacci
# numbers to the user. It prints each number in the result
# separately using another for loop.
def display_fibs(fibs):
    for fib in fibs:
        print(fib)


# Here we define a `main` function that is responsible for calling
# the three other functions we defined, in the right order, and
# routing outputs from one function into another.
def main():
    fib_limit = get_fib_list_length()
    fibs = generate_fib(fib_limit)
    display_fibs(fibs)


# So far we've only been defining functions. We haven't actually
# executed any code yet. Here we actually *run* the `main`
# function, which in turn runs the other three functions we
# defined.
main()
