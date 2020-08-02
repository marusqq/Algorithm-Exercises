def rotate_right(string, times):

    nodes = string.split('->')
    
    while(times):
        nodes = rotate(nodes)
        times -= 1 


    return '->'.join(nodes)

def rotate(nodes):

    nodes.remove('NULL')
    rotated_nodes = []

    if len(nodes) == 0:
        return nodes

    last = nodes[len(nodes) - 1]
    nodes.remove(last)
    rotated_nodes.append(last)

    for node in nodes:
        rotated_nodes.append(node)

    rotated_nodes.append('NULL')

    return rotated_nodes