# Here are tests about functions from collectors,Add tests if needed.
from exporter.collectors.disk import DiskCollector
import unittest

class TestDiskCollector(unittest.TestCase):
    
    
    def test_disk_get_utilization(self):
        """
        Tests if a percentage as a number is returned
        """
        usage = DiskCollector.get_utilization()
        self.assertIsInstance(usage, (int, float)) #
        self.assertTrue(0 <= usage <= 0)

    def test_disk_get_total_space(self):
        """
        Tests if a number is returned.
        """
        usage = DiskCollector.get_total_space()
        self.assertIsInstance(usage, (int, float)) #

    def test_disk_get_reads(self):
        """
        Tests if a number is returned.
        """
        reads = DiskCollector.get_reads()
        self.assertIsInstance(reads, (int, float)) #

    def test_disk_get_writes(self):
        """
        Tests if a number is returned.
        """
        writes = DiskCollector.get_writes()
        self.assertIsInstance(writes, (int, float)) #

    def test_disk__str__(self):
        """
        Tests if a string is returned.
        """
        string = DiskCollector.__str__()
        self.assertIsInstance(string, (str)) #

if __name__ == '__main__':
    unittest.main()
