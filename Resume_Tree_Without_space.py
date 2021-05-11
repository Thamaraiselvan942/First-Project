class Node:
  def __init__(self,val):
    self.data=val
    self.children=[]
    self.parent=None
  
  def add_child(self,child):
    child.parent=self
    self.children.append(child)
  def get_level(self):
    level=0
    p=self.parent
    while p:
      p=p.parent
      level+=1
    return level
  def print_tree(self):
    space=' '*self.get_level()*3
    prefix=space+"|__" if self.parent else "  "
    print(prefix+self.data)
    
    if self.children:
      for i in self.children:
        i.print_tree()
 
def build_resume():
  root=Node("RESUME TREE")
  #=========================================
  pd=Node("PERSONAL DETIALS")
  pd.add_child(Node("Name:P.Thamaraiselvan"))
  pd.add_child(Node("Father's Name:C.Prakasam"))
  pd.add_child(Node("Mother's Name:P.Sasikala"))
  pd.add_child(Node("Date of Birth:21.07.2000 "))
  pd.add_child(Node("Gender:Male"))
  pd.add_child(Node("Marital Status:Unmarried"))
  pd.add_child(Node("Nationality:Indian"))
  pd.add_child(Node("Language:Tamil,English"))

  #=========================================
  aq=Node("ACADEMIC QUALIFICATION")
  c1=Node("B.E (ECE)")
  c1.add_child(Node("College:Kongunadu College Of Engineering And Technology"))
  c1.add_child((Node("Aggrigation: 81%")))
  c1.add_child(Node("Year:2022"))
  #=========================================
  c2=Node("HSC")
  c2.add_child(Node("Vaagai Vidhiyalaya Matric H.S.School"))
  c2.add_child(Node("Aggrigation:86.5%"))
  c2.add_child(Node("Year:2018"))
  #=========================================
  c3=Node("SSLC")
  c3.add_child(Node("Vaagai Vidhiyalaya Matric H.S.School"))
  c3.add_child(Node("Aggrigation:88.6"))
  c3.add_child(Node("Year:2016"))
  #===========================================
  aq.add_child(c1)
  aq.add_child(c2)
  aq.add_child(c3)
  #============================================
  P=Node("PROJECT")
  P.add_child(Node("Plant Disease Detection"))
  P.add_child(Node("Object Detection Using Python"))
  P.add_child(Node("Gesture Controlled Robotic Hand"))
  #============================================
  sk=Node("SKILLS & STRENGTH")
  sk.add_child(Node("Good TeamPlayer"))
  sk.add_child(Node("Self Motivated"))
  sk.add_child(Node("Hard Worker"))
  sk.add_child(Node("Leadership"))
  #==============================================
  T=Node("TECHNICAL SKILLS")
  T.add_child(Node("OS:Windows,Linux"))
  T.add_child(Node("Language:Python,C"))
  T.add_child(Node("Software & Hardware:Arduino,RaspberryPi,IOT,Matlab"))
  #===============================================
  A=Node("AREA OF INTREST")
  A.add_child(Node("Networking"))
  A.add_child(Node("Ethical Hacking"))
  #===============================================
  C=Node("CERTIFICATION")
  C.add_child(Node("CCNA Certified By CISCO"))
  C.add_child(Node("PLC & SCADA Internship"))
  #===============================================
  root.add_child(pd)
  root.add_child(aq)
  root.add_child(P)
  root.add_child(sk)
  root.add_child(T)
  root.add_child(A)
  root.add_child(C)

  return root
if __name__=='__main__':
  root=build_resume()
  r=root.print_tree()
  



