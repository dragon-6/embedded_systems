import platform
import socket
from pathlib import Path
import sys

print("host:", socket.gethostname())
print("os:", platform.system())
print("cpu:", platform.machine())
print("file:", Path(__file__).resolve())

print("Python:", sys.executable)
print("Virtual environment:", sys.prefix != sys.base_prefix)