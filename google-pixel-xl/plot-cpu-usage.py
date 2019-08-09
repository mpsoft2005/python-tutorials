import os, subprocess, time
import numpy as np
import matplotlib.pyplot as plt

def execute_command(command):
	p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	lines = p.stdout.readlines()

	for idx,line in enumerate(lines):
		line = bytes.decode(line)
		line = line.strip()
		lines[idx] = line

	status = p.wait()
	return status, lines


def calc_cpu_usage(cpu_stat_line):
	cpu_stat_dict = {}
	
	for usage_item in cpu_stat_line.split():
		usage,item = usage_item.split('%')
		cpu_stat_dict[item] = float(usage)

	total = cpu_stat_dict['cpu']
	idle = cpu_stat_dict['idle']

	return (total - idle) / total


plt.axis([0, 60, 0, 100])
plt.ion()

prev_cpu_usage = -1

for i in range(1, 61):
	print(i)
	status, lines = execute_command('adb shell top -n 1')
	cpu_usage = calc_cpu_usage(lines[3])
	print("cpu usage: {:.2%}".format(cpu_usage))

	if prev_cpu_usage < 0:
		prev_cpu_usage = cpu_usage
	
	plt.plot([i-1, i], [prev_cpu_usage*100, cpu_usage*100])
	prev_cpu_usage = cpu_usage
	
	plt.pause(0.1)

plt.pause(9999)
