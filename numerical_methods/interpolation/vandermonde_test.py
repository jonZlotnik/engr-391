import unittest
from unittest import TestCase

import numpy as np
from vandermonde import VandermondeInterpolator


class TestVandermondeInterpolator(TestCase):

    def test_vandermonde_matrix__builds_correct_matrix(self):
        vm = VandermondeInterpolator()
        vm.set_data_points(
            [1, 2, 4],
            [2, -1, 5]
        )

        expected_vm_matrix = np.array(
            [[1, 1, 1],
             [1, 2, 4],
             [1, 4, 16]]
        )

        np.testing.assert_array_equal(expected_vm_matrix, vm.vandermonde_matrix)

    def test_model_params__solves_for_correct_params(self):
        vm = VandermondeInterpolator()
        vm.set_data_points(
            [1, 2, 4],
            [2, -1, 5]
        )

        expected_params = (np.array([9, -9, 2])[np.newaxis]).transpose()

        np.testing.assert_array_equal(expected_params, vm.model_params)

    def test_evaluate_at(self):
        np.set_printoptions(precision=15)
        vm = VandermondeInterpolator()
        vm.set_data_points(
            [1, 2, 4],
            [2, -1, 5]
        )

        expected_value = 14
        np.testing.assert_array_equal(expected_value, vm.evaluate_at(5))


if __name__ == '__main__':
    unittest.main()
