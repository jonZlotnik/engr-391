import numpy as np
from scipy.linalg import solve


class VandermondeInterpolator:

    def __init__(self):
        self._x = np.ndarray([], np.float64)
        self._y = np.ndarray([], np.float64)

    def set_data_points(self, x: np.ndarray, y: np.ndarray):
        self._x = np.array(x, np.float64)
        self._y = np.array(y, np.float64)

    @property
    def vandermonde_matrix(self) -> np.ndarray:
        return np.vander(self._x)

    @property
    def model_params(self) -> np.ndarray:
        params = solve(self.vandermonde_matrix, self._y)[np.newaxis]
        return params.transpose()

    def evaluate_at(self, x) -> np.float64:
        input_matrix = np.empty(len(self._x), np.float64)
        for i in range(len(self._x)):
            input_matrix[i] = np.power(x, i)

        return np.matmul(input_matrix, self.model_params)
