def Get_S_box(number): #This function takes the number of the S-box and returns the corresponding S-box 

  #Every S-box is represented as a list of lists 
  #Every list in each list of lists represents a row in the corresponding S-box
  s1 =[[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
       [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
       [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
       [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]
  
  s2= [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
       [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
       [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
       [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]
  
  s3= [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
       [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
       [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
       [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]
  
  s4= [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
       [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
       [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
       [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]
  
  s5= [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
       [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
       [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
       [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]
  
  s6= [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
       [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
       [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
       [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]
  
  s7= [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
       [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
       [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
       [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]
  
  s8= [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
       [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
       [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
       [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]
  switcher = {
      1 : s1,
      2 : s2,
      3 : s3,
      4 : s4,
      5 : s5,
      6 : s6,
      7 : s7,
      8 : s8

  }
  return(switcher.get(number))


def Substitution(value , s_box): #This function takes a string of 6 bits and the desired s_box as inputs and returns a string of 4 bits after substitution
  row = int(value[0] + value[5] , 2)
  column = int(value[1]+value[2]+value[3]+ value[4] , 2)
  value = bin(s_box[row][column])[2:]
  while(len(value) < 4):
    value = '0' + value
  return value


def XOR(message,key):  
   
   if len(message)!=len(key):
      print("can not XOR two diffrent lenths")
      
   xor_result =""
   for j in range(len(message)):
        xor_result += str(int(message[j]) ^ int(key[j]))         
       
   return xor_result  
  
def expansion(message,e_bit_Selection):
   if(len(message)!=32):
      print("expansion message != 32")
      print(len(message))

   expansion_result = ''
   for row in e_bit_Selection:
      for bit_position in row:
          expansion_result += message[bit_position - 1]  
   print("expansion result is "+expansion_result)      
   return expansion_result



def Encrypt(message , keys):
  if(len(message) > 64):
    print("Input message is too long")
    print(len(message))
    print("message is "+message)
    return
  elif(len(message) < 64):
    print("Input message is too short")
    print(len(message))
    print("message is "+message)
    return
  
  #Every list in initial_permutation list of lists represents a row in the initial permutation table
  initial_permutation= [[58,50,42,34,26,18,10,2],
                        [60,52,44,36,28,20,12,4],
                        [62,54,46,38,30,22,14,6],
                        [64,56,48,40,32,24,16,8],
                        [57,49,41,33,25,17,9,1],
                        [59,51,43,35,27,19,11,3],
                        [61,53,54,37,29,21,13,5],
                        [63,55,47,39,31,23,15,7]]
  
  #Every list in e_bit_selection list of lists represents a row in the e_bit_selection_table 
  e_bit_Selection = [[32,1,2,3,4,5],
                     [4,5,6,7,8,9],
                     [8,9,10,11,12,13],
                     [12,13,14,15,16,17],
                     [16,17,18,19,20,21],
                     [20,21,22,23,24,25],
                     [24,25,26,27,28,29],
                     [28,29,30,31,32,1]]
  
  #Every list in p_function list of lists represents a row in p_function table 
  p_function = [[16,7,20,21],
                [29,12,28,17],
                [1,15,23,26],
                [5,18,31,10],
                [2,8,24,14],
                [32,27,3,9],
                [19,13,30,6],
                [22,11,4,25]]

  #Every list in final_permutation list of lists represents a row in final_premutation table 
  final_permutation = [[40,8,48,16,56,24,64,32],
                       [39,7,47,15,55,23,63,31],
                       [38,6,46,14,54,22,62,30],
                       [37,5,45,13,53,21,61,29],
                       [36,4,44,12,52,20,60,28],
                       [35,3,43,11,51,19,59,27],
                       [34,2,42,10,50,18,58,26],
                       [33,1,41,9,49,17,57,25]]

  #Write your implementation here


  #Step 1: Initial Permutation
    # Apply the initial permutation to the binary message
  permutation_result = ''
  for row in initial_permutation:
      for bit_position in row:
          permutation_result += message[bit_position - 1]

  #validating  initial permutation result
  #print(permutation_result)

  #Step 2: Splitting the message into two halves
  left = permutation_result[:32]
  #validating 
  print(left)


  right = permutation_result[32:]
  #validating 
  #print(right)
  

  #Step 3: 16 rounds of encryption
  for i in range(16):
  # print("intering the itration number "+str(i))
    #step 3.1: right part expansion
   expaneded=expansion(right,e_bit_Selection)

    #validating 
 # print(expaneded)

    #3.2 XORING
   xor_result=XOR(expaneded,keys[i])# change 0 to i 

    #validating
#  print(xor_result)

    #3.3 shrinking
   My48over6 = [xor_result[k:k+6] for k in range(0, len(xor_result), 6)]
   #validating
   print("xored res = ")
   print(My48over6)

    #3.4 Substitution 
   s_box_result = ''
   for j in range(8):  
    s_box_result+=Substitution(My48over6[j],Get_S_box(1+j)) #change 1 to i+1 and 0 to i
   #print("s box result "+s_box_result )
  
    #3.5 premutation
   p_function_result=""
   for row in p_function:
       for bit_position in row:
         p_function_result += s_box_result[bit_position - 1]
  #testing p_function_result
   #print(p_function_result)
   #print("p_function_result size = ")      
   #print(len(p_function_result))

    #3.6 XOR WITH LEFT
   XORED=XOR(p_function_result,left)  
  #print(XORED)
  #4 switch
   left=right
   right=XORED
   print("iteration num "+str(i)+" equalls")
   print(left+right)
   if i==15:
      
      tmp=left
      left=right
      right=tmp
      #print(left+right)
      finalshift=left+right

      final_result=""
      for row in final_permutation:
       for bit_position in row:
         final_result += finalshift[bit_position - 1]
      print() 
      print()  
      print("final result is "+final_result)   


     
    

message = "0000000100100011010001010110011110001001101010111100110111101111"
keys = ["000110110000001011101111111111000111000001110010",
        "011110011010111011011001110110111100100111100101",
        "010101011111110010001010010000101100111110011001",
        "011100101010110111010110110110110011010100011101",
        "011111001110110000000111111010110101001110101000",
        "011000111010010100111110010100000111101100101111",
        "111011001000010010110111111101100001100010111100",
        "111101111000101000111010110000010011101111111011",
        "111000001101101111101011111011011110011110000001",
        "101100011111001101000111101110100100011001001111",
        "001000010101111111010011110111101101001110000110",
        "011101010111000111110101100101000110011111101001",
        "100101111100010111010001111110101011101001000001",
        "010111110100001110110111111100101110011100111010",
        "101111111001000110001101001111010011111100001010",
        "110010110011110110001011000011100001011111110101"]

print(Encrypt(message, keys))#you should get 1000010111101000000100110101010000001111000010101011010000000101
                                             # 1000010111101000000100110101010000001111000010101011010000000101
                                              