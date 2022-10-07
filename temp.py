from gpiozero import CPUTemperature, DiskUsage
import shutil

cpu = CPUTemperature()
disk = DiskUsage()
path = "/media/pi/Sanne Data"
stat = shutil.disk_usage(path)


print(f'CPU Temperature: {cpu.temperature}')
print(f'Current disk usage: {disk.usage}%')

print(f"Disk usage statistics:{stat}")

#Ping server
