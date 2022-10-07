from gpiozero import CPUTemperature, DiskUsage
import shutil
import psutil

cpu = CPUTemperature()
disk = DiskUsage()
path = "/media/pi/Sanne Data"
stat = shutil.disk_usage(path)
calc = ((stat[1] / stat[0]) * 100)

while True:
    print(f'CPU Temp: {cpu.temperature} \t CPU {psutil.cpu_percent(4)}% \t SD%: {disk.usage}% \t SSD: {calc}%, Memory used: {psutil.virtual_memory().percent}%')
