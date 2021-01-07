filename = "sample_runs.txt"
def find_remainder(msg,ref_poly):
    part_msg = ''
    quotient = ''
    final_rem = ''
    for bit in range(0,len(msg)):
        if(len(part_msg) < len(ref_poly)):
            part_msg = part_msg + msg[bit]
            if (len(part_msg) == len(ref_poly)):
                #find msb
                msb = part_msg[0]
                #update the quotient
                quotient = quotient + msb
                #decide rem
                if(msb == '1'):
                    rem = ref_poly
                else:
                    rem = '0' * len(ref_poly)
                #peform XOR for part msg and rem
                partial_rem = ''
                for b1 in range(0,len(part_msg)):
                    if(part_msg[b1] == rem[b1]):
                        partial_rem = partial_rem + '0'
                    else:
                        partial_rem = partial_rem +  '1'
                part_msg = partial_rem[1:]
            
    final_rem = part_msg
    return final_rem
    

def crc_check():
    fopen = open(filename,'a')
    message = input("enter the message to be sent in binary: ")
    fopen.write("message : " + message)
    fopen.write('\n')
    ref_poly = input("enter the reference polynomial: ")
    fopen.write("reference_polynomial : " + ref_poly)
    fopen.write('\n')
    #add the zeros equal to the degree of polynomial
    degree = len(ref_poly)-1
    fopen.write("zeros appended : " + str(degree))
    fopen.write('\n')
    #append the zeros to the message and fetch M'(x)
    msg = message + '0' * degree  
    # msg = 1101011000
    fopen.write("message after appending zeros : " + msg)
    fopen.write('\n')
    remainder = find_remainder(msg,ref_poly) 
    fopen.write("computed remainder : " + remainder)
    fopen.write('\n')       
    actual_msg = message + remainder
    fopen.write("Actual message : " + actual_msg)
    fopen.write('\n')  
    fopen.close()
    receiver_crc(actual_msg,ref_poly)

def receiver_crc(actual_msg, ref_poly):
    fopen = open(filename,'a')
    #changing the transmitted_msg
    insert_error = list(actual_msg)
    n = input("enter number of bits you want to manipulate in the transmitted message : ")
    fopen.write("number of bits desired to manipulate : " + n)
    fopen.write('\n')
    for count in range(0,int(n)):
        change_bit = input("enter the position of bits that you want to change : ")
        fopen.write("position of bit to manipulate : " + change_bit)
        fopen.write('\n')
        change_bit = int(change_bit)
        if (insert_error[change_bit] == '0'):
            insert_error[change_bit] = '1'
        else:
            insert_error[change_bit] = '0'
    manipulated_msg = ''
    for i in insert_error:
        manipulated_msg = manipulated_msg + i
    fopen.write("manipulated_message : " + manipulated_msg)
    fopen.write('\n')
    remainder = find_remainder(manipulated_msg,ref_poly)
    fopen.write("computed remainder : " + remainder)
    fopen.write('\n')
    remainder = int(remainder)
    if(remainder == 0):
        fopen.write("No error detected")
        fopen.write('\n')
    else:
        fopen.write("error detected")
        fopen.write('\n')
    fopen.write('')
    fopen.write('\n')
    fopen.close()

crc_check()
