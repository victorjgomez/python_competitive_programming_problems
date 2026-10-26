class PriorityQueue:

    # Class constructor
    def __init__(self):
        # Members of
        self.heap = []
        self.data_dict = {}

        # Additional code here

    # Insert or update item with priority and data given
    def insert_or_update(self, priority, data):
        if(data in self.data_dict):
            if(self.heap[self.data_dict[data]][0] > priority):
                self.heap[self.data_dict[data]]=(priority,data)
                self.update(self.data_dict[data])

        else:
            self.data_dict[data] = len(self.heap)
            self.heap.append((priority, data))
            self.silf_up(len(self.heap)-1)


    # Extract element with lowest priority value
    # Return the element as tuple (priority, data)
    def extract(self):
        if(self.is_empty() == False):
            min_element = self.heap[0]
            del self.data_dict[self.heap[0][1]] #Eliminado elemento del diccionario
            if(self.__len__()>1):
                self.heap[0]=self.heap[len(self.heap)-1]
                self.data_dict[self.heap[0][1]]=0

            if(self.__len__()==1):
                self.heap.pop()

            else:
                self.heap.pop(len(self.heap)-1)
                self.silf_down(0)

            return min_element
        else:
            return None


    # Return the element with lowest priority
    # as a tuple (priority, data)
    # DO NOT REMOVE from queue
    def peek(self):
        if(self.is_empty()):
            return None
        else:
            return self.heap[0]

    # Return a string representing the internal state
    def __str__(self):
        print(self.heap)
        print(" ")
        print(self.data_dict)


    # Return number of elements in the queue
    def __len__(self):
        return len(self.heap)

    # Return True if queue is empty, False otherwise
    def is_empty(self):
        # Return queue is empty
        if(len(self.heap) == 0):
            return True
        else:
            return False

    # This function performs a silf_up to the element indicated in by the index.
    def silf_up(self,index):
        parent = int((index-1)/2)
        child = index

        while(parent>=0):
            if(self.heap[child][0]<self.heap[parent][0]):
                self.data_dict[self.heap[child][1]] = parent
                self.data_dict[self.heap[parent][1]] = child

                self.swapPositions(child,parent)
                child = parent
                parent = int((child-1)/2)

            else:
                return

    # This function performs an exchange in position between two elements given their indices.
    def swapPositions(self, pos1, pos2):
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]

    # This is an auxiliary function for print_tree.
    def childNodes(self,i):
        return (2 * i) + 1, (2 * i) + 2

    # This is a feature features the tree shaped mound aids in debugging.
    def print_tree(self, i=0, d=0):
        if i >= len(self.heap):
            return
        l, r = self.childNodes(i)
        self.print_tree(r, d=d + 1)
        print("   " * d + str(self.heap[i][0]))
        self.print_tree(l, d=d + 1)

    # This function performs a silf_down to the element indicated in by the index.
    def silf_down(self,index):
        parent = index
        left_child = 2 * parent + 1
        right_child = 2 * parent + 2

        while(right_child<len(self.heap)):
            if(self.heap[parent][0]>min(self.heap[left_child][0],self.heap[right_child][0])):
                youngest_son_index = self.youngest_child_ind(left_child,right_child)

                self.data_dict[self.heap[parent][1]] = youngest_son_index
                self.data_dict[self.heap[youngest_son_index][1]] = parent

                self.swapPositions(parent,youngest_son_index)
                parent = youngest_son_index
                left_child = 2 * parent + 1
                right_child = 2 * parent + 2
            else:
                return

        if(left_child<len(self.heap)):
            if (self.heap[parent][0] > self.heap[left_child][0]):
                self.data_dict[self.heap[parent][1]] = left_child
                self.data_dict[self.heap[left_child][1]] = parent

                self.swapPositions(parent,left_child)


    # This is a function returns the index of the youngest child.
    def youngest_child_ind(self,left_child,right_child):
        if(self.heap[left_child][0]<self.heap[right_child][0]):
            return left_child
        else:
            return right_child

    # This function performs a heap update if necessary.
    def update(self,index):
        my_parent = int((index-1)/2)

        if(my_parent>=0):
           if(self.heap[index][0]<self.heap[my_parent][0]):
             self.silf_up(index)




