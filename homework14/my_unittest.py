import doctest
import unittest


def load_tests(loader,tests,ignore):
    tests.addTests(doctest.DocFileSuite("my_doctest.md"))
    return tests

if __name__=="__main__":
    unittest.main(verbosity=2)