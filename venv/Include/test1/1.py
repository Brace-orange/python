a = [1, 2, 3]
a[1]
print(a[-1])
print(a[::-1])
a[1] = "a"
a.append("re")
a.append([1,32])
a.extend([32,43])
print(a)
a.pop(1)
a.pop()
del a[1]
print(a)
a.pop();
print(a)
print("a.count", a.count(1))
print("a.index", a.index(1))
a.insert(1, "this")
a.insert(3, "re")
a.remove("re") # 移除第一个
print(a)
a.reverse()
# a.sort()
print(a)
# print(max(a))
# print(min(a))
# a + c
# a * 2
print(len(a))