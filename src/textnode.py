from htmlnode import LeafNode
class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, target):
        if self.text == target.text:
            if self.text_type == target.text_type:
                if self.url == target.url:
                    return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


test_node = TextNode("beans", "bold")

def text_node_to_html_node(text_node):
    valid_types = ["text", "bold", "italic", "code", "link", "image"]
    text_type = text_node.text_type
    if text_type not in valid_types:
        raise Exception(f"{text_type}: is not a valid text type")
    if text_type == "text":
        return LeafNode(value= text_node.text)
    elif text_type == "bold":
        return LeafNode(tag="b", value= text_node.text)
    elif text_type == "italic":
        return LeafNode(tag="i", value= text_node.text)
    elif text_type == "code":
        return LeafNode(tag="code", value= text_node.text)
    elif text_type == "link":
        link = text_node.url
        return LeafNode(tag="a", value= text_node.text, props= {"href":link})
    elif text_type == "image":
        link = text_node.url
        return LeafNode(tag="img", props= {"src":link, "alt":text_node.text})
    

print(text_node_to_html_node(test_node))