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
