# 각각 1st, 2nd 숫자와 그 합
# 순서대로 x3, x2, x1, x0
x = [0, 0, 0, 0]
y = [0, 0, 0, 0]

# 4bit full adder 함수 만들기
def adder(x, y):
    # 순서대로 c_out, s3, s2, s1, s0
    s = [0, 0, 0, 0, 0]
    for i in range(3, -1, -1):
        s[i+1] += (x[i] + y[i])
        if s[i+1] >= 2:
            s[i+1] -= 2
            s[i] += 1
    return s

# truth table 작성하기
# 1. Carry.txt
tt1 = open("Carry.txt", "w+")

tt1.write("x3 x2 x1 x0 y3 y2 y1 y0 c_out \n")
# tt1.write("---------------------------------------------- \n")
for i in range(16):
    for i in range(16):
        s = adder(x, y)
        tt1.write("%d %d %d %d %d %d %d %d %d \n" % (x[0], x[1], x[2], x[3], y[0], y[1], y[2], y[3], s[0]))
        y = adder(y, [0, 0, 0, 1])[1:]
    # tt1.write("---------------------------------------------- \n")
    x = adder(x, [0, 0, 0, 1])[1:]

tt1.close()

# 2. S0.txt
tt1 = open("S0.txt", "w+")

tt1.write("x3 x2 x1 x0 y3 y2 y1 y0 s0 \n")
# tt1.write("---------------------------------------------- \n")
for i in range(16):
    for i in range(16):
        s = adder(x, y)
        tt1.write("%d %d %d %d %d %d %d %d %d \n" % (x[0], x[1], x[2], x[3], y[0], y[1], y[2], y[3], s[4]))
        y = adder(y, [0, 0, 0, 1])[1:]
    # tt1.write("---------------------------------------------- \n")
    x = adder(x, [0, 0, 0, 1])[1:]

tt1.close()

# 3. S1.txt
tt1 = open("S1.txt", "w+")

tt1.write("x3 x2 x1 x0 y3 y2 y1 y0 s1 \n")
# tt1.write("---------------------------------------------- \n")
for i in range(16):
    for i in range(16):
        s = adder(x, y)
        tt1.write("%d %d %d %d %d %d %d %d %d \n" % (x[0], x[1], x[2], x[3], y[0], y[1], y[2], y[3], s[3]))
        y = adder(y, [0, 0, 0, 1])[1:]
    # tt1.write("---------------------------------------------- \n")
    x = adder(x, [0, 0, 0, 1])[1:]

tt1.close()

# 4. S2.txt
tt1 = open("S2.txt", "w+")

tt1.write("x3 x2 x1 x0 y3 y2 y1 y0 s2 \n")
# tt1.write("---------------------------------------------- \n")
for i in range(16):
    for i in range(16):
        s = adder(x, y)
        tt1.write("%d %d %d %d %d %d %d %d %d \n" % (x[0], x[1], x[2], x[3], y[0], y[1], y[2], y[3], s[2]))
        y = adder(y, [0, 0, 0, 1])[1:]
    # tt1.write("---------------------------------------------- \n")
    x = adder(x, [0, 0, 0, 1])[1:]

tt1.close()

# 5. S3.txt
tt1 = open("S3.txt", "w+")

tt1.write("x3 x2 x1 x0 | y3 y2 y1 y0 | s3 \n")
# tt1.write("---------------------------------------------- \n")
for i in range(16):
    for i in range(16):
        s = adder(x, y)
        tt1.write("%d %d %d %d %d %d %d %d %d \n" % (x[0], x[1], x[2], x[3], y[0], y[1], y[2], y[3], s[1]))
        y = adder(y, [0, 0, 0, 1])[1:]
    # tt1.write("---------------------------------------------- \n")
    x = adder(x, [0, 0, 0, 1])[1:]

tt1.close()