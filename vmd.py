# VMD format & functions
# source : https://blog.goo.ne.jp/torisu_tetosuki/e/bc9f1c4d597341b394bd02b64597499d

from collections import namedtuple
from io import BufferedReader, TextIOWrapper
from struct import unpack

# VMD formats
VMD_HEADER       = namedtuple("VMD_HEADER",       
                                ["VmdHeader", "VmdModelName"])

VMD_MOTION_COUNT = namedtuple("VMD_MOTION_COUNT", 
                                ["Count"])

VMD_MOTION       = namedtuple("VMD_MOTION",
                                ["BoneName", "FrameNo", "Location", "Rotation", "Interpolation"])

VMD_SKIN_COUNT   = namedtuple("VMD_SKIN_COUNT",
                                ["Count"])

VMD_SKIN         = namedtuple("VMD_SKIN",
                                ["SkinName", "FrameNo", "Weight"])

VMD_CAMERA_COUNT = namedtuple("VMD_CAMERA_COUNT",
                                ["Count"])

VMD_CAMERA       = namedtuple("VMD_CAMERA",
                                ["FrameNo", "Length", "Location", "Rotation",
                                 "Interpolation", "ViewingAngle", "Perspective"])

VMD_LIGHT_COUNT  = namedtuple("VMDF_LIGHT_COUNT",
                                ["Count"])

VMD_LIGHT        = namedtuple("VMD_LIGHT",
                                ["FrameNo", "RGB", "Location"])

VMD_SELF_SHADOW_COUNT = namedtuple("VMD_SELF_SHADOW_COUNT",
                                ["Count"])

VMD_SELF_SHADOW  = namedtuple("VMD_SELF_SHADOW",
                                ["FrameNo", "Mode", "Distance"])


# function to decode bytes
def vmdread(file: BufferedReader, count: int, fmt: str) -> str|int|tuple:
    data_bytes = file.read(count)
    data = unpack(fmt, data_bytes)
    if len(data) == 1:
        if type(data[0]) == bytes:
            return data[0].rstrip(b'\x00').decode("shift-jis", errors="ignore") # str
        else:
            return data[0] # int
    else:
        return data # tuple
    

# function to write data to output file
def vmdoutput(outputfile: TextIOWrapper, content: int|str|tuple):
    if type(content) == tuple: # if needed to output each field
        for i in range(len(content)):
            print(content[i], end="", file=outputfile)
            print(" ", sep="", end="", file=outputfile)
        print("", file=outputfile)
    else:
        print(content, file=outputfile)