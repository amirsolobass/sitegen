from copystatic import copy_from_dir
import unittest
import os
import shutil


class TestCopyStatic(unittest.TestCase):
    def test_copy_from_dir(self):
        src_dir = "test_static_src"
        dest_dir = "test_static_dest"

        # Setup: create source directory and some files
        os.makedirs(src_dir, exist_ok=True)
        with open(os.path.join(src_dir, "testfile.txt"), "w") as f:
            f.write("This is a test file.")

        # Call the function to test
        copy_from_dir(src_dir, dest_dir)

        # Verify: check if files are copied
        self.assertTrue(os.path.exists(dest_dir))
        self.assertTrue(os.path.isfile(os.path.join(dest_dir, "testfile.txt")))

        # Cleanup: remove test directories
        shutil.rmtree(src_dir)
        shutil.rmtree(dest_dir)