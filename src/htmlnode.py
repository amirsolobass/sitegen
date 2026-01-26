class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        

    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)


    def to_html(self):
        if self.tag == "img":
            props_html = self.props_to_html()
            return f"<{self.tag}{props_html}/>"
        if self.tag is None:
            return self.value
        if self.value is None:
            raise ValueError("LeafNode must have a value to convert to HTML")
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

        
        
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        props_html = self.props_to_html()
        if self.tag is None:
            raise ValueError("ParentNode must have a tag to convert to HTML")
        if self.children is None:
            raise ValueError("ParentNode must have children to convert to HTML")
        for child in self.children:
            if not isinstance(child, HTMLNode):
                raise ValueError("All children of ParentNode must be HTMLNode instances")
            return f"<{self.tag}{props_html}>" + "".join(child.to_html() for child in self.children) + f"</{self.tag}>"
        
    def add_child(self, child):
        if self.children is None:
            self.children = []
        self.children.append(child)
        
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
    

