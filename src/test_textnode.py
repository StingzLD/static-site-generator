import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node1, node2)

        node3 = TextNode("This is a link node", TextType.LINK)
        node4 = TextNode("This is a link node", TextType.LINK)
        self.assertEqual(node3, node4)

        node5 = TextNode("This is an image node", TextType.IMAGE)
        node6 = TextNode("This is an image node", TextType.IMAGE)
        self.assertEqual(node3, node4)

        self.assertNotEqual(node1, node3)
        self.assertNotEqual(node1, node5)
        self.assertNotEqual(node3, node5)


if __name__ == "__main__":
    unittest.main()
