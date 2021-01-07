#Exercise 1
For executing the functionality of CRC protocol, the following steps needs to be followed:
1. Execute crc_main.py as a python script
2. User will be prompted to enter the message in binary, M(x)
3. User will be prompted to enter the reference polynomial 
4. User will be prompted to enter the number of bits he/she wants to manipulate while transmitting the message to the receiver.
5. User will be prompted to enter the position of bits that he/she desires to change from 1 to 0 and vice versa.
6. If the remainder is a non-zero, then there is an error in the transmitted message, otherwise, there is no error.
7. The complete output is appended into the file sample_runs.txt.

Output sample:

message : 1101011
reference_polynomial : 1101
zeros appended : 3
message after appending zeros : 1101011000
computed remainder : 010
Actual message : 1101011010
number of bits desired to manipulate : 2
position of bit to manipulate : 4
position of bit to manipulate : 7
manipulated_message : 1101111110
computed remainder : 111
error detected

#Exercise 2
For executing the bridge processing functionality, the following steps needs to be followed:
1. Execute the bridge_algo.py as a python script.
2. Based on the RandomFrames.txt file, source_MAC is searched in the BridgeFDB.txt file,
If found, then the destination MAC is searched in the same file, if they are mapped to the same port, then the frame is discarded otherwise, it is forwarded to the port tagged to the destination MAC; if the destination is not found, then it is broadcasted on all ports.
If not found, a new source MAC is added to the BridgeFDB.txt  
3. Also, if the source port in RandomFrames.txt for a MAC does not match the source port in FDB, for the same MAC, then the BridgeFDB.txt is updated with new port as shown in RandomFrames.txt and the updated FDB is saved in BridgeUpdateFDB.txt
4. The complete output is written in file BridgeOutput.txt

Output sample:

00-00-00-11-0b-0d	00-13-46-c6-a5-35	1	forwarded on dest port : 2	
00-0c-29-51-33-c1	01-00-5e-7f-ff-64	4	discarded as they lie on same side	
01-00-5e-7f-ff-64	00-00-4f-31-fa-fb	3	broadcasted on all ports	
00-1d-60-29-cc-b2	00-1d-7d-77-de-3c	4	discarded as they lie on same side	
00-19-5b-0d-04-dc	00-21-91-f5-d5-d4	1	discarded as they lie on same side	
00-1a-4d-34-ab-cd	00-e0-4c-86-70-09	2	forwarded on dest port : 1	
00-1f-d0-c8-49-7f	00-24-1d-3a-7d-14	3	forwarded on dest port : 4	
00-11-22-33-44-55	00-1d-60-29-a5-ae	3	discarded as they lie on same side	
00-24-1d-3a-b8-2a	00-19-5b-0d-04-dc	2	forwarded on dest port : 1	
00-0c-29-33-47-6f	00-11-22-33-44-55	2	forwarded on dest port : 3	

Port updation in BridgeFDB.txt is done for the MAC, 01-00-5e-7f-ff-64 as port 3 from port 4


