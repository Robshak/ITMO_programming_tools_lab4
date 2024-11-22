import unittest
import os
import platform
import ctypes

lib_name = "libsegment_tree.so" if platform.system() == "Linux" else "segment_tree.dll"
lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../build", lib_name))

if platform.system() == "Windows":
    lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), lib_name))

if not os.path.exists(lib_path):
    raise FileNotFoundError(f"Library not found at {lib_path}")

segment_tree = ctypes.CDLL(lib_path)



class Node(ctypes.Structure):
    _fields_ = [("min", ctypes.c_int), ("max", ctypes.c_int), ("sum", ctypes.c_int)]

# Setting arguments and types for functions
segment_tree.initialize_tree.argtypes = [ctypes.c_int]
segment_tree.build_wrapper.argtypes = [ctypes.c_int]
segment_tree.update_wrapper.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
segment_tree.query_wrapper.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
segment_tree.query_wrapper.restype = Node


class TestSegmentTree(unittest.TestCase):
    def setUp(self):
        self.size = 32
        segment_tree.initialize_tree(self.size)
        segment_tree.build_wrapper(self.size)

    def test_initial_values(self):
        result = segment_tree.query_wrapper(0, 32, self.size)
        self.assertEqual(result.min, 0)
        self.assertEqual(result.max, 0)
        self.assertEqual(result.sum, 0)

    def test_single_update(self):
        segment_tree.update_wrapper(15, 10, self.size)

        result = segment_tree.query_wrapper(10, 20, self.size)
        self.assertEqual(result.min, 0)
        self.assertEqual(result.max, 10)
        self.assertEqual(result.sum, 10)

    def test_multiple_updates_in_range(self):
        segment_tree.update_wrapper(10, 5, self.size)
        segment_tree.update_wrapper(11, 7, self.size)
        segment_tree.update_wrapper(12, 3, self.size)

        result = segment_tree.query_wrapper(10, 13, self.size)
        self.assertEqual(result.min, 3)
        self.assertEqual(result.max, 7)
        self.assertEqual(result.sum, 15)

    def test_edge_updates(self):
        segment_tree.update_wrapper(0, 20, self.size)
        segment_tree.update_wrapper(31, 40, self.size)

        result = segment_tree.query_wrapper(0, 32, self.size)
        self.assertEqual(result.min, 0)
        self.assertEqual(result.max, 40)
        self.assertEqual(result.sum, 60)

    def test_overlapping_ranges(self):
        segment_tree.update_wrapper(14, 8, self.size)
        segment_tree.update_wrapper(18, 12, self.size)
        
        # First range includes updated values
        result1 = segment_tree.query_wrapper(10, 20, self.size)
        self.assertEqual(result1.min, 0)
        self.assertEqual(result1.max, 12)
        self.assertEqual(result1.sum, 20)

        # Second range also includes updated values but is broader
        result2 = segment_tree.query_wrapper(15, 30, self.size)
        self.assertEqual(result2.min, 0)
        self.assertEqual(result2.max, 12)
        self.assertEqual(result2.sum, 12)

if __name__ == "__main__":
    unittest.main()
