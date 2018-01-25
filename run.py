#!bin/python
from app import app
import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        app.run(debug = True)
    elif len(sys.argv) == 3:
        app.run(debug = True, host = sys.argv[1], port = int(sys.argv[2]))
