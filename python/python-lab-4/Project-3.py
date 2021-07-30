from math import floor
import time
from datetime import datetime
current_unix=floor(time.time())

current_date=datetime.fromtimestamp(current_unix)

print(current_date)