class linkedList(object):
    def __init__(self):
        self.head = None
    
    # 노드추가
    def append(self,value):
        new_Node = Node(value)
        if(self.head is None):
            self.head = new_Node
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_Node
            
            
    # 주소록 목록 보여주기
    def getlist(self):
        point = self.head
        while point:
            v = point.value
            point = point.next
            print(v)
            
            
    # 주소록 삭제 
    def delNode(self, n):
        # 첫번째 노드를 지울때
        if n == 1:
            preNode = self.head.next
            self.head = preNode
               
        # 그 이외 노드를 지울때 
        else:
            # n+1번째 노드를 찾는 코드
            postNode = self.head
            for i in range(1, n+1):
                postNode = postNode.next
            # n-1번째 노드를 찾는 코드    
            preNode = self.head
            for i in range(1, n-1):
                preNode = preNode.next
            preNode.next = postNode
            
            
    # 주소록 업데이트 
    def update(self,num,name):
        if(num==1):
            self.head.value=name
        else:
            point = self.head
            for i in range(1,num):
                point= point.next
            point.value = name

            
# 노드 클래스
class Node:
    def __init__(self,value=0 , next=None):
        self.value=value
        self.next=next
            
ll = linkedList()            
            
# 구현부
while True:
    menue = int(input("1.추가 , 2.수정 , 3.삭제, 4.주소록 목록 보기 5.종료 : "))
    
    if(menue==5):
        break
    
    elif(menue==1):
        name = input("이름을 입력해주세요 : ")
        ll.append(name)
    
    elif(menue==2):
        num,name=input("몇번째 주소록을 수정하시겠습니까?,어떤 이름으로 수정하시겠습니까?(쉼표로 구분해서 작성해주세요) : ").split(",")
        num = int(num)
        ll.update(num , name)
        ll.getlist()
    
    elif (menue == 3):
        num = int(input("몇 번 데이터를 삭제하시겠습니까? : "))
        if ll.head:
            ll.delNode(num)
            ll.getlist()
        else:
            print("주소록이 비어 있습니다.")
  
    elif(menue==4):
        if ll.head:
            ll.getlist()
        else:
            print("주소록이 비어 있습니다.")  
    else:
        break
           
