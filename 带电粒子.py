import pygame
import sys,os,time
from pygame.locals import *
import random
import math
import threading
from tkinter import *
import tkinter
import tkinter.messagebox
vect = pygame.Vector2
class MY_GUI(Tk):
    def __init__(self):
        super(MY_GUI, self).__init__()        
    #设置窗口
        self.title("控制台")           #窗口名
        self.geometry('700x300+700+20')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        #self.geometry('1068x681+10+10')
        #self["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #self.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        #标签
        self.init_data_label = Label(self, text="质量（kg）：")
        self.init_data_label.grid(row=1, column=0)
        self.result_data_label = Label(self, text="电荷量（C）：")
        self.result_data_label.grid(row=2, column=0)
        self.log_label = Label(self, text="初速度vx（m/s）：")
        self.log_label.grid(row=3, column=0)
        self.log_label = Label(self, text="初速度vy（m/s）：")
        self.log_label.grid(row=4, column=0)
        self.label1=Label(self, text="电场强度（N/C 向下为正）").grid(row=5, column=0)
        self.label2=Label(self, text="磁感应强度（T 向外为正）").grid(row=6, column=0)
        #文本框
        self.mtext = Entry(self)  #原始数据录入框
        self.mtext.grid(row = 1,column = 1, sticky = tkinter.E)
        self.qtext = Entry(self)  #处理结果展示
        self.qtext.grid(row=2,column = 1, sticky = tkinter.E)
        self.vxtext = Entry(self)  # 日志框
        self.vxtext.grid(row=3,column = 1, sticky = tkinter.E)
        self.vytext = Entry(self)
        self.vytext.grid(row=4,column = 1, sticky = tkinter.E)
        self.etext= Entry(self)
        self.etext.grid(row=5,column = 1, sticky = tkinter.E)
        self.btext= Entry(self)
        self.btext.grid(row=6,column = 1, sticky = tkinter.E)
        #按钮
        self.buttonm = Button(self, text="质量重置", bg="lightblue", width=10,command=self.updatem)  # 调用内部方法  加()为直接调用
        self.buttonm.grid(row=1, column=10)
        self.buttonq = Button(self, text="电荷量重置", bg="lightblue", width=10,command=self.updateq)  # 调用内部方法  加()为直接调用
        self.buttonq.grid(row=2, column=10)
        self.buttonv = Button(self, text="初速度重置", bg="lightblue", width=10,command=self.updatev)  # 调用内部方法  加()为直接调用
        self.buttonv.grid(row=3, column=10)
        self.buttonE = Button(self, text="设置电场", bg="lightblue", width=10,command=self.initE)  # 调用内部方法  加()为直接调用
        self.buttonE.grid(row=5, column=10)
        self.buttonB = Button(self, text="设置磁场", bg="lightblue", width=10,command=self.initB)  # 调用内部方法  加()为直接调用
        self.buttonB.grid(row=6, column=10)
        self.buttonoffE = Button(self, text="清除电场", bg="red", width=10,command=game.clearE)  # 调用内部方法  加()为直接调用
        self.buttonoffE.grid(row=7, column=0)
        self.buttonoffB = Button(self, text="清除磁场", bg="red", width=10,command=game.clearB)  # 调用内部方法  加()为直接调用
        self.buttonoffB.grid(row=7, column=1)
        self.buttonabout = Button(self, text="关于", width=10,command=self.about).grid(row=7, column=2)  # 调用内部方法  加()为直接调用
        self.button1 = Button(self, text="模型一", width=10,command=self.init1).grid(row=8, column=0)
        self.button2 = Button(self, text="模型二", width=10,command=self.init2).grid(row=8, column=1)
        self.button3 = Button(self, text="模型三", width=10,command=self.init3).grid(row=8, column=2)
        self.button4 = Button(self, text="模型四", width=10,command=self.init4).grid(row=9, column=0)
    #功能函数
    def about(self):
        tkinter.messagebox.showinfo("关于本软件",'开发者：曦微(QQ2273805191)'+
                                    '\n为方便高中学子攻克物理难题，'+
                                    '\n开发者不辞辛苦，不舍昼夜，'+
                                    '\n牺牲宝贵的学习时间完成此项目，'+
                                    '\n请尊重开发者的劳动成果，侵权必究！！'+
                                    '\n偶尔存在误差请谅解')
    def init1(self):
        game.running=False
        B((572.0,532.0),(1120, 328) ,50.0)
        E((596.5, 284.0) ,(1187, 156) ,300.0)
        game.v0=(0,0)
        game.running=True
    def init2(self):
        game.running=False
        B((799.0, 283.0) ,(720, 552) ,50.0)
        E((1041.5, 301.5) ,(59, 25) ,300.0)
        game.running=True
    def init3(self):
        game.running=False
        B((603.0, 322.5) ,(940, 469) ,-20.0)
        E((591.5, 323.0) ,(891, 466) ,400.0)        
        game.v0=(20,0)
        game.running=True
    def init4(self):
        game.running=False
        B((600.0, 261.0) ,(1190, 124) ,-20.0)
        B((599.5, 417.5) ,(1195, 181), -40.0)
        Ball((1000,327),(0,5),game.ballq,game.ballm)
        game.running=True
    def initE(self):
        try:
            game.initE(float(self.etext.get()))
            
        except:
            tkinter.messagebox.showinfo("错误提示",'请正确输入电场强度后重试！！')
    def initB(self):
        try:
            game.initB(float(self.btext.get()))
            
        except:
            tkinter.messagebox.showinfo("错误提示",'请正确输入磁感应强度后重试！！')    
    def updatem(self):
        src = self.mtext.get()
        try:
            game.ballm=float(src)
        except:
            tkinter.messagebox.showinfo("错误提示",'输入格式有误！！')
    def updateq(self):
        src = self.qtext.get()
        try:
            game.ballq=float(src)
        except:
            tkinter.messagebox.showinfo("错误提示",'输入格式有误！！')
    def updatev(self):
        src1 = self.vxtext.get()
        src2 = self.vytext.get()
        try:
            game.v0=(float(src1),float(src2))
        except:
            tkinter.messagebox.showinfo("错误提示",'输入格式有误！！')
class B(pygame.sprite.Sprite):
    def __init__(self,pos,size,energy):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.pos=pos
        self.size=size
        self.energy=energy
        if self.energy>=0:
            self.oldimage=self.images[0]
        else:
            self.oldimage=self.images[1]
        self.image=pygame.transform.smoothscale(self.oldimage,size)
        self.rect=self.image.get_rect()
        self.rect.centerx=pos[0]
        self.rect.centery=pos[1]
        print('OK')
    def update(self):
        game.screen.blit(self.image,self.rect)
        textfont=pygame.font.SysFont('arial',30)
        self.text=textfont.render('B='+str(int(self.energy))+'T',True,(255,0,0))
        self.textrect=self.text.get_rect(center=self.rect.center)
        game.screen.blit(self.text,self.textrect)
class E(pygame.sprite.Sprite):
    def __init__(self,pos,size,energy):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.pos=pos
        self.size=size
        self.energy=energy
        if self.energy>=0:
            self.oldimage=self.images[0]
        else:
            self.oldimage=self.images[1]
        self.image=pygame.transform.smoothscale(self.oldimage,size)
        self.rect=self.image.get_rect()
        self.rect.centerx=pos[0]
        self.rect.centery=pos[1]
        print('OK')
    def update(self):
        game.screen.blit(self.image,self.rect)
        textfont=pygame.font.SysFont('arial',32)
        self.text=textfont.render('E='+str(int(self.energy))+'N/C',True,(255,0,0))
        self.textrect=self.text.get_rect(center=self.rect.center)
        game.screen.blit(self.text,self.textrect)
class Dirt(pygame.sprite.Sprite):
    def __init__(self, actor):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.actor=actor
        self.rect = self.image.get_rect(center=self.actor.rect.center)
        self.life =2000
    def update(self):
        
        self.life = self.life - 1
        game.screen.blit(self.image,self.rect)
        if self.life <=0:
            self.kill()
class smallDirt(Dirt):
    def __init__(self,owner):
        super(smallDirt,self).__init__(owner)
        self.owner=owner
        self.life =1000  
        self.rect=self.image.get_rect(center=self.owner.rect.center)
class Ball(pygame.sprite.Sprite):
    def __init__(self,pos,v0,q,m):
        pygame.sprite.Sprite.__init__(self, self.containers)
        
        self.rect=self.image.get_rect(center=(pos[0],pos[1]))
        self.q=q
        self.m=m
        self.v=vect(*v0)
        self.x=self.rect.centerx
        self.y=self.rect.centery
    def getforce(self,F):
        self.a=F*(1/self.m)*(1/60)
        self.v=self.v+self.a
    def cheek1(self):
        #elist=pygame.sprite.spritecollide(self,game.Egroup,False)
        elist=[i for i in game.Egroup if i.rect.collidepoint(self.x,self.y)]
        if elist != []:
            for e in elist:
                self.getforce(vect(0,self.q*e.energy))
        blist=[i for i in game.Bgroup if i.rect.collidepoint(self.x,self.y)]
        if blist != []:
            self.vlen=self.v.length()
            if self.vlen!=0:
                for b in blist:
                                        
                    bforce=vect(-self.v[1],self.v[0])*(b.energy*self.q)#F=qvb
                    self.getforce(bforce)
                self.v.scale_to_length(self.vlen)
    def move(self):
        self.x+=self.v[0]
        self.y+=self.v[1]
        self.rect.centerx+=self.v[0]
        self.rect.centery+=self.v[1]
        #print(self.v.length())
        if abs(self.x-self.rect.centerx)>1:
            #print(abs(self.x-self.rect.x))
            self.rect.centerx=self.x           
        if abs(self.y-self.rect.centery)>1:
            #print(abs(self.y-self.rect.y))
            self.rect.centery=self.y
        #self.rect.move_ip(*self.v)
        if self.rect.left <0 or self.rect.right > 1200 or self.rect.top < 0 or self.rect.bottom > 700:
            game.setballing=True
            self.kill()
        smallDirt(self)
    def update(self):
        #self.getforce((0,200))
        self.cheek1()
        self.move()
        game.screen.blit(self.image,self.rect)
main_dir = os.path.split(os.path.abspath(__file__))[0]        
def load_image(file):
    "loads an image, prepares it for play"
    file = os.path.join(main_dir, 'res', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface
class Game(threading.Thread):
    FPS=60
    allsp = pygame.sprite.RenderUpdates()
    setballing=True
    initeing=False
    initbing=False
    initenum=1
    initbnum=1
    Bgroup=pygame.sprite.Group()
    Egroup=pygame.sprite.Group()
    dirtgroup=pygame.sprite.Group()
    Ball.containers = allsp
    Dirt.containers = allsp,dirtgroup
    B.containers = allsp,Bgroup
    E.containers = allsp,Egroup
    ballm=0.5
    ballq=0.1
    v0=(20,0)
    def __init__(self):
        super(Game, self).__init__()
    def initE(self,e):
        self.setballing=False
        self.initbing=False
        self.initeing=True
        self.E0=e
    def initB(self,b):
        self.setballing=False
        self.initeing=False
        self.initbing=True
        self.B0=b
    def clearE(self):
        for i in self.Egroup:
            i.kill()
    def clearB(self):
        for i in self.Bgroup:
            i.kill()      
    def update(self):
        self.allsp.update()
        if self.initbing:
            if self.pressed_mouse[0]==1:
                if self.initbnum==1:
                    self.initbnum-=1
                    self.epos=pygame.mouse.get_pos()                 
            elif self.initbnum==0:
                self.initbing=False
                self.initbnum=1
                self.epos2=pygame.mouse.get_pos()
                sizex=abs(self.epos[0]-self.epos2[0])
                sizey=abs(self.epos[1]-self.epos2[1])
                B(((self.epos[0]+self.epos2[0])/2,(self.epos[1]+self.epos2[1])/2),(sizex,sizey),self.B0)
                self.setballing=True
        if self.initeing:
            if self.pressed_mouse[0]==1:
                if self.initenum==1:
                    self.initenum-=1
                    self.epos=pygame.mouse.get_pos()                 
            elif self.initenum==0:
                self.initeing=False
                self.initenum=1
                self.epos2=pygame.mouse.get_pos()
                sizex=abs(self.epos[0]-self.epos2[0])
                sizey=abs(self.epos[1]-self.epos2[1])
                E(((self.epos[0]+self.epos2[0])/2,(self.epos[1]+self.epos2[1])/2),(sizex,sizey),self.E0)
                self.setballing=True
        if self.setballing:
            ballpos=(pygame.mouse.get_pos()[0]-5,pygame.mouse.get_pos()[1]-5)
            self.screen.blit(Ball.image,ballpos)
            if self.pressed_mouse[0]==1:
                for i in self.dirtgroup:
                    i.kill()
                self.ball=Ball(pygame.mouse.get_pos(),self.v0,self.ballq,self.ballm)
                self.setballing=False

  
    def run(self):
        FPSClock=pygame.time.Clock()    
        self.screen = pygame.display.set_mode((1200, 700))
        pygame.display.set_caption('SMALL BALL')
        self.running=True
        Run=True
        E.images=[load_image('e+.png'),load_image('e_.png')]
        B.images=[load_image('B_outside.png'),load_image('B_inside.png')]
        Ball.image=pygame.transform.smoothscale(load_image('gunstar1.png'),(10,10))
        smallDirt.image=pygame.transform.smoothscale(load_image('ball0.png'),(10,10))
        while Run:
            while self.running:
                self.screen.fill((135,206,250))
                self.pressed_mouse = pygame.mouse.get_pressed()
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:                    
                            Run=False
                        if event.key == K_SPACE:                    
                            for i in self.Bgroup:
                                print('B',i.pos,i.size,i.energy)
                            for i in self.Egroup:
                                print('E',i.pos,i.size,i.energy)
                    if event.type == QUIT:
                        Run=False
                self.update()
                pygame.display.update()
                FPSClock.tick(self.FPS)
    
pygame.init()
game=Game()
game.start()
mywindow = MY_GUI()
# 设置根窗口默认属性
time.sleep(1)
#mywindow.about()
mywindow.mainloop()

