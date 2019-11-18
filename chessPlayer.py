import random




def inv(position):#old code, convert row store to store
    r=position[0]
    c=position[1]
    rt=8*r+c
    return rt            

def swapp(a,b):
    temp=[]
    for i in a:
        temp=temp+[i]
    print(temp)
    a=[]
    for i in b:
        a=a+[i]
    print(a)
    b=[]
    for i in temp:
        b=b+[i]
    print(b)
    return b
    

def getpos(pos):#old code, convert store pos to coordinate
    if(( pos<0)or(pos>63)):
        return False
    rt=[]
    a=0
    while((a+1)*8<pos):
        a=a+1
    r=a
    c=pos%8
    rt=[7-r,7-c]
    return rt

class chess:
    def __init__(self):
        self.store=[23,21,22,24,25,22,21,23,20,20,20,20,20,20,20,20,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,10,10,10,10,10,10,10,13,11,12,14,15,12,11,13]

def genboard():
    store=[23,21,22,24,25,22,21,23,20,20,20,20,20,20,20,20,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,10,10,10,10,10,10,10,13,11,12,14,15,12,11,13]
    return store
        
def printboard(board):  
    pt=["#    ","_    ","#    ","_    ","#    ","_    ","#    ","_    ", "_    ","#    ","_    ","#    ","_    ","#    ","_    ","#    ","#    ","_    ","#    ","_    ","#    ","_    ","#    ","_    ","_    ","#    ","_    ","#    ","_    ","#    ","_    ","#    ","#    ","_    ","#    ","_    ","#    ","_    ","#    ","_    ","_    ","#    ","_    ","#    ","_    ","#    ","_    ","#    ","#    ","_    ","#    ","_    ","#    ","_    ","#    ","_    ","_    ","#    ","_    ","#    ","_    ","#    ","_    ","#    "]
    for a in range(0,8):
        for b in range(0,8):
            l=8*a+b
            if board[l]!=0:
                k=""
                if board[l]==23:
                    k="bROOK"
                elif board[l]==21:
                    k="bKnht"
                elif board[l]==22:
                    k="bBish"
                elif board[l]==25:
                    k="bKing"
                elif board[l]==24:
                    k="bQunn"
                elif board[l]==20:
                    k="bPawn"
                elif board[l]==13:
                    k="wRook"
                elif board[l]==11:
                    k="wKnht"
                elif board[l]==12:
                    k="wBish"
                elif board[l]==15:
                    k="wKing"
                elif board[l]==14:
                    k="wQunn"
                elif board[l]==10:
                    k="wPawn"                
                pt[l]=k
            m=63-(8*a+b)
            if m<10:    
                pt[l]=pt[l]+"0"+str(m) 
            else:   
                pt[l]=pt[l]+str(m)   
    op=""
    cnt=0
    while cnt<64:
        op=op+"\t"+pt[cnt]
        if cnt%8==7:
            op=op+"\n"
        cnt=cnt+1
    print (op)   
    return True


def GetPlayerPositions(board,player):
        if ((player!=10)and(player!=20)):
            return False
        pos=[]
        for a in range (0,8):
            for b in range (0,8):
                l=8*a+b
                if player==20:
                    if board[l]>=20:
                        pos=pos+[l]
                else:
                    if ((board[l]>0)and(board[l]<20)):
                        pos=pos+[l] 

        return pos
def qwe(pos):#enemy or player
    if pos==0:
        return 0
    elif pos>=20:
        return -1 #b
    else:
        return 1 #w





def GetPieceLegalMoves(board,position):
    pos=position
    if ((pos<0)or(pos>63)):
        return False
    r=int(pos/8)
    c=pos%8
    store=[[],[],[],[],[],[],[],[]]
    cnt=0
    while cnt<8:
        for i in range(cnt*8+0,cnt*8+8,1):
            store[cnt]=store[cnt]+[board[i]]
        cnt=cnt+1
    k=store[r][c]
    lp=[]
    if k!=0:
        if k==10:
            if qwe(store[r-1][c])==0:
                lp=lp+[inv([r-1,c])]
            if ((r+1<8)and(c+1<8)):
                if qwe(store[r-1][c+1])==-1:#w
                    lp=lp+[inv([r-1,c+1])]
            if ((r-1>=0)and(c-1>=0)):
                if qwe(store[r-1][c-1])==-1:
                    lp=lp+[inv([r-1,c-1])]
                
        if k==20:
            
            if qwe(store[r+1][c])==0:
                lp=lp+[inv([r+1,c])]
            if ((r+1<8)and(c+1<8)):
                if qwe(store[r+1][c+1])==1:
                    lp=lp+[inv([r+1,c+1])]
            if ((c-1>=0)and(r+1<8)):
                if qwe(store[r+1][c-1])==1:
                    lp=lp+[inv([r+1,c-1])]  
        if k==23:
            
            i=r
            if i-1>=0:
                i=i-1
                while(qwe(store[i][c])!=-1): 
                    if qwe(store[i][c])==1:
                        lp=lp+[inv([i,c])]
                        break 
                    lp=lp+[inv([i,c])]
                    i=i-1
                 
                    if i<0:
                        break
                          
            i=r
            if i+1<8:
                i=i+1
                while(qwe(store[i][c])!=-1): 
                    if qwe(store[i][c])==1:
                        lp=lp+[inv([i,c])]
                        break  
                    lp=lp+[inv([i,c])]
                    i=i+1
               
                    if i>=8:
                        break 
                           
            
            j=c
            if j+1<8:
                j=j+1
                while(qwe(store[r][j])!=-1): 
                    if qwe(store[r][j])==1:
                        lp=lp+[inv([r,j])]
                        break 
                    lp=lp+[inv([r,j])]
                    j=j+1
                   
                    if j>=8:
                        break
                        
            j=c
            if j-1>=0:
                j=j-1
                while(qwe(store[r][j])!=-1):
                    if qwe(store[r][j])==1:
                        lp=lp+[inv([r,j])]
                        break 
                    lp=lp+[inv([r,j])]
                    j=j-1
                
                    if j<0:
                        break                
                           
        if k==13:
            
            i=r
            if i-1>=0:
                i=i-1
                while(qwe(store[i][c])!=1):
                    if qwe(store[i][c])==-1:
                        lp=lp+[inv([i,c])]
                        break 
                    lp=lp+[inv([i,c])]
                    i=i-1

                    if i<0:
                        breakgenmove


                    
            i=r
            if i+1<8:
                i=i+1
                while(qwe(store[i][c])!=1):
                    if qwe(store[i][c])==-1:
                        lp=lp+[inv([i,c])]
                        break          
                    lp=lp+[inv([i,c])]
                    i=i+1
                  
                    if i>=8:
                        break 
                                    
            
            j=c
            if j+1<8:
                j=j+1
                while(qwe(store[r][j])!=1):
                    if qwe(store[r][j])==-1:
                        lp=lp+[inv([r,j])]
                        break        
                    lp=lp+[inv([r,j])]
                    j=j+1
            
                    if j>=8:
                        break
                    
                                        
            j=c
            if j-1>=0:
                j=j-1
                while(qwe(store[r][j])!=1):
                    if qwe(store[r][j])==-1:
                        lp=lp+[inv([r,j])]
                        break                     
                    lp=lp+[inv([r,j])]
                    j=j-1
                   
                    if j<0:
                        break  
                        
        
        if k==21:
            if ((r-2>=0)and(c+1<8)):
                if qwe(store[r-2][c+1])!=-1:
                    lp=lp+[inv([r-2,c+1])]
            if ((r-2>=0)and(c-1>=0)):
                if qwe(store[r-2][c-1])!=-1:#2                    
                    lp=lp+[inv([r-2,c-1])] 
            if ((r+2<8)and(c+1<8)):                        
                if qwe(store[r+2][c+1])!=-1:#3
                    lp=lp+[inv([r+2,c+1])]  
            if ((r+2<8)and(c-1>=0)):       
                if qwe(store[r+2][c-1])!=-1:#4
                    lp=lp+[inv([r+2,c-1])]   
            if ((r-1>=0)and(c+2<8)):        
                if qwe(store[r-1][c+2])!=-1:#5
                    lp=lp+[inv([r-1,c+2])]  
            if ((r-1>=0)and(c-2>=0)):        
                if qwe(store[r-1][c-2])!=-1:#6
                
                    lp=lp+[inv([r-1,c-2])]  
            if ((r+1<8)and(c+2<8)):        
                if qwe(store[r+1][c+2])!=-1:#7
                
                    lp=lp+[inv([r+1,c+2])]  
            if ((r+1<8)and(c-2>=0)):        
                if qwe(store[r+1][c-2])!=-1:#8
                
                    lp=lp+[inv([r+1,c-2])]                        
        if k==11:
            if ((r-2>=0)and(c+1<8)):
                if qwe(store[r-2][c+1])!=1:
                    lp=lp+[inv([r-2,c+1])]
            if ((r-2>=0)and(c-1>=0)):
                if qwe(store[r-2][c-1])!=1:#2                    
                    lp=lp+[inv([r-2,c-1])] 
            if ((r+2<8)and(c+1<8)):                        
                if qwe(store[r+2][c+1])!=1:#3
                    lp=lp+[inv([r+2,c+1])]  
            if ((r+2<8)and(c-1>=0)):       
                if qwe(store[r+2][c-1])!=1:#4
                    lp=lp+[inv([r+2,c-1])]   
            if ((r-1>=0)and(c+2<8)):        
                if qwe(store[r-1][c+2])!=1:#5
                    lp=lp+[inv([r-1,c+2])]  
            if ((r-1>=0)and(c-2>=0)):        
                if qwe(store[r-1][c-2])!=1:#6
                
                    lp=lp+[inv([r-1,c-2])]  
            if ((r+1<8)and(c+2<8)):        
                if qwe(store[r+1][c+2])!=1:#7
                
                    lp=lp+[inv([r+1,c+2])]  
            if ((r+1<8)and(c-2>=0)):        
                if qwe(store[r+1][c-2])!=1:#8
                
                    lp=lp+[inv([r+1,c-2])]  
                    
        if k==22:
            i=r
            j=c
            if ((i-1>=0)and(j-1>=0)):
                i=i-1
                j=c-1
                while(qwe(store[i][j])!=-1):
                    if qwe(store[i][j])==1:
                        lp=lp+[inv([i,j])]
                        break   
                    lp=lp+[inv([i,j])]
                    i=i-1
                    j=j-1

                    if ((i<0)or(j<0)):
                        break
                     
            i=r
            j=c
            if ((i+1<8)and(j-1>=0)):
                i=i+1
                j=j-1
                while(qwe(store[i][j])!=-1):
                    if qwe(store[i][j])==1:
                        lp=lp+[inv([i,j])]
                        break     
                    lp=lp+[inv([i,j])]
                    i=i+1
                    j=j-1
               
                    if ((i>=8)or(j<0)):
                        break 
                    
            i=r
            j=c
            if ((j+1<8)and(i-1>=0)):
                i=i-1
                j=j+1
                while(qwe(store[i][j])!=-1): 
                    if qwe(store[i][j])==1:
                        lp=lp+[inv([i,j])]
                        break
                    lp=lp+[inv([i,j])]
                    j=j+1
                    i=i-1
                
                    if ((j>=8)or(i<0)):
                        break
                            
            j=c
            i=r
            if ((j+1<8)and(i+1<8)):
                j=j+1
                i=i+1
                while(qwe(store[i][j])!=-1):
                    if qwe(store[i][j])==1:
                        lp=lp+[inv([i,j])]
                        break 
                    lp=lp+[inv([i,j])]
                    j=j+1
                    i=i+1
                    
                    if((i>=8)or(j>=8)):
                        break 
                       
                    
        if k==12:
            i=r
            j=c
            if ((i-1>=0)and(j-1>=0)):
                i=i-1
                j=c-1
                while(qwe(store[i][j])!=1):
                    if qwe(store[i][j])==-1:
                        lp=lp+[inv([i,j])]
                        break  
                    lp=lp+[inv([i,j])]
                    i=i-1
                    j=j-1

                    if ((i<0)or(j<0)):
                        break
                      
            i=r
            j=c
            if ((i+1<8)and(j-1>=0)):
                i=i+1
                j=j-1
                while(qwe(store[i][j])!=1):
                    if qwe(store[i][j])==-1:
                        lp=lp+[inv([i,j])]
                        break 
                    lp=lp+[inv([i,j])]
                    i=i+1
                    j=j-1
              
                    if ((i>=8)or(j<0)):
                        break 
                         
            i=r
            j=c
            if ((j+1<8)and(i-1>=0)):
                i=i-1
                j=j+1
                while(qwe(store[i][j])!=1):
                    if qwe(store[i][j])==-1:
                        lp=lp+[inv([i,j])]
                        break  
                    lp=lp+[inv([i,j])]
                    j=j+1
                    i=i-1
                   
                    if ((j>=8)or(i<0)):
                        break
                       
            j=c
            i=r
            if ((j+1<8)and(i+1<8)):
                j=j+1
                i=i+1
                while(qwe(store[i][j])!=1):
                    if qwe(store[i][j])==-1:
                        lp=lp+[inv([i,j])]
                        break   
                    lp=lp+[inv([i,j])]
                    j=j+1
                    i=i+1
                   
                    if((i>=8)or(j>=8)):
                        break 
                      

        if k==24:
            i=r
            j=c
            if ((i-1>=0)and(j-1>=0)):
                i=i-1
                j=c-1
                while(qwe(store[i][j])!=-1):
                    if qwe(store[i][j])==1:
                        lp=lp+[inv([i,j])]
                        break 
                    lp=lp+[inv([i,j])]
                    i=i-1
                    j=j-1

                    if ((i<0)or(j<0)):
                        break
                       
            i=r
            j=c
            if ((i+1<8)and(j-1>=0)):
                i=i+1
                j=j-1
                while(qwe(store[i][j])!=-1):
                    if qwe(store[i][j])==1:
                        lp=lp+[inv([i,j])]
                        break
                    lp=lp+[inv([i,j])]
                    i=i+1
                    j=j-1
     
                    if ((i>=8)or(j<0)):
                        break 
                                   
            i=r
            j=c
            if ((j+1<8)and(i-1>=0)):
                i=i-1
                j=j+1
                while(qwe(store[i][j])!=-1):
                    if qwe(store[i][j])==1:
                        lp=lp+[inv([i,j])]
                        break     
                    lp=lp+[inv([i,j])]
                    j=j+1
                    i=i-1
                   
                    if ((j>=8)or(i<0)):
                        break
                    
            j=c
            i=r
            if ((j+1<8)and(i+1<8)):
                j=j+1
                i=i+1
                while(qwe(store[i][j])!=-1):
                    if qwe(store[i][j])==1:
                        lp=lp+[inv([i,j])]
                        break
                    lp=lp+[inv([i,j])]
                    j=j+1
                    i=i+1
                   
                    if((i>=8)or(j>=8)):
                        break          
                         
            i=r
            if i-1>=0:
                i=i-1
                while(qwe(store[i][c])!=-1): 
                    if qwe(store[i][c])==1:
                        lp=lp+[inv([i,c])]
                        break 
                    lp=lp+[inv([i,c])]
                    i=i-1
                   
                    if i<0:
                        break
                        
            i=r
            if i+1<8:
                i=i+1
                while(qwe(store[i][c])!=-1):
                    if qwe(store[i][c])==1:
                        lp=lp+[inv([i,c])]
                        break  
                    lp=lp+[inv([i,c])]
                    i=i+1
                
                    if i>=8:
                        break 
                          
            j=c
            if j+1<8:
                j=j+1
                while(qwe(store[r][j])!=-1):
                    if qwe(store[r][j])==1:
                        lp=lp+[inv([r,j])]
                        break 
                    lp=lp+[inv([r,j])]
                    j=j+1
                  
                    if j>=8:
                        break
                         
            j=c
            if j-1>=0:
                j=j-1
                while(qwe(store[r][j])!=-1): 
                    if qwe(store[r][j])==1:
                        lp=lp+[inv([r,j])]
                        break  
                    lp=lp+[inv([r,j])]
                    j=j-1
                    
                    if j<0:
                        break      
                    
                      
                    
                    
        if k==14:
            i=r
            j=c
            if ((i-1>=0)and(j-1>=0)):
                i=i-1
                j=c-1
                while(qwe(store[i][j])!=1): 
                    if qwe(store[i][j])==-1:
                        lp=lp+[inv([i,j])]
                        break   
                    lp=lp+[inv([i,j])]
                    i=i-1
                    j=j-1

                    if ((i<0)or(j<0)):
                        break
                     
            i=r
            j=c
            if ((i+1<8)and(j-1>=0)):
                i=i+1
                j=j-1
                while(qwe(store[i][j])!=1): 
                    if qwe(store[i][j])==-1:
                        lp=lp+[inv([i,j])]
                        break  
                    lp=lp+[inv([i,j])]
                    i=i+1
                    j=j-1

                    if ((i>=8)or(j<0)):
                        break 
                                          
            i=r
            j=c
            if ((j+1<8)and(i-1>=0)):
                i=i-1
                j=j+1
                while(qwe(store[i][j])!=1): 
                    if qwe(store[i][j])==-1:
                        lp=lp+[inv([i,j])]
                        break  
                    lp=lp+[inv([i,j])]
                    j=j+1
                    i=i-1
            
                    if ((j>=8)or(i<0)):
                        break
                              
            j=c
            i=r
            if ((j+1<8)and(i+1<8)):
                j=j+1
                i=i+1
                while(qwe(store[i][j])!=1):
                    if qwe(store[i][j])==-1:
                        lp=lp+[inv([i,j])]
                        break   
                    lp=lp+[inv([i,j])]
                    j=j+1
                    i=i+1
                    
                    if((i>=8)or(j>=8)):
                        break          
                     
            i=r
            if i-1>=0:
                i=i-1
                while(qwe(store[i][c])!=1):
                    if qwe(store[i][c])==-1:
                        lp=lp+[inv([i,c])]
                        break  
                    lp=lp+[inv([i,c])]
                    i=i-1
        
                    if i<0:
                        break
          
            i=r
            if i+1<8:
                i=i+1
                while(qwe(store[i][c])!=1):
                    if qwe(store[i][c])==-1:
                        lp=lp+[inv([i,c])]
                        break 
                    lp=lp+[inv([i,c])]
                    i=i+1
                 
                    if i>=8:
                        break 
                          
            
            j=c
            if j+1<8:
                j=j+1
                while(qwe(store[r][j])!=1): 
                    if qwe(store[r][j])==-1:
                        lp=lp+[inv([r,j])]
                        break 
                    lp=lp+[inv([r,j])]
                    j=j+1
               
                    if j>=8:
                        break
                            
            j=c
            if j-1>=0:
                j=j-1
                while(qwe(store[r][j])!=1):
                    if qwe(store[r][j])==-1:
                        lp=lp+[inv([r,j])]
                        break   
                    lp=lp+[inv([r,j])]
                    j=j-1
                   
                    if j<0:
                        break   
                      
        if k==25:
            if r-1>=0:
                if qwe(store[r-1][c])!=-1:
                    lp=lp+[inv([r-1,c])]
            if r+1<8:     
                if qwe(store[r+1][c])!=-1:
                        lp=lp+[inv([r+1,c])]
            if c+1<8:
                if qwe(store[r][c+1])!=-1:
                        lp=lp+[inv([r,c+1])]
            if c-1>=0:
                if qwe(store[r][c-1])!=-1:
                        lp=lp+[inv([r,c-1])]                
            if ((r-1>=0)and(c+1<8)):
                if qwe(store[r-1][c+1])!=-1:
                    lp=lp+[inv([r-1,c+1])]
            if ((c-1>=0)and(r-1>=0)):
                if qwe(store[r-1][c-1])!=-1:
                    lp=lp+[inv([r-1,c-1])]   
            if ((r+1<8)and(c+1<8)):
                if qwe(store[r+1][c+1])!=-1:
                    lp=lp+[inv([r+1,c+1])]
            if ((c-1>=0)and(r+1<8)):
                if qwe(store[r+1][c-1])!=-1:
                    lp=lp+[inv([r+1,c-1])]   
            
        if k==15:
            if r-1>=0:
                if qwe(store[r-1][c])!=1:
                    lp=lp+[inv([r-1,c])]
            if r+1<8:     
                if qwe(store[r+1][c])!=1:
                        lp=lp+[inv([r+1,c])]
            if c+1<8:
                if qwe(store[r][c+1])!=1:
                        lp=lp+[inv([r,c+1])]
            if c-1>=0:
                if qwe(store[r][c-1])!=1:
                        lp=lp+[inv([r,c-1])]                
            if ((r-1>=0)and(c+1<8)):
                if qwe(store[r-1][c+1])!=1:
                    lp=lp+[inv([r-1,c+1])]
            if ((c-1>=0)and(r-1>=0)):
                if qwe(store[r-1][c-1])!=1:
                    lp=lp+[inv([r-1,c-1])]   
            if ((r+1<8)and(c+1<8)):
                if qwe(store[r+1][c+1])!=1:
                    lp=lp+[inv([r+1,c+1])]
            if ((c-1>=0)and(r+1<8)):
                if qwe(store[r+1][c-1])!=1:
                    lp=lp+[inv([r+1,c-1])]        
    
    return lp


def IsPositionUnderThreat(board,position,player):
    danger=False
    opmove=[]
    me=10
    op=20
    if player==20:
        me=20
        op=10
    checklist=GetPlayerPositions(board,op)
    for i in checklist:
        opmove=opmove+GetPieceLegalMoves(board,i)
    for j in opmove:
        if j==position:
            return True
    return False

def getmove(player):#game iput
    if ((player!=20)and(player!=10)):
        return False
    if player==10:
        ip_1=63-input("player white which gogo?")
        ip_2=63-input("player white where gogo?")
        move=[ip_1,ip_2]
    if player==20:
        ip_1=63-input("player black which gogo?")
        ip_2=63-input("player black where gogo?")
        move=[ip_1,ip_2] 
    return move


def win(board):#victory detect
    b=0
    w=0
    for i in board:
        if i==15:
            b=1
        if i==25:
            w=1
    if b==0:
        return 1
    elif w==0:
        return -1
    else:
        return 0

def accepto():# game 
    x=genboard()
    printboard(x)
    winner=0
    gameover=False
    while gameover==False:


        check_w=0
        while check_w==0:
            wmove=getmove(10)
            check_1=GetPlayerPositions(x,10)
            a=0
            for j in check_1:
                if j==wmove[0]:
                    a=1
            if a==0:
                print("yo your chess is not even there!")
                
            check_2=GetPieceLegalMoves(x,wmove[0])
            b=0
            if a==1:
                for j in check_2:
                    if j==wmove[1]:
                        b=1            
                if b==0:
                    print("yo watch out you can not go there!")
            if((a==1)and(b==1)):
                check_w==1
                break
        temp=x[wmove[0]]
        x[wmove[0]]=0
        x[wmove[1]]=temp
        if win(x)==1:
            winner=1
            gameover==True
            break
        printboard(x)
    

        check_b=0
        while check_b==0:
            bmove=getmove(20)
            check_1=GetPlayerPositions(x,20)
            a=0
            for j in check_1:
                if j==bmove[0]:
                    a=1
            if a==0:
                print("yo your chess is not even there!")
            check_2=GetPieceLegalMoves(x,bmove[0])
            b=0
            if a==1:
                for j in check_2:
                    if j==bmove[1]:
                        b=1
                if b==0:
                    print("yo watch out you can not go there!")
            if((a==1)and(b==1)):
                check_b==1
                break
        temp=x[bmove[0]]
        x[bmove[0]]=0
        x[bmove[1]]=temp
        if win(x)==-1:
            winner=-1
            gameover==True
            break        
        printboard(x)
    return True        
def gogo(x,move):#move chess
    temp=x[move[0]]
    x[move[0]]=0
    x[move[1]]=temp   
    return True
        
def value(board,pos):#assign value
    k=board[pos]
    if k==0:
        return 0
    if k%10==0:
        return 5
    if k%10==1:
        return 15
    if k%10==2:
        return 20
    if k%10==3:
        return 20
    if k%10==4:
        return 50
    if k%10==5:
        return 1000
def genmove(board,player):#get all available moves
    sim=genboard()
    sim=[]
    for i in board:
        sim=sim+[i]
    sim_2=genboard()
    sim_2=[]
    for i in board:
        sim_2=sim_2+[i]
    op=0
    if player==10:
        op=-1
        op_c=20
    else:
        op=1
        op_c=10
    checklist_me=GetPlayerPositions(sim_2,player)
    checklist_op=GetPlayerPositions(sim_2,op_c)
    move_me1=[]
    cand_me1=[]
    
    gain=0
    cnt=0
    for i in checklist_me:
        move_me1=move_me1+[[i,GetPieceLegalMoves(board,i),sim[i]]]
    for i in move_me1:
        for j in i[1]:
            sim_2=[]
            for p in board:
                sim_2=sim_2+[p]
                
            if qwe(board[j])==op:
                cand_me1=cand_me1+[[[i[0],j],5*value(x,j)]]
            else:
                cand_me1=cand_me1+[[[i[0],j],0]]

#threat bonus
            for k in checklist_op:
                if IsPositionUnderThreat(sim_2,k,op_c)==True:
                    cand_me1[cnt][1]=cand_me1[cnt][1]-0.5*value(sim_2,k) 
            gogo(sim_2,[i[0],j])
            simnext=GetPlayerPositions(sim_2,player)
            #print (simnext)
            #printboard(sim_2)
            for k in checklist_op:
                if IsPositionUnderThreat(sim_2,k,op_c)==True:
                    cand_me1[cnt][1]=cand_me1[cnt][1]+0.5*value(sim_2,k)                                       
            for h in simnext:
                if IsPositionUnderThreat(sim_2,h,player)==True:
                    cand_me1[cnt][1]=cand_me1[cnt][1]-5*value(sim_2,h)                    

            cnt=cnt+1
    random.shuffle(cand_me1)        
    swap=1
   # print(cand_me1)
    while swap==1:
        swap=0
        for i in range(0,len(cand_me1)-1,1):
            if cand_me1[i][1]<cand_me1[i+1][1]:
                #print(cand_me1)
                #swapp(cand_me1[i],cand_me1[i+1])
                
                temp=[]
                for g in cand_me1[i]:
                    temp=temp+[g]
                    #print("this is temp")
                    #print(temp)
                cand_me1[i]=[]
                for g in cand_me1[i+1]:
                    cand_me1[i]=cand_me1[i]+[g]
                #print("this is cand[i]")
                #print(cand_me1[i])
                cand_me1[i+1]=[]
                for g in temp:
                    cand_me1[i+1]=cand_me1[i+1]+[g]                
                #print("letsgo")
                #print(cand_me1)
                swap=1
    
    cand_me1=cand_me1[:7]         
    return cand_me1

def xianren(board,player):#get next 3 moves and find max offset
    
    if player==10:
        op=-1
        op_c=20
    else:
        op=1
        op_c=10    
    simu_1=genboard()
    simu_1=[]
    for i in board:
        simu_1=simu_1+[i]
    simu_2=genboard()
    simu_2=[]
    for i in board:
        simu_2=simu_2+[i]
    step_1valueresult=[]    
    step_1=genmove(board,player)
    for i in step_1:
        step_1valueresult=step_1valueresult+[i[1]]
    
    #print("step1"+str(step_1))
    print("30%")
    step_2=[]
    step_2temp=[]
    step_2value=[[],[],[],[],[],[],[]]
    step_2valueresult=[-10000,-10000,-10000,-10000,-10000,-10000,-10000]
    step_2result=[[],[],[],[],[],[],[]]
    for i in range(0,len(step_1),1):
        simu_1=[]
        for j in board:
            simu_1=simu_1+[j]
        gogo(simu_1,step_1[i][0])
        step_2temp=genmove(simu_1,op_c)

        for j in step_2temp:
            step_2value[i]=step_2value[i]+[j[1]]
        step_2=step_2+[step_2temp]
    for i in range(0, len(step_2value),1):
        for j in range(0,len(step_2value[i]),1):
           # print(step_2valueresult[i])
           # print(step_2value[i][j])
            if step_2valueresult[i]<step_2value[i][j]:
                step_2valueresult[i]=step_2value[i][j]
                step_2result[i]=step_2[i][j]        
   # print(step_2result)
    #print(step_2valueresult)
    print("60%")
    step_3=[]
    step_3temp=[]
    step_3value=[[],[],[],[],[],[],[]]
    step_3valueresult=[-10000,-10000,-10000,-10000,-10000,-10000,-10000]
    step_3result=[[],[],[],[],[],[],[]]        
    for i in range(0,len(step_2result),1):
        simu_2=[]
        for j in board:
            simu_2=simu_2+[j]
        gogo(simu_1,step_1[i][0])
        gogo(simu_2,step_2result[i][0])
        step_3temp=genmove(simu_2,player)
    
        for j in step_3temp:
            step_3value[i]=step_3value[i]+[j[1]]
        step_3=step_3+[step_3temp]
        
    for i in range(0, len(step_3value),1):
        for j in range(0,len(step_3value[i]),1):
               # print(step_2valueresult[i])
               # print(step_2value[i][j])
            if step_3valueresult[i]<step_3value[i][j]:
                step_3valueresult[i]=step_3value[i][j]
                step_3result[i]=step_3[i][j]        
       # print(step_2result)
    #print(step_3)
    #print(step_3valueresult) 
    print("90%")
    valueresult=[]
    for i in range(0,7,1):
        valueresult=valueresult+[step_1valueresult[i]-step_2valueresult[i]+step_3valueresult[i]]
    #print(valueresult)
    winvalue=-10000
    winnermove=[]
    for i in range(0,7,1):
        if winvalue<valueresult[i]:
            winvalue=valueresult[i]
            winnermove=step_1[i]
    #print(step_1)
    #print(valueresult)
    #print(step_2result)
    #print(step_1valueresult)
    #print(step_2valueresult)
    #print(step_3valueresult)
    print(63-winnermove[0][0],63-winnermove[0][1])
    #print(getpos(winnermove[0][0]),getpos(winnermove[0][1]))

    return winnermove  



def accepto2(ai):# game 
    x=genboard()
    printboard(x)
    winner=0
    gameover=False
    while gameover==False:
        if ai==20:

            check_w=0
            while check_w==0:
                wmove=getmove(10)
                check_1=GetPlayerPositions(x,10)
                a=0
                for j in check_1:
                    if j==wmove[0]:
                        a=1
                if a==0:
                    print("yo your chess is not even there!")
                    
                check_2=GetPieceLegalMoves(x,wmove[0])
                b=0
                if a==1:
                    for j in check_2:
                        if j==wmove[1]:
                            b=1            
                    if b==0:
                        print("yo watch out you can not go there!")
                if((a==1)and(b==1)):
                    check_w==1
                    break
            temp=x[wmove[0]]
            x[wmove[0]]=0
            x[wmove[1]]=temp
            if win(x)==-1:
                winner=-1
                gameover==True
                print("white win!")
                return True
            elif win(x)==1:
                winner=1
                print("black win!")
                return True 
            printboard(x)
            
            black=xianren(x,20)
            gogo(x,black[0])
            if win(x)==-1:
                winner=-1
                gameover==True
                print("white win!")
                return True
            elif win(x)==1:
                winner=1
                print("black win!")
                return True         
            printboard(x)
            
        if ai==10:
            white=xianren(x,10)
            gogo(x,white[0])
            if win(x)==-1:
                winner=-1
                gameover==True
                print("white win!")
                return True
            elif win(x)==1:
                winner=1
                print("black win!")
                return True       
            printboard(x)            
            
            check_b=0            
        
            while check_b==0:
                bmove=getmove(20)
                check_1=GetPlayerPositions(x,20)
                a=0
                for j in check_1:
                    if j==bmove[0]:
                        a=1
                if a==0:
                    print("yo your chess is not even there!")
                check_2=GetPieceLegalMoves(x,bmove[0])
                b=0
                if a==1:
                    for j in check_2:
                        if j==bmove[1]:
                            b=1
                    if b==0:
                        print("yo watch out you can not go there!")
                if((a==1)and(b==1)):
                    check_b==1
                    break
            temp=x[bmove[0]]
            x[bmove[0]]=0
            x[bmove[1]]=temp
            if win(x)==-1:
                winner=-1
                gameover==True
                print("white win!")
                return True
            elif win(x)==1:
                winner=1
                print("black win!")
                return True         
            printboard(x)
    return True




def chessPlayer(board,player):
 
    if player==10:
        op=-1
        op_c=20
    else:
        op=1
        op_c=10    
    simu_1=genboard()
    simu_1=[]
    for i in board:
        simu_1=simu_1+[i]
    simu_2=genboard()
    simu_2=[]
    for i in board:
        simu_2=simu_2+[i]
    step_1valueresult=[]    
    step_1=genmove(board,player)
    for i in step_1:
        step_1valueresult=step_1valueresult+[i[1]]
    
    #print("step1"+str(step_1))
    print("30%")
    step_2=[]
    step_2temp=[]
    step_2value=[[],[],[],[],[],[],[]]
    step_2valueresult=[-10000,-10000,-10000,-10000,-10000,-10000,-10000]
    step_2result=[[],[],[],[],[],[],[]]
    for i in range(0,len(step_1),1):
        simu_1=[]
        for j in board:
            simu_1=simu_1+[j]
        gogo(simu_1,step_1[i][0])
        step_2temp=genmove(simu_1,op_c)

        for j in step_2temp:
            step_2value[i]=step_2value[i]+[j[1]]
        step_2=step_2+[step_2temp]
    for i in range(0, len(step_2value),1):
        for j in range(0,len(step_2value[i]),1):
           # print(step_2valueresult[i])
           # print(step_2value[i][j])
            if step_2valueresult[i]<step_2value[i][j]:
                step_2valueresult[i]=step_2value[i][j]
                step_2result[i]=step_2[i][j]        
   # print(step_2result)
    #print(step_2valueresult)
    print("60%")
    step_3=[]
    step_3temp=[]
    step_3value=[[],[],[],[],[],[],[]]
    step_3valueresult=[-10000,-10000,-10000,-10000,-10000,-10000,-10000]
    step_3result=[[],[],[],[],[],[],[]]        
    for i in range(0,len(step_2result),1):
        simu_2=[]
        for j in board:
            simu_2=simu_2+[j]
        gogo(simu_1,step_1[i][0])
        gogo(simu_2,step_2result[i][0])
        step_3temp=genmove(simu_2,player)
    
        for j in step_3temp:
            step_3value[i]=step_3value[i]+[j[1]]
        step_3=step_3+[step_3temp]
        
    for i in range(0, len(step_3value),1):
        for j in range(0,len(step_3value[i]),1):
               # print(step_2valueresult[i])
               # print(step_2value[i][j])
            if step_3valueresult[i]<step_3value[i][j]:
                step_3valueresult[i]=step_3value[i][j]
                step_3result[i]=step_3[i][j]        
       # print(step_2result)
    #print(step_3)
    #print(step_3valueresult) 
    print("90%")
    valueresult=[]
    for i in range(0,7,1):
        valueresult=valueresult+[step_1valueresult[i]-step_2valueresult[i]+step_3valueresult[i]]
    #print(valueresult)
    winvalue=-10000
    winnermove=[]
    for i in range(0,7,1):
        if winvalue<valueresult[i]:
            winvalue=valueresult[i]
            winnermove=step_1[i]
    rs=[]
    for i in range(0,7,1):
        rs=rs+[[step_1[i][0],valueresult[i]]]
    winnermove[0][0]=63-winnermove[0][0]
    winnermove[0][1]=63-winnermove[0][1]
    for i in step_1:
        i[0][0]=63-i[0][0]
        i[0][1]=63-i[0][1]
    print(winnermove)
    return[True,winnermove[0],rs,[step_1[0],[step_1[1],[step_1[3],step_1[4]]],[step_1[2],[step_1[5],step_1[6]]]]]
    









def accepto3(ai):# game 
    x=genboard()
    printboard(x)
    winner=0
    gameover=False
    while gameover==False:
        if ai==20:


                
            white=xianren(x,10)
            gogo(x,white[0])
            if win(x)==-1:
                winner=-1
                gameover==True
                print("White Win!")
                return True
            elif win(x)==1:
                winner=1
                print("black win!")
                return True
            printboard(x)      
            black=xianren(x,20)
            gogo(x,black[0])
            if win(x)==-1:
                winner=-1
                gameover==True
                print("white win!")
                return True
            elif win(x)==1:
                winner=1
                print("black win!")
                return True            
            printboard(x)
            
        if ai==10:
            white=xianren(x,10)
            gogo(x,white[0])
            if win(x)==-1:
                winner=-1
                gameover==True
                print("white win!")
                return True
            elif win(x)==1:
                winner=1
                print("black win!")
                return True       
            printboard(x)            
            
            check_b=0            
        
            while check_b==0:
                bmove=getmove(20)
                check_1=GetPlayerPositions(x,20)
                a=0
                for j in check_1:
                    if j==bmove[0]:
                        a=1
                if a==0:
                    print("yo your chess is not even there!")
                check_2=GetPieceLegalMoves(x,bmove[0])
                b=0
                if a==1:
                    for j in check_2:
                        if j==bmove[1]:
                            b=1
                    if b==0:
                        print("yo watch out you can not go there!")
                if((a==1)and(b==1)):
                    check_b==1
                    break
            temp=x[bmove[0]]
            x[bmove[0]]=0
            x[bmove[1]]=temp
            if win(x)==-1:
                winner=-1
                gameover==True
                print("white win!")
                return True
            elif win(x)==1:
                winner=1
                print("black win!")
                return True       
            printboard(x)
    return True





x=genboard()
#printboard(x)
#print(GetPlayerPositions(x,20))
#print(GetPieceLegalMoves(x,56))
#print(IsPositionUnderThreat(x,48,10))
#print(genmove(x,10))

aiposition=input("type 10 to play as black side, type 20 to play as white side,type 30 to watch ai vs ai")
if aiposition==30:
    accepto3(20)
else:
    print("type in the position of the chess you wish to move when it shows:'player which gogo?',then type the position that you want the chess to go to when it shows:'player where gogo?'")
    accepto2(aiposition)
#xianren(x,20)
#print(chessPlayer(x,20))
