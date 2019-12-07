from anytree import Node, RenderTree, AsciiStyle, PreOrderIter, Walker
from anytree.cachedsearch import find, findall


def count_orbits(input):
    root = build_orbit_tree(input.split())

    # print(RenderTree(root, style=AsciiStyle()).by_attr())

    count = 0
    for node in PreOrderIter(root):
        current_node = node
        while(current_node.parent != None):
            count = count + 1
            current_node = current_node.parent

    return count


def build_orbit_tree(input_tokens):
    root = Node("COM")
    while(len(input_tokens) > 0):
        # print(len(input_tokens), " to go")
        token = input_tokens.pop(0)
        parent = find(root, lambda node: node.name == token.split(")")[0])
        if (parent != None):
            Node(token.split(")")[1], parent=parent)
        else:
            input_tokens.append(token)
    return root


def count_transits(from_name, to_name, input):
    root = build_orbit_tree(input.split())

    # print(RenderTree(root, style=AsciiStyle()).by_attr())

    from_node = find(root, lambda node: node.name == from_name).parent
    to_node = find(root, lambda node: node.name == to_name).parent

    walker = Walker()
    (upwards, _, downwards) = walker.walk(from_node, to_node)
    return (len(upwards) + len(downwards))
