import unittest

TestRepeatedEnum = None


class RepeatedEnumTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global TestRepeatedEnum
        from test_repeated_enum_proto import TestRepeatedEnum

    def test_repeated_enum_serde(self):
        message1 = TestRepeatedEnum()
        message2 = TestRepeatedEnum()

        message1.list_enum.append(2)
        message1.list_enum.append(0)
        message1.list_enum.append(1)
        # Must be able to handle arbitrary integers in enums:
        message1.list_enum.append(42)
        # ... but not arbitrary values:
        with self.assertRaises(TypeError):
            message1.list_enum.append('not an int')

        buf = message1.SerializeToString()
        message2.ParseFromString(buf)

        for i in range(len(message1.list_enum)):
            self.assertEqual(message1.list_enum[i], message2.list_enum[i])

    def test_single_enum_serde(self):
        message1 = TestRepeatedEnum()
        message2 = TestRepeatedEnum()

        message1.single_enum = 1
        # Must be able to handle arbitrary integers in enums:
        message1.single_enum = 42
        # ... but not arbitrary values:
        with self.assertRaises(TypeError):
            message1.single_enum = 'not an int'

        buf = message1.SerializeToString()
        message2.ParseFromString(buf)

        self.assertEqual(message1.single_enum, message2.single_enum)

if __name__ == "__main__":
    unittest.main()
