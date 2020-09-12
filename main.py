import time
from sds011 import *

sensor = SDS011("/dev/ttyUSB0", use_query_mode=True)
print("Starting sensor...")
sensor.sleep(sleep=False)
time.sleep(15)

for i in range(0, 10):
    (pm25, pm10) = sensor.query()
    print("pm25 ->", pm25, "pm10 ->", pm10)
    time.sleep(5)

sensor.sleep()
