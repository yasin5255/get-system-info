import os
import psutil

def get_cpu_count():
    return os.cpu_count()

def get_ram_size():
    mem = psutil.virtual_memory()
    return mem.total

def get_disk_space():
    disk = psutil.disk_usage('/')
    return disk.total

if __name__ == "__main__":
    cpu_count = get_cpu_count()
    ram_size = get_ram_size()
    disk_space = get_disk_space()

    print("İşlemci Sayısı:", cpu_count)
    print("RAM Miktarı:", ram_size, "bytes")
    print("Boştaki Disk Alanı:", disk_space, "bytes")
