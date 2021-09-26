import signal, sys

def catch_ctrl_C(sig,frame):
    print("You can not use CTRL+C to exit code")

signal.signal(signal.SIGINT, catch_ctrl_C)

# Your code here
