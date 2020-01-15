import unittest
import depth_dict
import depth_object
import lca


class TestFunctionality(unittest.TestCase):

    def test_depth_dict(self):
        a = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4
                }
            }
        }
        result = dict(depth_dict.print_depth(a))
        self.assertEqual(result['key1'], 1)
        self.assertEqual(result['key2'], 1)
        self.assertEqual(result['key3'], 2)
        self.assertEqual(result['key4'], 2)
        self.assertEqual(result['key5'], 3)

    def test_depth_object(self):
        a = {
            'key1': 1,
            'key2': {
                'key3': 1,
                'key4': {
                    'key5': 4,
                    'user': depth_object.person_a,
                }
            }
        }
        result = dict(depth_object.print_depth(a))
        self.assertEqual(result['key1'], 1)
        self.assertEqual(result['key2'], 1)
        self.assertEqual(result['key3'], 2)
        self.assertEqual(result['key4'], 2)
        self.assertEqual(result['key5'], 3)
        self.assertEqual(result['user: '], 3)
        self.assertEqual(result['first_name: '], 4)
        self.assertEqual(result['last_name: '], 4)
        self.assertEqual(result['father: '], 4)

    def test_lca(self):
        root = lca.root
        result = lca.lca(root, 3, 7)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()


