s = input("Enter :") #Enter input string
count = 0
x = len(s) #length of input string length
n = 0  
m = x
v = 0
for i in range(n,x):
                k = s[i].isalpha() #if s[i] is integer then k is False
                if k == False and i >= v: 
                                a = ''  # Empty string
                                
                                if m > 0:
                                                count +=1
                                                for j in range(n,n+(int(s[i]))):
                                                                v +=1
                                                                m -=1
                                                                a +=s[j] #String concatination
                                                print("Frame",c,":",a)
                                                n = v        
                                else:
                                                break
print("No.of Frames are :",count)
print("No.of Charecters are :",len(s))

                                                

                                                
                                                
                
