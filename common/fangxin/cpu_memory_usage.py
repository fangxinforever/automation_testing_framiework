import psutil
import time

# 获取CPU占用率和内存占用率
cpu_percent = psutil.cpu_percent()
mem_percent = psutil.virtual_memory().percent

# 输出CPU占用率和内存占用率
print("CPU占用率：{}%".format(cpu_percent))
print("内存占用率：{}%".format(mem_percent))

# 每隔一秒钟获取一次CPU和内存占用率
while True:
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent

    print("CPU占用率：{}%".format(cpu_percent))
    print("内存占用率：{}%".format(mem_percent))

    time.sleep(1)
