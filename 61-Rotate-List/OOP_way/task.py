
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.last_node = False

    def set_val(self, new_val):
        self.val = new_val
        return

    def set_next(self, new_next):
        self.next = new_next
        return

    def print_node(self):
        print('Node - val:', self.val, ', next:', self.next)
        return


class Solution:
    def __init__(self, input = "1->2->3->4->5->NULL", k = 2):
        self.input = input
        self.k = k

    def rotateRight(self, nodeList, k: int) -> ListNode:
        print('before:')
        self.print_node_list(nodeList)

        while(k > 0):
            print('op:')
            for node in range(0, len(nodeList)):
                #nodeList[node]
                nodeList[node].set_val()
                #1,2; 2,3; 3,4; 4,5;
                continue

            self.print_node_list(nodeList)
            k -= 1
        return

    def print_node_list(self, nodeList):
        for node in nodeList:
            node.print_node()
        print('')

    def read_input(self):
        array_of_nodes = self.input.split('->')
        return array_of_nodes

    def create_nodes(self, array_of_nodes):
        list_of_nodes = []
        for i in range(0, len(array_of_nodes) - 2):
            list_of_nodes.append(ListNode(array_of_nodes[i], array_of_nodes[i+1]))

        return list_of_nodes

    def task(self):
        array_of_nodes = self.read_input()
        list_of_nodes = self.create_nodes(array_of_nodes)
        self.rotateRight(list_of_nodes, self.k)
