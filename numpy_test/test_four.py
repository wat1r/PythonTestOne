import numpy as np




def fill_ndarray(t1):
    for i in range(t1.shape[1]):
        temp_col = t1[:, i]
        nan_count = np.count_nonzero(temp_col != temp_col)
        if nan_count != 0:
            temp_not_nan_col = temp_col[temp_col == temp_col]
            temp_col[np.isnan(temp_col)] = temp_not_nan_col.mean()
    return t1


if __name__ == '__main__':
    t1 = np.arange(12).reshape((3, 4)).astype("float")
    # print(t1)
    t1[1, 2:] = np.nan
    # print(t1)
    print(fill_ndarray(t1))

# print(t1)
