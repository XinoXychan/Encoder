#mau ngapain?
import os, sys
os.system('git pull')
try:
    __import__("Aku").main()
except Exception as e:
    exit(str(e))
