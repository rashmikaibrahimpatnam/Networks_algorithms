def dectobin(decimal):
    #decimal to binary    
    bin_data = bin(decimal)
    return bin_data

def read_file(filename):
    fopen = open(filename,'r')
    lines = fopen.read()
    final = ''
    for char in lines:
        #converting the text to ascii decimals
        ascii = ord(char)
        #converting decimals to binary
        binary = dectobin(ascii)
        #removing the 0b after conversion to binary
        binary = binary.lstrip('0b')
        #checking for the length of binary obtained --> 8 bits 
        if len(binary) <= 7:
            zeros = 7 - len(binary)
            #appending the leading zeros to form 8 bit pattern
            for i in range(0,zeros): 
                binary = '0' + binary 
        final = final + binary
    fopen.close()
    return final

def stuffed_msg(msg):
    fleopen = open("bitstuffed_msg.txt",'w')
    fleopen.write(msg)
    fleopen.close()

def bitstuffing():
    count = 0
    lst = []
    #reading the input file and fetching the binary data
    fetched_binary_data = read_file('input.txt')
    for bit in fetched_binary_data:
        if bit == '1':
            count += 1
            lst.append(bit)
            if count == 5:
                #stuff an extra 0 bit after finding 5 consecutive 1's
                lst.append('0')
                count = 0
        else:
            count = 0
            lst.append(bit)
    stuffed_pattern = ''
    start_flag = end_flag = '01111110'
    message_sent = start_flag + stuffed_pattern.join(lst) + end_flag
    stuffed_msg(message_sent)

def bintodecimal(binary_data):
    #binary to decimal
    val = 0
    index = 0
    while(binary_data != 0):
        mod = binary_data % 10
        val = val + mod * pow(2,index)
        binary_data = binary_data//10
        index += 1
    return val

def dividebinary(binary_data):
    input_data = ''
    for i in range(0,len(binary_data),7):
        divided_data = int(binary_data[i:i+7])
        converttodecimal = bintodecimal(divided_data)   
        #converting ascii to string
        input_data = input_data + chr(converttodecimal)
    #appending the text into a file
    new_f = open('output.txt','w')
    new_f.write(input_data)
    new_f.close()

def read_stuffedmsg(fname):
    fopen = open(fname,'r')
    bits = fopen.read()  
    #removed the start and end flags
    bits = bits[8:len(bits)-8]
    stuffed_lst = []
    for chr in bits:
        stuffed_lst.append(chr)
    fopen.close()
    return stuffed_lst

def removebits(filename):
    stuffedlst = read_stuffedmsg(filename)
    #remove stuffed bits
    count = 0
    new_lst = []
    index = 0
    while index <len(stuffedlst):

        bit = stuffedlst[index]
        if bit == '1':
            count += 1
            new_lst.append(stuffedlst[index])
            if count == 5:
                #remove the stuffed 0 bit
                index = index + 2
                count = 0
            else:
                index += 1
        else:
            count = 0
            new_lst.append(stuffedlst[index])
            index += 1
        
    final = ''
    unstuffed = final.join(new_lst)
    dividebinary(unstuffed)

bitstuffing()
removebits('bitstuffed_msg.txt')
