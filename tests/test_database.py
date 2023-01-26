import toolkit as tk
import unittest
from unittest.mock import patch


class TestDatabase(unittest.TestCase):

    def test_db_connect(self):
        tk.db_connect('postgresql://reader:NWDMCE5xdipIjRrp@hh-pgsql-public.ebi.ac.uk:5432/pfmegrnargs')

    def test_db_execute(self):
        tk.db_connect('postgresql://reader:NWDMCE5xdipIjRrp@hh-pgsql-public.ebi.ac.uk:5432/pfmegrnargs')

        result = tk.db_execute('SELECT * FROM information_schema.tables;')
        self.assertGreater(len(result), 0)


if __name__ == '__main__': unittest.main()