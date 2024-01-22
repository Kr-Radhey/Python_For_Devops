import os
import shutil

total, used, freee = shutil.disk_usage("/")

print(f"Total disk size is : {total // 2**30} GB")
print(f"Used disk space is : {used //2**30} GB")
print(f"Free disk space is : {freee //2**30} GB")