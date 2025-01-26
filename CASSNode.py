class CassNode:
    def __init__(self, label):
        """
        label: The string label for this node, e.g. "#VAR", "for($S;$S$)$", "return", etc.
        """
        self.label = label
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def to_cass_string(self) -> str:
        """
        Recursively produce a textual representation for debugging
        or for MISIM consumption, depending on how you format it.
        """
        # Example approach: label(child1(...) child2(...) ...)
        child_strings = [c.to_cass_string() for c in self.children]
        # You can adapt parentheses, placeholders, etc. to match your official CASS format
        return f"{self.label}({','.join(child_strings)})"

    def to_dot(self, node_id=0, parent_id=None, lines=None):
        """
        Recursively produce GraphViz DOT notation for rendering a PNG.
        """
        if lines is None:
            lines = ["digraph CASS {", "  node [shape=ellipse];"]

        current_id = node_id
        # Escape double quotes in label if necessary
        safe_label = self.label.replace('"', '\\"')
        lines.append(f'  n{current_id} [label="[{node_id}]:   {safe_label}"];')

        if parent_id is not None:
            lines.append(f'  n{parent_id} -> n{current_id};')

        next_id = current_id + 1
        for child in self.children:
            next_id = child.to_dot(next_id, current_id, lines)

        if parent_id is None:
            lines.insert(0, "digraph cass {")
            lines.insert(1, "  node [shape=ellipse];")
            lines.append("}")
        return next_id

