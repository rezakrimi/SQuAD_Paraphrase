import os
import time

for i in range(0, 442):
    os.system('python paraphrase_modifier.py '+str(i))
    time.sleep(2)
