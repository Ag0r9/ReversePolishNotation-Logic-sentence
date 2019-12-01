def RNP()   
   ent=input().split()
   ex=['FORALL', '∀','EXISTS', '∃']       #quantifier
   neg=['NOT','¬','~']                     #negation                                
   qva=['AND', '&', '∧','OR', '|', '∨','IMPLIES', '→','IFF', '↔','XOR', '⊕']
   i=0                                     #^operators^
   while(i<len(ent)):
      c=list(ent[i])
      if (ent[i] in ex):
          ent[i]='('+ent[i]+' '+ent[i-2]+' '+ent[i-1]+')'  #quantfier+' '+variable+' '+predicate
          ent.pop(i-2)
          i -= 1                           #removing var and predic from the list  
          ent.pop(i-1)
          i-=1
      elif (ent[i] in neg):
          ent[i]=ent[i]+ent[i-1]          #negation+form
          ent.pop(i-1)                    #removing variable/constant from the list
          i-=1
      elif (ent[i] in qva):
          ent[i]=ent[i-2]+' '+ent[i]+' '+ent[i-1]           #form+' '+operaor+' '+form
          ent.pop(i - 2)
          i -= 1                          #removing forms from the list
          ent.pop(i - 1)
          i-=1
      elif (len(c)>1):                    #predicate
          if (c[1]=='/'):
              a =', '.join(ent[i-int(c[2]):i]) 
              ent[i]=c[0]+'('+ a +')'           #putting terms into predicate
              d=i-int(c[2])
              for k in range(i-int(c[2]),i):    #removing terms from the list
                  ent.pop(d)
                  i-=1
      i+=1
   print(ent[0])
RNP()
