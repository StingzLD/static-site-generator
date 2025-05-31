import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "tag1",
            props={"type": "quote", "source": "musical"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' type="quote" source="musical"',
        )

    def test_values(self):
        node = HTMLNode(
            "tag2",
            "The internet is for porn",
            None,
            {"type": "quote", "source": "Avenue Q"},
        )
        self.assertEqual(
            node.tag,
            "tag2",
        )
        self.assertEqual(
            node.value,
            "The internet is for porn",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            {"type": "quote", "source": "Avenue Q"},
        )

    def test_repr(self):
        node = HTMLNode(
            "tag3",
            "A face so fair, a heart so pure - Sir, if you had been born a woman, you would have been she!",
            None,
            {"type": "quote", "source": "A Funny Thing Happened on the Way to the Forum"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(tag3, A face so fair, a heart so pure - Sir, if you had been born a woman, you would have been she!, None, {'type': 'quote', 'source': 'A Funny Thing Happened on the Way to the Forum'})",
        )


if __name__ == "__main__":
    unittest.main()
