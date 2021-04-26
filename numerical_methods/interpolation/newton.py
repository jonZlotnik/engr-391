import numpy as np

class NewtonInterpolator:
    def __init__(self):
        self._x = np.ndarray([], np.float64)
        self._y = np.ndarray([], np.float64)

    def set_data_points(self, x: np.ndarray, y: np.ndarray):
        self._x = np.array(x, np.float64)
        self._y = np.array(y, np.float64)

    @property
    def ndd_coefficients(self):
        """
        Creates NDD pyramid and extracts coeffs
        https://medium.com/@sddkal/newtons-divided-difference-method-for-polynomial-interpolation-4bc094ba90d7
        """
        n = np.shape(self._y)[0]
        pyramid = np.zeros([n, n])  # Create a square matrix to hold pyramid
        pyramid[::, 0] = self._y  # first column is y
        for j in range(1, n):
            for i in range(n - j):
                # create pyramid by updating other columns
                pyramid[i][j] = (pyramid[i + 1][j - 1] - pyramid[i][j - 1]) / (self._x[i + j] - self._x[i])
        return pyramid[0]  # return first row