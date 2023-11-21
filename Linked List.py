# 첫번째 링크드리스트 구현

# class LinkedList(object):
#     def __init__(self):
#         self.head = None
        
#     past = None
#     current = None

#     def append(self, v):
#         global current 
#         global past
#         if(past is None) :
            
#             current = Node(v)
#             past = current
        
#         current = Node(v)
        

#         if self.head is None:
#             self.head = current
            
#         else:
#             past.A = current
#             past = current


     
# class Node :
#     def __init__(self , A=None , V=0) :
#         self.A = A
#         self.V = V


# ll = LinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.append(4)


# 두번째 링크드리스트 구현


class linkedList(object):
    def __init__(self):
        self.head = None
    def append(self,value):
        new_Node = Node(value)
        if(self.head is None):
            self.head = new_Node
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_Node
            
class Node:
    def __init__(self,value=0 , next=None):
        self.value=value
        self.next=next

ll = linkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)


n = int(input("몇번째 데이터를 원합니까?"))

node = ll.head
for i in range(1,n):
    node=node.next

n = str(n)    
valueOfNode = str(node.value)
print(n + "번째 데이터 : " + valueOfNode)




# 네, 주어진 코드도 링크드 리스트를 구현하고 있습니다.

# 주어진 코드와 이전에 제공된 코드 간에는 몇 가지 차이가 있습니다. 다음은 두 가지 구현 방식의 차이점과 효율성에 대한 설명입니다:

# 헤드 노드 저장 방식:

# 이전 코드: 이전 코드에서는 past와 current 변수를 사용하여 헤드 노드를 저장하고, 노드를 추가할 때 past와 current를 업데이트하는 방식을 사용했습니다.
# 현재 코드: 현재 코드에서는 self.head 변수를 사용하여 헤드 노드를 직접 저장합니다. 노드를 추가할 때 self.head를 기준으로 마지막 노드를 찾아 새로운 노드를 추가합니다.
# 노드 추가 방식:

# 이전 코드: 이전 코드에서는 past와 current 변수를 사용하여 노드를 추가하고 연결했습니다.
# 현재 코드: 현재 코드에서는 next 속성을 사용하여 노드를 추가하고 연결했습니다.
# 효율성 측면에서는 현재 코드가 더 효율적입니다. 이유는 다음과 같습니다:

# 헤드 노드 저장 방식: 현재 코드에서는 헤드 노드를 self.head 변수에 직접 저장하여 접근하므로, 헤드 노드에 대한 접근과 업데이트가 간단하고 효율적입니다.

# 노드 추가 방식: 현재 코드에서는 노드를 추가할 때 next 속성을 사용하여 연결합니다. 이 방식은 현재 노드에서 다음 노드로 직접 연결되므로, 마지막 노드를 찾기 위해 반복문을 사용하지 않아도 됩니다. 따라서, 노드 추가 작업의 시간 복잡도가 더 낮아 효율적입니다.

# 따라서, 주어진 두 가지 구현 방식 중 현재 코드가 더 효율적인 코드입니다.
        
