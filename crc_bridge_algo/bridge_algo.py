def read_bridgefdb():
    fopen = open('BridgeFDB.txt','r')
    lines = fopen.readlines()
    fopen.close()
    dict = {}
    DMAC = []
    port = []
    for i in range(0,len(lines)):
        if(i%2 == 0):
            #even index
            DMAC.append(lines[i].strip('\n'))
        else:
            #odd index
            port.append(lines[i].strip('\n'))
    for j in range(0,len(DMAC)):
        dict[DMAC[j]] = port[j]
    return dict

def into_parts(lst,size):
    return (lst[val:val+size] for val in range(0,len(lst),size))
    
def read_randomframes():
    fdb = read_bridgefdb()
    ropen = open('RandomFrames.txt','r')
    lines = ropen.readlines()
    ropen.close()
    refined_lst = []
    output = open('BridgeOutput.txt','w')
    for lin in lines:
        refined_lst.append(lin.strip('\n'))
    for grp in into_parts(refined_lst,3):
        src = grp[0]
        src_port = fdb.get(src)
        for i in grp:
            output.write(i)
            output.write('\t')
        if (src_port != None):
            if(src_port != grp[2]):
                #update fdb bridge text file
                fopen = open('BridgeFDB.txt','a')
                fopen.write('\n')
                fopen.write('---->')
                fopen.write(grp[0])
                fopen.write('\n')
                fopen.write(grp[2])
                fdb[grp[0]] = grp[2]
                fopen.close()
                open("BridgeUpdateFDB.txt", "w").writelines([lin for lin in open("BridgeFDB.txt").readlines()])
            dest_port = fdb.get(grp[1])
            if(dest_port != None):
                if (src_port == dest_port):
                    output.write("discarded as they lie on same side")
                    output.write('\t')
                else:
                    output.write("forwarded on dest port : "+ dest_port)
                    output.write('\t')
            else:
                output.write("broadcasted on all ports")
                output.write('\t')
        else:
            output.write("update")
            output.write('\t')
            fopen = open('BridgeFDB.txt','a')
            fopen.write('\n')
            fopen.write(grp[0])
            fopen.write('\n')
            fopen.write(grp[2])
            fdb[grp[0]] = grp[2]
            fopen.close()
        output.write('\n')
    output.close()

read_randomframes()