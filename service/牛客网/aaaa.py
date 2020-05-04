import os
import signal
print(os.getpid(), signal.SIGKILL)
os.kill(os.getpid(), signal.SIGKILL)
print("Adsfds")