from anytree import Node, find, findall, RenderTree, AsciiStyle, PreOrderIter

def count_orbits(input):
    root = Node("COM")
    input_tokens = input.split()

    while(len(input_tokens) > 0):
        print(len(input_tokens), " to go")
        token = input_tokens.pop(0);
        parent = find(root, lambda node: node.name == token.split(")")[0])
        if (parent != None):
            Node(token.split(")")[1], parent=parent)
        else:
            input_tokens.append(token)

    # print(RenderTree(root, style=AsciiStyle()).by_attr())

    count = 0;
    for node in PreOrderIter(root):
        current_node = node
        while(current_node.parent != None):
            count = count + 1
            current_node = current_node.parent

    return count