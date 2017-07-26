# Created by: Aditya Dua
# 25 July, 2017
"""
Test module for poses: SO2, SE2, SO3 and SE3
"""
import unittest
import numpy as np
from .. import pose
from .common import matrix_mismatch_string_builder
from .common import matrices_equal


class TestSO3(unittest.TestCase):

    def test_pose_so3_constructor_no_args(self):
        obj = pose.SO3()
        exp_mat = np.asmatrix(np.eye(3, 3))
        rec_mat = obj.data[0]
        if not matrices_equal(rec_mat, exp_mat):
            output_str = matrix_mismatch_string_builder(rec_mat, exp_mat)
            self.fail(output_str)

    def test_pose_so3_constructor_so3_object(self):
        obj1 = pose.SO3()
        obj2 = pose.SO3(obj1)

        for i in range(obj2.length):
            if not np.array_equal(obj1.data[i], obj2.data[i]):
                output_str = matrix_mismatch_string_builder(obj2.data[i], obj1.data[i])
                self.fail(output_str)


    def test_pose_so3_constructor_se3(self):
        self.fail("Missing implementation")

if __name__ == '__main__':
    unittest.main()