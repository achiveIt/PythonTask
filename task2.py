import time

def calculate_execution_time(new_function):
    def wrapper():
        startTime = time.time()
        result = new_function()
        endTime = time.time()
        print(f'Execution Time: {endTime - startTime:.8f} seconds')
        return result
    return  wrapper
    

def logger_function(new_function):
    def wrapper():
        print(f'calling greet function at: {time.time()}')
        result = new_function()
        print(f'funciton call ends at: {time.time()}')
        return result
    return wrapper


@calculate_execution_time
@logger_function
def greet():
    print("Hello..")

greet()