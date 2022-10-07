from gpiozero import CPUTemperature, DiskUsage
cpu = CPUTemperature()
disk = DiskUsage()

print(f'CPU Temperature: {cpu.temperature}')
print(f'Current disk usage: {disk.usage}%')
