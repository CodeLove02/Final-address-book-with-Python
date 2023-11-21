# linkedList를 활용한 주소록 프로그램

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
            
            
# 주소록 목록 보여주기(chatgpt)
class getlist:
    def __init__(self, point=None):
        self.point = point

    def getlist(self):
        point = self.point
        while point:
            v = point.value
            point = point.next
            print(v)
            

#주소록 업데이트하기
class update:
    def __init__(self,point):
        self.point = point
        
    def update(self,num,name):
        if(num==1):
            self.point.value=name
        else:
            for i in range(1,num):
                self.point=self.point.next
            self.point.value=name

            


# n은 지우고싶은 데이터의 순서번호
# node는 첫번째 노드를 의미하므로 n번째 노드를 가리키기 위해서는 n-1번 (node.next) 를 수행. for문에서 끝자리수-1이므로 n 써주면 됨
# 하지만 그 전 노드를 가리켜야 하므로 for문 끝자리수:n-1 


# global preNode 
# preNode = ll.head
# global postNode 
# postNode = ll.head
# linkedList 연결해제(내가한거)



class delete():
    def __init__(self, point=None):
        self.preNode = point
        self.postNode = point
    def delNode(self, n):
        # 첫번째 노드를 지울때
        if n == 1:
            
                self.preNode = self.preNode.next
                ll.head = self.preNode
                list_instance.point = self.preNode    
        # 그 이외 노드를 지울때 
        else:
            # n+1번째 노드를 찾는 코드
            for i in range(1, n+1):
                self.postNode = self.postNode.next
            # n-1번째 노드를 찾는 코드    
            for i in range(1, n-1):
                self.preNode = self.preNode.next
            self.preNode.next = self.postNode



ll = linkedList()
list_instance = getlist(ll.head)
dl = delete(ll.head)


# 구현부
while True:
    menue = int(input("1.추가 , 2.수정 , 3.삭제, 4.주소록 목록 보기 5.종료"))
    
    if(menue==5):
        break
    
    elif(menue==1):
        name = input("이름을 입력해주세요")
        ll.append(name)
    
    elif(menue==2):
        num,name=input("몇번째 주소록을 수정하시겠습니까?,어떤 이름으로 수정하시겠습니까?(쉼표로 구분해서 작성해주세요)").split(",")
        num = int(num)
        ud = update(ll.head)
        ud.update(num,name)
        list_instance.getlist()
    
    elif (menue == 3):
        num = int(input("몇 번 데이터를 삭제하시겠습니까?"))
        if ll.head:
            dl = delete(ll.head)
            dl.delNode(num)
            list_instance.getlist()
        else:
            print("주소록이 비어 있습니다.")
  
    
    elif(menue==4):
        if ll.head:
            list_instance = getlist(ll.head)
            list_instance.getlist()
        else:
            print("주소록이 비어 있습니다.")  
    else:
        break
