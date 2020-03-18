import unittest


class TestCli(unittest.TestCase):

    def setUp(self):
        self.folders_per_layer = 3
        self.files_per_folder = 10

    def test_extract_metadata_from_fits_file(self):

        self.assertEqual(1, 1, "Should be 1")


if __name__ == '__main__':
    unittest.main()
