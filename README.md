# Python Notes

# 字符串

Sample Code
```Python
s = "my name is ben"
print(type(s))
print(s)
```

Output
```
<class 'str'>
my name is ben
```

# Bytes
Sample Code
```Python
data = b'hello ben'
print(type(data))
print(data)
```

Output
```
<class 'bytes'>
b'hello ben'
```

# str to bytes, bytes to str

Sample Code
```Python
# str to bytes
str.encode(s)

# bytes to str
bytes.decode(data)
```

# 计算CPU使用率

Caculate CPU Loading
```Python
cpu_stat_dict = {}
cpu_stat_line = "400%cpu  97%user   0%nice  88%sys 200%idle   0%iow  13%irq   3%sirq   0%host"

for usage_item in cpu_stat_line.split():
	usage,item = usage_item.split('%')
	cpu_stat_dict[item] = float(usage)

total = cpu_stat_dict['cpu']
idle = cpu_stat_dict['idle']

total_cpu_usage = (total - idle) / total
print("CPU Loading: {:.2%}".format(total_cpu_usage))
```

Output
```
CPU Loading: 50.00%
```
