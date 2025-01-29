class CassNode:
    def __init__(self, label):
        """
        label: The string label for this node, e.g. "#VAR", "for($S;$S$)$", "return", etc.
        """
        self.label = str(label)
        self.children = []
        self.prevUse = -1 #keep track of the prev node usage
        self.nextUse = -1

    def add_child(self, child):
        self.children.append(child)

    def to_cass_string(self) -> str:
        
        child_strings = [c.to_cass_string() for c in self.children]
        if self.label == "removed":
            return "".join(child_strings)
        
        if self.label.startswith("v"):
            return (f"{self.label}\\t{self.prevUse}\\t{self.nextUse}\\t" +
                    "".join(child_strings))
        
        if self.label.startswith("V"):
            return f"{self.label}\\t" + "".join(child_strings)
        
        if self.label.startswith(("N", "C", "S")):
            return f"{self.label}\\t" + "".join(child_strings)

        # 5) Include the label for non-removed nodes
        child_count = len(self.children)
        return f"{self.label}\\t{child_count}\\t" + "".join(child_strings)
        
    def get_node_count(self) -> int:
        """
        Computes the total number of valid nodes in the graph as seen by to_dot().
        Counts all nodes except those labeled 'removed'.
        """
        node_counter = {"current_id": 1}  # Start numbering at 1
        total_nodes = 0

        def traverse(node):
            nonlocal total_nodes
            current_id = node_counter["current_id"]

            # If the node is valid (not removed or numeric-only), count it
            if not node.label.lstrip('-').isdigit() and node.label != "removed":
                node_counter["current_id"] += 1
                total_nodes += 1

            # Visit children
            for child in node.children:
                traverse(child)

        # Start traversal from the root
        traverse(self)

        return total_nodes

    def to_dot(self):
        """
        Generate a GraphViz DOT file with nodes numbered in the CASS-style creation order.
        """
        lines = ["digraph CASS {", "  node [shape=ellipse];"]
        node_counter = {"current_id": 1}  # Start numbering at 1
        edges = []

        def traverse(node, parent_id=None):
            
            current_id = node_counter["current_id"]
            

            # Assign the current node's ID
            if (not(node.label.lstrip('-').isdigit()) and not(node.label == 'removed')):
                
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
            
            else: 

                for child in node.children:
                    traverse(child, current_id)

                return current_id

        # Start traversal from the root
        traverse(self)

        # Add edges to the DOT file
        lines.extend(edges[1:])
    

        # Close the DOT graph
        lines.append("}")

        return lines
    
    

def assign_usage_links(root: CassNode):
    """
    1) Do a DFS or BFS over 'root' in the same order you produce your final numbering.
    2) For each node referencing a local variable (label 'vX'), record it in usage_map.
    3) After collecting, fill in .prevUse and .nextUse.
    """

    # usage_map: varName -> list of (sequentialIndex, nodeObj)
    usage_map = {}

    # We'll track an incremental index to replicate the order you see in .to_cass_string
    # Because .to_cass_string calls get_node_count first, then it visits children in order.
    # So let's do a simple pre-order DFS. 
    # If you want EXACT matching with your existing "node numbering," 
    # you may replicate the logic from get_node_count/to_dot, etc.
    current_id = [1]  # store in a list so we can increment in nested function

    def dfs(node: CassNode):
        # If this node is "valid" (not "removed", not purely numeric, etc.):
        if (node.label != "removed" and not node.label.lstrip('-').isdigit()):
            this_index = current_id[0]
            current_id[0] += 1

            # If it's a local variable usage, store in usage_map
            if node.label.startswith("v"):
                var_name = node.label[1:]  # e.g. "vsum" => "sum"
                if var_name not in usage_map:
                    usage_map[var_name] = []
                usage_map[var_name].append((this_index, node))

            # Recurse on children
            for child in node.children:
                dfs(child)
        else:
            # Even if it's "removed" or numeric, we want to DFS into children
            # if you want to skip children for certain nodes, do so carefully
            for child in node.children:
                dfs(child)

    # 1) Collect usage in a DFS
    dfs(root)

    # 2) For each variable, link up usage
    for var_name, usage_list in usage_map.items():
        # usage_list is e.g. [(4, nodeObj), (8, nodeObj), (21, nodeObj)]
        for i, (this_idx, node_obj) in enumerate(usage_list):
            # prev
            if i > 0:
                prev_idx = usage_list[i-1][0]
                node_obj.prevUse = prev_idx
            else:
                node_obj.prevUse = -1

            # next
            if i < len(usage_list)-1:
                next_idx = usage_list[i+1][0]
                node_obj.nextUse = next_idx
            else:
                node_obj.nextUse = -1