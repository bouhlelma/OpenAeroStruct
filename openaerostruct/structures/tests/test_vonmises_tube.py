import unittest

from openaerostruct.structures.vonmises_tube import VonMisesTube
from openaerostruct.utils.testing import run_test, get_default_surfaces


class Test(unittest.TestCase):

    def test(self):
        surface = get_default_surfaces()[0]

        comp = VonMisesTube(surface=surface)

        run_test(self, comp)


if __name__ == '__main__':
    unittest.main()
