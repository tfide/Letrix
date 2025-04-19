import time

    
start_time = time.time()

def reset():
    global start_time
    start_time = time.time()

def set_timer(value: float):
    global start_time
    start_time = time.time() - value

def get_time() -> float:
    return time.time() - start_time

def start_timer():
    reset()
