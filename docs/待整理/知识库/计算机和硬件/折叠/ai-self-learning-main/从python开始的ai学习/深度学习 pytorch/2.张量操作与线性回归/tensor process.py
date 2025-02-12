import  torch
torch.manual_seed(1)
import numpy as np

# =================== example 1 ===================#
# torch.cat

# flag = True
flag = False

if flag:
    t = torch.ones((2, 3))

    t_0 = torch.cat([t, t], dim = 0)
    t_1 = torch.cat([t, t], dim = 1)

    print("t_0: {} shape: {}\nt_1: {} shape: {}".format(t_0, t_0.shape, t_1, t_1.shape))

# =================== example 2 ===================#
# torch.stack

# flag = True
flag = False

if flag:
    t = torch.ones((2, 3))

    t_stack = torch.stack([t, t], dim = 2)

    t_stack1 = torch.stack([t, t, t], dim = 0)

    print("\nt_stack:{} shape: {}".format(t_stack, t_stack.shape))

    print("\nt_stack1:{} shape: {}".format(t_stack1, t_stack1.shape))

# =================== example 3 ===================#
# torch.chunk

# flag = True
flag = False

if flag:
    a = torch.ones((2, 7))  # 7
    list_of_tensors = torch.chunk(a, dim = 1, chunks = 3)  # 3

    for idx, t in enumerate(list_of_tensors):
        print("第{}个张量：{}， shape is {}".format(idx + 1, t, t.shape))

# =================== example 4 ===================#
# torch.split

# flag = True
flag = False

if flag:
    t = torch.ones((2, 5))

    list_of_tensors = torch.split(t, [2, 1, 2], dim = 1)
    for idx, t in enumerate(list_of_tensors):
        print("第{}个张量：{}, shape is {}".format(idx + 1, t, t.shape))

# =================== example 5 ===================#
# torch.index_select

# flag = True
flag = False

if flag:
    t = torch.randint(0, 9, size = (3, 3))
    idx = torch.tensor([0, 2], dtype = torch.long)   # 必须是torch.long
    t_select = torch.index_select(t, dim = 0, index = idx)
    print("t: \n{}\nt_select:\n{}".format(t, t_select))

# =================== example 6 ===================#
# torch.masked_select

# flag = True
flag = False

if flag:

    t = torch.randint(0, 9, size = (3, 3))
    mask = t.ge(5)  # ge is mean greater than or equal/ gt: greater than le lt
    t_select = torch.masked_select(t, mask)
    print("t: \n{}mask: \n{}t_select: \n{}".format(t, mask, t_select))

# =================== example 7 ===================#
# torch.reshape

# flag = True
flag = False

if flag:
    t = torch.randperm(8)
    t_reshape = torch.reshape(t, (-1, 2, 2))  # 大小要匹配, -1表示这一维度不关心，自动生成
    print("t: {}\nt_select: \n{}".format(t, t_reshape))

    t[0] = 1024
    print("t: {}\nt_reshape:\n{}".format(t, t_reshape))
    print("t.data 内存地址:{}".format(id(t.data)))
    print("t_reshape.data 内存地址:{}".format(id(t_reshape.data)))

# =================== example 8 ===================#
# torch.transpose

# flag = True
flag = False

if flag:
    # torch.transpose
    t = torch.rand((2, 3, 4))
    t_transpose = torch.transpose(t, dim0 = 1, dim1 = 2)
    print("t shape:{}\nt_transpose shape: {}".format(t.shape, t_transpose.shape))

# =================== example 9 ===================#
# torch.transpose

# flag = True
flag = False

if flag:
    # torch.transpose
    t = torch.rand((1, 2, 3, 1))
    t_sq = torch.squeeze(t)
    t_0 = torch.squeeze(t, dim = 0)
    t_1 = torch.squeeze(t, dim = 1)
    print(t.shape)
    print(t_sq.shape)
    print(t_0.shape)
    print(t_1.shape)

# =================== example 10 ===================#
# torch.add

# flag = True
flag = False

if flag:
    t_0 = torch.randn((3, 3))
    t_1 = torch.ones_like(t_0)
    t_add = torch.add(t_0, t_1, alpha = 10)

    print("t_0: \n{}\nt_1: \n{}\nt_add_10:\n{}".format(t_0, t_1, t_add))
