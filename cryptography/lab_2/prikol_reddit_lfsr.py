import numpy as np

def lfsr(p, s, n):
    ''' Linear feedback shift-register.

    'p' is a list/array of 1s and 0s corresponding to the coefficients of the
        primitive polynomial in GF(2).
    's' is the list of the initial state of the LFSR (also 1s and 0s).
        It is required that len(s) >= len(p).
    'n' is the length of the desired bitstream (e.g. for a list of 7 initial
        states, n could be 64 to return a random bitstream (boolean array) of
        length 64).

    '''
    # set comparison indices
    end = len(s)
    start = end - len(p)
    # create output array, bool for efficient comparisons and storage
    s_out = np.empty(n, dtype=bool)
    # copy over starting values
    s_out[:end] = s
    # reverse p and convert to bool for efficient comparisons
    p_reversed = np.array(p[::-1], dtype=bool)

    # create full sequence
    while end < n:
        s_out[end] = np.logical_xor.reduce(p_reversed & s_out[start:end])
        start += 1
        end += 1

    return s_out

array = lfsr([1, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0], 100)
arr = array.astype(int)
print(arr)