from BitVector import BitVector
import os
from os import walk
import io

f = []
for (dirpath, dirnames, filenames) in walk(r'C:/FileDirectory'):
    f.extend(filenames)
    break

for fl in f:

#read file as bits
    # fp_read = io.StringIO(r'C:/Users/Chinmay/Google Drive/Python Files/Py files/FileDirectory/'+fl)
    # bv = BitVector(fp = fp_read)
    _hash_ = BitVector(size = 32)
    bv = BitVector(filename = r'C:/FileDirectory/'+fl)
    while (bv.more_to_read):
        bv1 = bv.read_bits_from_file(32)

        #initialize hash to all 0s 32 -bit
        for i in range(int(len(bv1)/8)):
            _hash_ << 8    #circularly shift hash by 8 positions to left
            bv_byte= bv1[i:i+7] #read byte from a file
            _hash_[25:32] = bv_byte ^ _hash_[25:32] #XOR byte from file and least signifcant 8 bits of hash
    bv.close_file_object()
    _hash_hex = _hash_.get_bitvector_in_hex() #represent hash in hex
    print('Filename :\t'+ str(fl))
    print('Hash : \t\t' + str(_hash_))
    print('Hash in Hex : \t' + str(_hash_hex) + '\n')
    FILEOUT = open('C:/outdirectory/output.txt','a')
    FILEOUT.write('File Name: '+ fl + '\n')
    FILEOUT.write('Hash for file :'+ str(_hash_)+ '\n')
    FILEOUT.close()

# to read hashes for all files from bits file use following code
# from BitVector import BitVector
# import os
# from os import walk
# import io
# bv = BitVector(filename = 'C:/outdirectory/output.bits')
# bv2 = bv.read_bits_from_file(32)
# print(bv2)
