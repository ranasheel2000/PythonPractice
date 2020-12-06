import time
import datetime

if __name__ == "__main__":
  while True:
    timeStamp = datetime.datetime.now()
    print("current timestamp =", timeStamp)
    time.sleep(1)
