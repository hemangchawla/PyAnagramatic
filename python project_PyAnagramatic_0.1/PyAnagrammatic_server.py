import pygame
from pygame.locals import *
from random import *
import inputbox, inputbox2
import time
import socket
from sys import exit


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


mainloop, x,y, color, fontsize, delta, fps =  True, 60 , 0, (32,32,32), 35, 1, 1
back="s1.jpg" #back=background img
w_w="waiting.jpg"
m1=[]         #loaded vovels list
m2=[]         #loaded consonants list
v=["a.gif","e.gif","i.gif","o.gif","u.gif","v2.jpg"]
c=["b.gif","c.gif","d.gif","f.gif","g.gif","h.gif","j.gif","k.gif","l.gif","m.gif","n.gif","p.gif","q.gif","r.gif","s.gif","t.gif","v.gif","w.gif","x.gif","y.gif","z.gif","c2.jpg"]     
k=0 # used for adding letter from lower to upper row
i1=0 # used for displaying of letters in the lower list in appropriate sizes
llist,ulist=[],[]
k2=0
vclick,cclick,p2=0,0,0
n=range(10)
flag_s=False
flag_c= False

pygame.display.set_caption("Py.Anagramatic")

pygame.init()

pygame.mixer.init()    # For Sounds
sound = pygame.mixer.Sound("music.ogg")
sound.play(-1)

pl_name=inputbox.main()  # For name
print "Hello, %s"%pl_name

p=inputbox2.main()  #for ipv4
print "Ip = %s"%p

server.bind((p, 5051))
server.listen(1)

screen=pygame.display.set_mode((1000,650),0,32) #waiting
background = pygame.image.load(back).convert()
wait= pygame.image.load(w_w).convert()
screen.blit(wait,(0,0))
screen.blit(pygame.transform.scale(pygame.image.load("logo.png"),(200,146)),(800,0))
pygame.display.update()

tup=server.accept()
ne=tup[0]

pygame.display.set_caption("Py.Anagramatic(S)")

screen=pygame.display.set_mode((1000,650),0,32) #main game window starts
background = pygame.image.load(back).convert()

for i in range(6):
       m1.append(pygame.image.load(v[i]))
for i in range(22):
       m2.append(pygame.image.load(c[i]))

       
 #Background
screen.blit(background, (0,0))
screen.blit(pygame.transform.scale(pygame.image.load("logo.png"),(200,146)),(800,0))
# 18 empty squares
for i in range(9):
       pygame.draw.rect(screen,(255,255,255),Rect((130+(i*65),380), (45,45)))
       pygame.draw.rect(screen,(255,255,255),Rect((130+(i*65),150), (45,45)))

pygame.draw.rect(screen,(0,255,0),Rect((800,0), (0,650)),5)

running, x,y=  True, 390 ,260 
fontsize =69
myFont = pygame.font.SysFont("None", fontsize)
color = (50,50,50)
lt=[]
t=0
for z in range(60,-1,-1):
       lt.append("%s"%z)


ne.send(pl_name)
clien=ne.recv(2048)
       
while True:
       if  t>59:
              timeup=True
       else:
              timeup=False

              

       if len(llist)==9:
              
              if running==True :
                     time.sleep(1)
                     screen.blit(pygame.image.load("clock.png"),(350.25,220))
                     screen.blit(myFont.render(lt[t], 0, (color)), (x,y))
                     if t<=59:
                            t+=1
                            
       
       
       for event in pygame.event.get():
              if event.type == QUIT:
                     #pygame.quit() #does not hang
                     exit() 
              if event.type==MOUSEBUTTONDOWN:
                     Click()       

      

       # Letters V & C
       pygame.draw.rect(screen,(255,255,255),Rect((245,445), (90,90)),2)
       pygame.draw.rect(screen,(255,255,255),Rect((445,445), (90,90)),2) 
       screen.blit(m1[5],(260,460))
       screen.blit(m2[21],(460,460))
       screen.blit(pygame.image.load("round.gif"),(200,0))
       screen.blit(pygame.image.load("1.gif"),(600,20))
       
       pygame.display.update()
       if timeup==True:
                       col=(255,255,255)
                       scree=pygame.display.set_mode((900,650),0,32)
                       backgroun = pygame.image.load("s2.jpg").convert()
                       fle=open("Dict/%s/%s%s.txt"%tuple(["%d"%len(ulist),"%d"%len(ulist),ulist[0]]))
                       word_l= fle.read()
                       wo=''
                       da=ne.recv(2048)
                       print da
                       fle2=open("Dict/%s/%s%s.txt"%tuple(["%d"%len(da),"%d"%len(da),da[0]]))
                       cl_l=fle2.read()
                       for u in range(len(ulist)):
                                     wo+=ulist[u]

                       ne.send(wo)
                       for u in range(len(word_l.split())):
                                   if (wo==word_l.split()[u]):
                                          flag_s=True
                       for u in range(len(cl_l.split())):
                                   if (da==cl_l.split()[u]):
                                          flag_c=True
                       if(flag_c==True and flag_s==True):
                              if(len(wo)<len(da)):
                                     ne.send("1_1")
                                     fsize=60
                                     mf= pygame.font.SysFont("None", fsize)
                                     scree.blit(backgroun, (0,0))
                                     scree.blit(mf.render(pl_name,0,(col)),(20,200))
                                     scree.blit(mf.render(clien,0,(col)),(20,400))
                                     scree.blit(mf.render(wo,0,(col)),(200,200))
                                     scree.blit(mf.render(da,0,(col)),(200,400))
                                     scree.blit(mf.render("%s Wins"%clien,0,(col)),(600,300))
                                     screen.blit(pygame.image.load("tick.jpg"),(600,200))
                                     screen.blit(pygame.image.load("tick.jpg"),(600,400))
                                     pygame.display.update()
                                     time.sleep(11)
                                     exit()
                                                 
                              elif(len(wo)>len(da)):
                                     ne.send("1_2")
                                     fsize=60
                                     mf= pygame.font.SysFont("None", fsize)
                                     scree.blit(backgroun, (0,0))
                                     scree.blit(mf.render(pl_name,0,(col)),(20,200))
                                     scree.blit(mf.render(clien,0,(col)),(20,400))
                                     scree.blit(mf.render(wo,0,(col)),(200,200))
                                     scree.blit(mf.render(da,0,(col)),(200,400))
                                     scree.blit(mf.render("%s Wins"%pl_name,0,(col)),(600,300))
                                     screen.blit(pygame.image.load("tick.jpg"),(600,200))
                                     screen.blit(pygame.image.load("tick.jpg"),(600,400))
                                     pygame.display.update()
                                     time.sleep(11)
                                     exit()
                              else:
                                     ne.send("1_3")
                                     fsize=60
                                     mf= pygame.font.SysFont("None", fsize)
                                     scree.blit(backgroun, (0,0))
                                     scree.blit(mf.render(pl_name,0,(col)),(20,200))
                                     scree.blit(mf.render(clien,0,(col)),(20,400))
                                     scree.blit(mf.render(wo,0,(col)),(200,200))
                                     scree.blit(mf.render(da,0,(col)),(200,400))
                                     scree.blit(mf.render("Game Tied",0,(col)),(600,300))
                                     screen.blit(pygame.image.load("tick.jpg"),(600,200))
                                     screen.blit(pygame.image.load("tick.jpg"),(600,400))
                                     pygame.display.update()
                                     time.sleep(11)
                                     exit()
                       elif(flag_c==False and flag_s==True):
                              ne.send("2")
                              fsize=60
                              mf= pygame.font.SysFont("None", fsize)
                              scree.blit(backgroun, (0,0))
                              scree.blit(mf.render(pl_name,0,(col)),(20,200))
                              scree.blit(mf.render(clien,0,(col)),(20,400))
                              scree.blit(mf.render(wo,0,(col)),(200,200))
                              scree.blit(mf.render(da,0,(col)),(200,400))
                              scree.blit(mf.render("%s Wins"%pl_name,0,(col)),(600,300))
                              screen.blit(pygame.image.load("tick.jpg"),(600,200))
                              screen.blit(pygame.image.load("cross.jpg"),(600,400))
                              pygame.display.update()
                              time.sleep(11)
                              exit()
                       elif(flag_c==True and flag_s==False):
                              ne.send("3")
                              fsize=60
                              mf= pygame.font.SysFont("None", fsize)
                              scree.blit(backgroun, (0,0))
                              scree.blit(mf.render(pl_name,0,(col)),(20,200))
                              scree.blit(mf.render(clien,0,(col)),(20,400))
                              scree.blit(mf.render(wo,0,(col)),(200,200))
                              scree.blit(mf.render(da,0,(col)),(200,400))
                              scree.blit(mf.render("%s Wins"%clien,0,(col)),(600,300))
                              screen.blit(pygame.image.load("cross.jpg"),(600,200))
                              screen.blit(pygame.image.load("tick.jpg"),(600,400))
                              pygame.display.update()
                              time.sleep(11)
                              exit()
                       else:
                              ne.send("4")
                              fsize=60
                              mf= pygame.font.SysFont("None", fsize)
                              scree.blit(backgroun, (0,0))
                              scree.blit(mf.render(pl_name,0,(col)),(20,200))
                              scree.blit(mf.render(clien,0,(col)),(20,400))
                              scree.blit(mf.render(wo,0,(col)),(200,200))
                              scree.blit(mf.render(da,0,(col)),(200,400))
                              scree.blit(mf.render("%s "%clien,0,(col)),(600,300))
                              screen.blit(pygame.image.load("cross.jpg"),(600,200))
                              screen.blit(pygame.image.load("cross.jpg"),(600,400))
                              pygame.display.update()
                              time.sleep(11)
                              exit()



                       
       def Click():
              x,y=pygame.mouse.get_pos()
              a=[]
              global i1,v,c,screen,m1,m2,k,ulist,llist,n,vclick,k2,cclick,p2
              
              if i1<9:
                     #p2+=1
                     if (((x<335 and x>245) and (y<535 and y>445)) and p2%2==0):
                            # print "mouse on V"
                            a0=randint(0,4)
                            screen.blit(m1[a0],(137+(65*i1),388))
                            # print v[a0][0]
                            llist.append(v[a0][0])
                            ne.send(llist[i1])
                            i1+=1
                            if  (len(llist)>8):
                                   screen.blit(pygame.image.load("clock.png"),(350.25,220))
                                   screen.blit(pygame.transform.scale(pygame.image.load("reset - Copy.gif"),(144,48)),(320,550))
                                   
                                   
                           # print llist
                            vclick+=1
                            if vclick>7 :
                                i1=9
                                for i in range(9):
                                          pygame.draw.rect(screen,(255,255,255),Rect((130+(i*65),380), (45,45)))
                                llist=[]
                                for q in range(9):
                                       if(p2%2==0):
                                              p2+=1
                                              a0=randint(0,4)
                                              screen.blit(m1[a0],(137+(65*q),388))
                                              llist.append(v[a0][0])
                                              ne.send(llist[q])
                                       elif(p2%2!=0):
                                              p2+=1
                                              a0=randint(0,20)
                                              screen.blit(m2[a0],(137+(65*(q+1)),388))
                                              llist.append(c[a0][0])
                                              ne.send(llist[q])
                                              
                                       if  (len(llist)>8):
                                           screen.blit(pygame.image.load("clock.png"),(350.25,220))
                                           screen.blit(pygame.transform.scale(pygame.image.load("reset - Copy.gif"),(144,48)),(320,550))
                                          
                                   
                   

                     elif(((x<535 and x>445) and (y<535 and y>445))):
                                   #  print "mouse on C"
                                   a0=randint(0,20)
                                   screen.blit(m2[a0],(137+(65*i1),388))
                                   # print c[a0][0]
                                   llist.append(c[a0][0])
                                   ne.send(llist[i1])
                                   i1+=1
                                   print len(llist)
                                   print i1
                                   if  (len(llist)>8):
                                          screen.blit(pygame.image.load("clock.png"),(350.25,220))
                                          screen.blit(pygame.transform.scale(pygame.image.load("reset - Copy.gif"),(144,48)),(320,550))
                                        
                                   cclick+=1
                                   if cclick>7 :
                                          i1=9
                                          for i in range(9):
                                                 pygame.draw.rect(screen,(255,255,255),Rect((130+(i*65),380), (45,45)))
                                                 llist=[]
                                                 for q in range(9):
                                                     if(p2%2==0):
                                                            p2+=1
                                                            a0=randint(0,4)
                                                            screen.blit(m1[a0],(137+(65*q),388))
                                                            llist.append(v[a0][0])
                                                            ne.send(llist[q])
                                                     elif(p2%2!=0):
                                                            p2+=1
                                                            a0=randint(0,20)
                                                            screen.blit(m2[a0],(137+(65*(q+1)),388))
                                                            llist.append(c[a0][0])
                                                            ne.send(llist[q])
                                              
                                                     if  (len(llist)>8):
                                                               screen.blit(pygame.image.load("clock.png"),(350.25,220))
                                                               screen.blit(pygame.transform.scale(pygame.image.load("reset - Copy.gif"),(144,48)),(320,550))
                                                              


                            
                     
              elif (i1>=9):
                     if((x>730 and x<880) and (y<186.5 and y>148.5) and len(ulist)>2):
                            fle=open("Dict/%s/%s%s.txt"%tuple(["%d"%len(ulist),"%d"%len(ulist),ulist[0]]))
                            word_l= fle.read()
                            wo=''
                            for u in range(len(ulist)):
                                   wo+=ulist[u]
                            for u in range(len(word_l.split())):
                                   if (wo==word_l.split()[u]):
                                          print "yes"
                            da=ne.recv(2048)
                            if len(da)>len(wo):
                                   print "Client Wins"
                            elif len(da)==len(wo):
                                   print "draw"
                            else:
                                   print "Server wins"
                                          
                     else:
                            for j in n:
                                   if (((x<175+(j*65) and x>130+(j*65)) and (y<425 and y>380))):
                                          ulist.append(llist[j])
                                          #print ulist
                                          n.remove(j)
                                          pygame.draw.rect(screen,(0,0,0),Rect((133+(j*65),400),(40,0)),6)
                                          if (k<9):
                                                 screen.blit(pygame.image.load("%s.gif"%llist[j]),(132+(k*65),158))
                                                 k+=1
                                   elif(((x<464 and x>320) and (y<598 and y>550))):
                                          n=range(10)
                                          ulist=[]
                                          for k2 in range(9):
                                                 pygame.draw.rect(screen,(255,255,255),Rect((130+(k2*65),380),(45,45)))
                                                 pygame.draw.rect(screen,(255,255,255),Rect((130+(k2*65),150),(45,45)))
                                                 screen.blit(pygame.image.load("%s.gif"%llist[k2]),(137+(k2*65),388))
                                                 k=0
                                                 n=range(10)

                    
                            
