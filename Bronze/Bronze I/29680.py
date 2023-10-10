import math
h,w,w1,w2 = map(float,input().split())
print(round(math.sqrt((w2-w1)**2 + h**2)*w + w*w1 + ((w1+w2) * h),5))