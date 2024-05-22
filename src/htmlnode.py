
class HtmlNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html() called from HtmlNode")
    
    def props_to_html(self):
        if self.props == None:
            return ""
        else:
            props_html = ""
            for prop in self.props:
                props_html += f' {prop}="{self.props[prop]}"'
            return props_html

    def __repr__(self):
        string = "## HTML Node ## \n{line}\n".format(line = "-" * 15)
        string += f"Tag: {self.tag}\nValue: {self.value} \n"
        if self.children == None:
            string += "Children: None\n"
        else:
            num = 1
            string += "Children: \n"
            for child in self.children:
                string += f"  Child .{num}: {child} \n"
                num += 1
        
        if self.props == None:
            string += "Props: None"
        else:
            string += "Props: \n"
            num = 1
            for item in self.props.items():
                string += f"  Prop .{num}: {item[0]} : {item[1]}\n"
                num += 1
        string += "\n" + "-" * 5 + " END " + "-" * 5 + "\n"
        return string


class LeafNode(HtmlNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)        
        
    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf Nodes require a value")
        if self.tag == None:
            return self.value
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            props_html = self.props_to_html()
            return f"<{self.tag}{props_html}> {self.value} </{self.tag}>"


class ParentNode(HtmlNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)
        if self.tag == None:
            raise ValueError("No tag provided")
        if self.children == None:
            raise ValueError("No children provided")
        
    def to_html(self):
        html = f"<{self.tag}{self.props_to_html()}>"
        close_tag = f"</{self.tag}>"
        for child in self.children:
            html += child.to_html()            
        return html + close_tag

