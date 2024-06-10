class HTMLNode:
    def __init__(self, tag:str=None, value:str=None, children:list=None, props:dict=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        result_str = ' '.join(f'{k}="{v}"' for k, v in self.props.items())
        return result_str
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None) -> None:
        super().__init__(tag, value, None, props)
    
    def to_html(self) -> str:
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        props = self.props_to_html()
        if props:
            props = " " + props
        return f"<{self.tag}{props}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag:str, children: list, props: dict = None) -> None:
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is not provided")
        if self.children is None:
            raise ValueError("Parent nodes must have children")
        children_html = "".join(node.to_html() for node in self.children)
        return f'<{self.tag}>{children_html}</{self.tag}>'
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
    
