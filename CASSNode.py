class CassNode:
    def __init__(self, label):

        self.label = str(label)
        self.children = []
        self.prevUse = -1 # keep track of the prev node usage
        self.nextUse = -1

    def add_child(self, child):
        self.children.append(child)

    # Creating the Cass string
    def to_cass_string(self) -> str:

         # Appending nodes with appropriate suffixes :
        # -> LocalVar v, LocalFun f : previously used in node_nr, next used in current node_nr
        # -> NumLit, CharLit, StringLit, GlobalVar : None
        # -> Internal : children size
        
        child_strings = [c.to_cass_string() for c in self.children]
        if self.label == "removed":
            return "".join(child_strings)
        
        if self.label.startswith("v"):
            return (f"{self.label}\\t{self.prevUse}\\t{self.nextUse}\\t" +
                    "".join(child_strings))
        
        if self.label.startswith("V"):
            return f"{self.label}\\t" + "".join(child_strings)
        
        if self.label.startswith(("N", "C", "S", "F")):
            return f"{self.label}\\t" + "".join(child_strings)

        # 5) Include the label for non-removed nodes
        child_count = len(self.children)
        return f"{self.label}\\t{child_count}\\t" + "".join(child_strings)
        
    
        
    # Getting all nodes in a Cass tree
    def get_node_count(self) -> int:
        
        node_counter = {"current_id": 1}  # Start numbering at 1
        total_nodes = 0

        def traverse(node):
            nonlocal total_nodes
            current_id = node_counter["current_id"]

            if node.label != "removed":
                node_counter["current_id"] += 1
                total_nodes += 1

            for child in node.children:
                traverse(child)


        traverse(self)

        return total_nodes
    
    # Generating a GraphViz DOT file with nodes numbered in the CASS-style creation order
    def to_dot(self):
        
        lines = ["digraph CASS {", "  node [shape=ellipse];"]
        node_counter = {"current_id": 1}  # Start numbering at 1
        edges = []

        def traverse(node, parent_id=None):
            
            current_id = node_counter["current_id"]
            
            if node.label != 'removed':
                
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

        traverse(self)

        # Add edges to the DOT file
        lines.extend(edges[1:])
    
        # Close the DOT graph
        lines.append("}")

        return lines
    

"""
    1) Numbering the nodes according to preorder Depth First Search Algorithm.
    2) For each node referencing a local variable (label 'vX'), record it in usage_map.
    3) After collecting, fill in .prevUse and .nextUse.
"""   

def assign_usage_links(root: CassNode):
    
    usage_map = {}

    current_id = [1] 

    def dfs(node: CassNode):
        
        if (node.label != "removed"):
            this_index = current_id[0]
            current_id[0] += 1

            # If it's a local variable usage, store in usage_map
            if node.label.startswith("v"):
                var_name = node.label[1:]  # "vsum" => "sum"
                if var_name not in usage_map:
                    usage_map[var_name] = []
                usage_map[var_name].append((this_index, node))

            # Recurse on children
            for child in node.children:
                dfs(child)
        else:
            
            for child in node.children:
                dfs(child)

    # Collect usage in a DFS
    dfs(root)

    # For each variable, link up usage
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