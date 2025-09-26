# def f(s, s2, m):
#     if s + s2 >= 63: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(s+1,s2,m-1), f(s*2,s2,m-1), f(s,s2+1,m-1), f(s,s*2,m-1)]
#     return any(h) if m%2 != 0 else all(h)
# # print(19, min(s for s in range (1,58) if f(5,s,2)))
# print(20, [s for s in range(1,58) if not f(5,s,1) and f(5,s,3)])
# print(21, min(s for s in range(1,58) if not f(5,s,2) and f(5,s,4)))
#
# ## any - хотя бы один
# ## all - все



#=======================
#ЗАДАЧА НОВЫМ СПОСОБОМ

# 0 ход это начало, первый петя 1 ход

# def f(s, h):
#     if s >= 41: return h % 2 == 0
#     if h == 0: return 0
#     step = [f(s+1, h-1), f(s+4, h-1), f(s*3, h-1)]
#     return any(step) if h % 2 != 0 else all(step)
#
# # print("19 задача: ", min(s for s in range(1, 41) if f(s, 2)))
# print("20 задача: ", [s for s in range(1, 41) if not f(s, 1) and f(s,3)])
# print("20 задача: ", min(s for s in range(1, 41) if not f(s, 2) and f(s, 4)))

### +1 *2 >=59 , 5;s

def f(s, s2, h):
    if s+s2 >= 59: return h % 2 == 0
    if h == 0: return 0
    step = [f(s+1, s2, h-1), f(s*2, s2, h-1), f(s, s2+1, h-1), f(s, s2*2, h-1)]
    return any(step) if h % 2 != 0 else any(step)
print(min(s for s in range(1, 54) if (5,s,2)))

# def f(k, p):
#     if k >= 151 and p == 2:
#         return 1
#     elif k < 151 and p == 2:
#         return 0
#     elif k >= 151 and p < 2:
#         return 0
#
#     if p % 2 == 0: ## до этого был ход ВАНИ (четный)
#         if k % 3 == 1:
#             return f(k+1, p+1) and f(k*2, p+1)
#         elif k % 3 == 2:
#             return f(k+2, p+1) and f(k*2, p+1)
#     else: ## до этого был ход ПЕТИ (нечетный)
#         if k % 3 == 1:
#             return f(k+1, p+1) or f(k*2, p+1)
#         elif k % 3 == 2:
#             return f(k+2, p+1) or f(k*2, p+1)
#
# for s in range(1, 150):
#     if s % 3 != 0 and f(s, 0):
#         print(s)


# def f(k, p):
#     if k >= 151 and p in (2, 4):
#         return 1
#     elif k < 151 and p == 4:
#         return 0
#     elif k >= 151 and p < 4:
#         return 0
#
#     if p % 2 == 1:
#         if k % 3 == 1:
#             return f(k+1, p+1) and f(k*2, p+1)
#         elif k % 3 == 2:
#             return f(k+2, p+1) and f(k*2, p+1)
#     else:
#         if k % 3 == 1:
#             return f(k+1, p+1) or f(k*2, p+1)
#         elif k % 3 == 2:
#             return f(k+2, p+1) or f(k*2, p+1)
#
#
# def f2(k, p):
#     if k >= 151 and p == 2:
#         return 1
#     elif k < 151 and p == 2:
#         return 0
#     elif k >= 151 and p < 2:
#         return 0
#
#     if p % 2 == 1:
#         if k % 3 == 1:
#             return f2(k+1, p+1) and f2(k*2, p+1)
#         elif k % 3 == 2:
#             return f2(k+2, p+1) and f2(k*2, p+1)
#     else:
#         if k % 3 == 1:
#             return f2(k+1, p+1) or f2(k*2, p+1)
#         elif k % 3 == 2:
#             return f2(k+2, p+1) or f2(k*2, p+1)
#
# for s in range(1, 150):
#     if s % 3 != 0 and f(s, 0):
#         print(s)
#
# print("=============")
#
# for s in range(1, 150):
#     if s % 3 != 0 and f2(s, 0):
#         print(s)