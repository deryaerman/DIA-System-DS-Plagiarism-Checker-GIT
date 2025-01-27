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
        return f"{self.label}({'/t'.join(child_strings)})"

    def to_dot(self):
        """
        Generate a GraphViz DOT file with nodes numbered in the CASS-style creation order.
        """
        lines = ["digraph CASS {", "  node [shape=ellipse];"]
        node_counter = {"current_id": 1}  # Start numbering at 1
        edges = []

        def traverse(node, parent_id=None):
            # Assign the current node's ID
            current_id = node_counter["current_id"]
            node_counter["current_id"] += 1

            # Escape double quotes in label if necessary
            safe_label = node.label.replace('"', '\\"')
            lines.append(f'  n{current_id} [label="[{current_id}]: {safe_label}"];')

            # Create an edge from parent to the current node
            if parent_id is not None:
                edges.append(f'  n{parent_id} -> n{current_id};')

            # Visit children in the order they were added
            for child in node.children:
                traverse(child, current_id)

            return current_id

        # Start traversal from the root
        traverse(self)

        # Add edges to the DOT file
        lines.extend(edges)

        # Close the DOT graph
        lines.append("}")

        return lines
    
    

