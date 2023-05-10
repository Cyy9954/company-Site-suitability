import unittest
import my_modules.calculate as cal
import my_modules.io as io

class TestRasterFunctions(unittest.TestCase):
    def setUp(self):
        # Create sample raster data for the test case
        self.raster = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    def test_read_raster_data(self):
        # Test functions for reading raster data
        file_path = "Data/Geology_TEST.txt"
        with open(file_path, "w") as f:
            f.write("0,1,2\n3,4,5\n6,7,8\n")
        expected_result = self.raster
        actual_result = io.read_raster_data(file_path)
        self.assertEqual(expected_result, actual_result)

    def test_multiply_raster(self):
        # Test a function that multiplies raster data by a weighting factor
        weight = 2
        expected_result = [[0, 2, 4], [6, 8, 10], [12, 14, 16]]
        actual_result = cal.multiply_raster(self.raster, weight)
        self.assertEqual(expected_result, actual_result)

    def test_add_rasters(self):
        # Test functions that add up raster data
        raster1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        raster2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        raster3 = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
        expected_result = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
        actual_result = cal.add_rasters(raster1, raster2, raster3)
        self.assertEqual(expected_result, actual_result)

    def test_rescale_raster(self):
        # Test the function that rescales the raster data
        new_min = 0
        new_max = 255
        expected_result = [[0, 31, 63], [95, 127, 159], [191, 223, 255]]
        actual_result = cal.rescale_raster(self.raster, new_min, new_max)
        self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
    unittest.main()