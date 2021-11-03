import sys
#min heap

class MinHeap:
    def __init__(self,maxsize):
        self.maxisize = maxsize
        self.size =0
        self.Heap = [0] * (self.maxisize+1)
        self.Heap[0] = -1 *sys.maxsize
        self.FRONT =1

    def parent(self,pos):
        return pos //2

    def left_child(self,pos):
        return  2*pos
    def right_child(selfs,pos):
        return  (2*pos)+1

    def swap(self,pos1,pos2):
        self.Heap[pos1],self.Heap[pos2]=self.Heap[pos2],self.Heap[pos1]

    def is_leaf(self,pos):
        if pos >self.size//2 and self.pos <self.size:
            return True
        return False

    def min_heaqify(self,pos):
        if self.Heap[pos] > self.left_child(self.Heap) or     self.Heap[pos] > self.right_child(self.Heap) :

            if self.Heap[pos] > self.left_child(self.Heap):
                self.swap(pos,self.left_child(self.Heap))
                self.min_heaqify(self.left_child(self.Heap))

            if self.Heap[pos] > self.right_child(self.Heap):
                self.swap(pos,self.right_child(self.Heap))
                self.min_heaqify(self.right_child(self.Heap))


    def insert(self,node):
        self.size+=1
        if self.size>self.maxisize:
            return False
        self.Heap.append(node)


        curr = self.size

        while self.Heap[curr] > self.parent(self.Heap[curr]):
            self.swap(self.Heap[curr],self.parent(self.Heap[curr] ))
            curr = self.parent(self.Heap[curr] )

    def remove(self):
        self.swap(self.Heap[self.FRONT],self.Heap[self.size])
        popped=self.size
        self.size-=1
        self.min_heaqify(self.FRONT)
        return popped




