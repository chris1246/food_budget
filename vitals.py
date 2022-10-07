from gpiozero import CPUTemperature, DiskUsage
import shutil

cpu = CPUTemperature()
disk = DiskUsage()
path = "/media/pi/Sanne Data"
stat = shutil.disk_usage(path)


print(f'CPU Temperature: {cpu.temperature}')
print(f'Internal disk usage: {disk.usage}%')
calc = (stat[1] / stat[0]) * 100
print(f"External disk usage: {calc}%")

#Ping server
