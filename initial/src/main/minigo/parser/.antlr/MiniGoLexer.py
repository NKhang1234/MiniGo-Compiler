# Generated from c:/Code/PPL_Asssignment/initial/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO

 
from lexererr import *


def serializedATN():
    return [
        4,0,63,530,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,
        71,2,72,7,72,2,73,7,73,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,
        3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,
        6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,
        1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,
        1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,
        1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,22,1,22,
        1,23,1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,26,1,27,1,27,1,27,1,28,
        1,28,1,29,1,29,1,29,1,30,1,30,1,31,1,31,1,31,1,32,1,32,1,32,1,33,
        1,33,1,33,1,34,1,34,1,35,1,35,1,36,1,36,1,36,1,37,1,37,1,37,1,38,
        1,38,1,38,1,39,1,39,1,39,1,40,1,40,1,40,1,41,1,41,1,41,1,42,1,42,
        1,43,1,43,1,44,1,44,1,45,1,45,1,46,1,46,1,47,1,47,1,48,1,48,1,49,
        1,49,1,50,1,50,1,51,1,51,1,52,1,52,1,53,1,53,1,54,1,54,3,54,349,
        8,54,1,54,1,54,1,54,5,54,354,8,54,10,54,12,54,357,9,54,1,55,1,55,
        1,55,1,55,3,55,363,8,55,1,55,1,55,1,56,1,56,1,56,5,56,370,8,56,10,
        56,12,56,373,9,56,3,56,375,8,56,1,57,1,57,1,57,4,57,380,8,57,11,
        57,12,57,381,1,58,1,58,1,58,4,58,387,8,58,11,58,12,58,388,1,59,1,
        59,1,59,4,59,394,8,59,11,59,12,59,395,1,60,1,60,3,60,400,8,60,1,
        61,4,61,403,8,61,11,61,12,61,404,1,61,1,61,5,61,409,8,61,10,61,12,
        61,412,9,61,1,62,4,62,415,8,62,11,62,12,62,416,1,62,1,62,4,62,421,
        8,62,11,62,12,62,422,1,62,1,62,3,62,427,8,62,1,62,4,62,430,8,62,
        11,62,12,62,431,1,63,1,63,1,63,5,63,437,8,63,10,63,12,63,440,9,63,
        1,63,1,63,1,63,1,64,1,64,1,65,1,65,1,65,1,65,1,65,1,65,1,65,1,65,
        1,65,1,65,3,65,457,8,65,1,66,1,66,1,66,1,66,5,66,463,8,66,10,66,
        12,66,466,9,66,1,66,3,66,469,8,66,1,66,1,66,1,67,1,67,1,67,1,67,
        1,67,5,67,478,8,67,10,67,12,67,481,9,67,1,67,1,67,1,67,1,67,1,67,
        1,68,1,68,1,68,1,68,1,69,4,69,493,8,69,11,69,12,69,494,1,69,1,69,
        1,70,1,70,1,70,1,71,1,71,1,71,5,71,505,8,71,10,71,12,71,508,9,71,
        1,71,1,71,1,71,1,72,1,72,1,72,5,72,516,8,72,10,72,12,72,519,9,72,
        1,72,1,72,1,72,1,72,3,72,525,8,72,1,72,1,72,1,73,1,73,0,0,74,1,1,
        3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,
        29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,25,
        51,26,53,27,55,28,57,29,59,30,61,31,63,32,65,33,67,34,69,35,71,36,
        73,37,75,38,77,39,79,40,81,41,83,42,85,43,87,44,89,45,91,46,93,47,
        95,48,97,49,99,50,101,51,103,52,105,0,107,0,109,53,111,54,113,0,
        115,0,117,0,119,0,121,55,123,0,125,0,127,56,129,0,131,0,133,57,135,
        58,137,59,139,60,141,0,143,61,145,62,147,63,1,0,17,2,0,65,90,97,
        122,1,0,48,57,1,0,49,57,2,0,66,66,98,98,1,0,48,49,2,0,79,79,111,
        111,1,0,48,55,2,0,88,88,120,120,3,0,48,57,65,70,97,102,2,0,69,69,
        101,101,2,0,43,43,45,45,3,0,10,10,34,34,92,92,1,0,10,10,1,1,10,10,
        2,0,42,42,47,47,3,0,9,9,12,13,32,32,5,0,34,34,92,92,110,110,114,
        114,116,116,553,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,
        0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,
        0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,
        0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,
        0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,
        0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,
        0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,
        0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,
        0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,0,0,0,
        0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,0,0,0,0,97,1,0,0,0,
        0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,0,0,109,1,0,0,0,0,111,1,0,
        0,0,0,121,1,0,0,0,0,127,1,0,0,0,0,133,1,0,0,0,0,135,1,0,0,0,0,137,
        1,0,0,0,0,139,1,0,0,0,0,143,1,0,0,0,0,145,1,0,0,0,0,147,1,0,0,0,
        1,149,1,0,0,0,3,151,1,0,0,0,5,154,1,0,0,0,7,159,1,0,0,0,9,163,1,
        0,0,0,11,170,1,0,0,0,13,175,1,0,0,0,15,180,1,0,0,0,17,187,1,0,0,
        0,19,197,1,0,0,0,21,204,1,0,0,0,23,208,1,0,0,0,25,214,1,0,0,0,27,
        222,1,0,0,0,29,228,1,0,0,0,31,232,1,0,0,0,33,241,1,0,0,0,35,247,
        1,0,0,0,37,253,1,0,0,0,39,257,1,0,0,0,41,262,1,0,0,0,43,268,1,0,
        0,0,45,270,1,0,0,0,47,272,1,0,0,0,49,274,1,0,0,0,51,276,1,0,0,0,
        53,278,1,0,0,0,55,281,1,0,0,0,57,284,1,0,0,0,59,286,1,0,0,0,61,289,
        1,0,0,0,63,291,1,0,0,0,65,294,1,0,0,0,67,297,1,0,0,0,69,300,1,0,
        0,0,71,302,1,0,0,0,73,304,1,0,0,0,75,307,1,0,0,0,77,310,1,0,0,0,
        79,313,1,0,0,0,81,316,1,0,0,0,83,319,1,0,0,0,85,322,1,0,0,0,87,324,
        1,0,0,0,89,326,1,0,0,0,91,328,1,0,0,0,93,330,1,0,0,0,95,332,1,0,
        0,0,97,334,1,0,0,0,99,336,1,0,0,0,101,338,1,0,0,0,103,340,1,0,0,
        0,105,342,1,0,0,0,107,344,1,0,0,0,109,348,1,0,0,0,111,362,1,0,0,
        0,113,374,1,0,0,0,115,376,1,0,0,0,117,383,1,0,0,0,119,390,1,0,0,
        0,121,399,1,0,0,0,123,402,1,0,0,0,125,414,1,0,0,0,127,433,1,0,0,
        0,129,444,1,0,0,0,131,456,1,0,0,0,133,458,1,0,0,0,135,472,1,0,0,
        0,137,487,1,0,0,0,139,492,1,0,0,0,141,498,1,0,0,0,143,501,1,0,0,
        0,145,512,1,0,0,0,147,528,1,0,0,0,149,150,5,95,0,0,150,2,1,0,0,0,
        151,152,5,105,0,0,152,153,5,102,0,0,153,4,1,0,0,0,154,155,5,101,
        0,0,155,156,5,108,0,0,156,157,5,115,0,0,157,158,5,101,0,0,158,6,
        1,0,0,0,159,160,5,102,0,0,160,161,5,111,0,0,161,162,5,114,0,0,162,
        8,1,0,0,0,163,164,5,114,0,0,164,165,5,101,0,0,165,166,5,116,0,0,
        166,167,5,117,0,0,167,168,5,114,0,0,168,169,5,110,0,0,169,10,1,0,
        0,0,170,171,5,102,0,0,171,172,5,117,0,0,172,173,5,110,0,0,173,174,
        5,99,0,0,174,12,1,0,0,0,175,176,5,116,0,0,176,177,5,121,0,0,177,
        178,5,112,0,0,178,179,5,101,0,0,179,14,1,0,0,0,180,181,5,115,0,0,
        181,182,5,116,0,0,182,183,5,114,0,0,183,184,5,117,0,0,184,185,5,
        99,0,0,185,186,5,116,0,0,186,16,1,0,0,0,187,188,5,105,0,0,188,189,
        5,110,0,0,189,190,5,116,0,0,190,191,5,101,0,0,191,192,5,114,0,0,
        192,193,5,102,0,0,193,194,5,97,0,0,194,195,5,99,0,0,195,196,5,101,
        0,0,196,18,1,0,0,0,197,198,5,115,0,0,198,199,5,116,0,0,199,200,5,
        114,0,0,200,201,5,105,0,0,201,202,5,110,0,0,202,203,5,103,0,0,203,
        20,1,0,0,0,204,205,5,105,0,0,205,206,5,110,0,0,206,207,5,116,0,0,
        207,22,1,0,0,0,208,209,5,102,0,0,209,210,5,108,0,0,210,211,5,111,
        0,0,211,212,5,97,0,0,212,213,5,116,0,0,213,24,1,0,0,0,214,215,5,
        98,0,0,215,216,5,111,0,0,216,217,5,111,0,0,217,218,5,108,0,0,218,
        219,5,101,0,0,219,220,5,97,0,0,220,221,5,110,0,0,221,26,1,0,0,0,
        222,223,5,99,0,0,223,224,5,111,0,0,224,225,5,110,0,0,225,226,5,115,
        0,0,226,227,5,116,0,0,227,28,1,0,0,0,228,229,5,118,0,0,229,230,5,
        97,0,0,230,231,5,114,0,0,231,30,1,0,0,0,232,233,5,99,0,0,233,234,
        5,111,0,0,234,235,5,110,0,0,235,236,5,116,0,0,236,237,5,105,0,0,
        237,238,5,110,0,0,238,239,5,117,0,0,239,240,5,101,0,0,240,32,1,0,
        0,0,241,242,5,98,0,0,242,243,5,114,0,0,243,244,5,101,0,0,244,245,
        5,97,0,0,245,246,5,107,0,0,246,34,1,0,0,0,247,248,5,114,0,0,248,
        249,5,97,0,0,249,250,5,110,0,0,250,251,5,103,0,0,251,252,5,101,0,
        0,252,36,1,0,0,0,253,254,5,110,0,0,254,255,5,105,0,0,255,256,5,108,
        0,0,256,38,1,0,0,0,257,258,5,116,0,0,258,259,5,114,0,0,259,260,5,
        117,0,0,260,261,5,101,0,0,261,40,1,0,0,0,262,263,5,102,0,0,263,264,
        5,97,0,0,264,265,5,108,0,0,265,266,5,115,0,0,266,267,5,101,0,0,267,
        42,1,0,0,0,268,269,5,43,0,0,269,44,1,0,0,0,270,271,5,45,0,0,271,
        46,1,0,0,0,272,273,5,42,0,0,273,48,1,0,0,0,274,275,5,47,0,0,275,
        50,1,0,0,0,276,277,5,37,0,0,277,52,1,0,0,0,278,279,5,61,0,0,279,
        280,5,61,0,0,280,54,1,0,0,0,281,282,5,33,0,0,282,283,5,61,0,0,283,
        56,1,0,0,0,284,285,5,60,0,0,285,58,1,0,0,0,286,287,5,60,0,0,287,
        288,5,61,0,0,288,60,1,0,0,0,289,290,5,62,0,0,290,62,1,0,0,0,291,
        292,5,62,0,0,292,293,5,61,0,0,293,64,1,0,0,0,294,295,5,38,0,0,295,
        296,5,38,0,0,296,66,1,0,0,0,297,298,5,124,0,0,298,299,5,124,0,0,
        299,68,1,0,0,0,300,301,5,33,0,0,301,70,1,0,0,0,302,303,5,61,0,0,
        303,72,1,0,0,0,304,305,5,58,0,0,305,306,5,61,0,0,306,74,1,0,0,0,
        307,308,5,43,0,0,308,309,5,61,0,0,309,76,1,0,0,0,310,311,5,45,0,
        0,311,312,5,61,0,0,312,78,1,0,0,0,313,314,5,42,0,0,314,315,5,61,
        0,0,315,80,1,0,0,0,316,317,5,47,0,0,317,318,5,61,0,0,318,82,1,0,
        0,0,319,320,5,37,0,0,320,321,5,61,0,0,321,84,1,0,0,0,322,323,5,46,
        0,0,323,86,1,0,0,0,324,325,5,58,0,0,325,88,1,0,0,0,326,327,5,40,
        0,0,327,90,1,0,0,0,328,329,5,41,0,0,329,92,1,0,0,0,330,331,5,123,
        0,0,331,94,1,0,0,0,332,333,5,125,0,0,333,96,1,0,0,0,334,335,5,91,
        0,0,335,98,1,0,0,0,336,337,5,93,0,0,337,100,1,0,0,0,338,339,5,44,
        0,0,339,102,1,0,0,0,340,341,5,59,0,0,341,104,1,0,0,0,342,343,7,0,
        0,0,343,106,1,0,0,0,344,345,7,1,0,0,345,108,1,0,0,0,346,349,3,105,
        52,0,347,349,5,95,0,0,348,346,1,0,0,0,348,347,1,0,0,0,349,355,1,
        0,0,0,350,354,3,105,52,0,351,354,3,107,53,0,352,354,5,95,0,0,353,
        350,1,0,0,0,353,351,1,0,0,0,353,352,1,0,0,0,354,357,1,0,0,0,355,
        353,1,0,0,0,355,356,1,0,0,0,356,110,1,0,0,0,357,355,1,0,0,0,358,
        363,3,113,56,0,359,363,3,115,57,0,360,363,3,117,58,0,361,363,3,119,
        59,0,362,358,1,0,0,0,362,359,1,0,0,0,362,360,1,0,0,0,362,361,1,0,
        0,0,363,364,1,0,0,0,364,365,6,55,0,0,365,112,1,0,0,0,366,375,5,48,
        0,0,367,371,7,2,0,0,368,370,3,107,53,0,369,368,1,0,0,0,370,373,1,
        0,0,0,371,369,1,0,0,0,371,372,1,0,0,0,372,375,1,0,0,0,373,371,1,
        0,0,0,374,366,1,0,0,0,374,367,1,0,0,0,375,114,1,0,0,0,376,377,5,
        48,0,0,377,379,7,3,0,0,378,380,7,4,0,0,379,378,1,0,0,0,380,381,1,
        0,0,0,381,379,1,0,0,0,381,382,1,0,0,0,382,116,1,0,0,0,383,384,5,
        48,0,0,384,386,7,5,0,0,385,387,7,6,0,0,386,385,1,0,0,0,387,388,1,
        0,0,0,388,386,1,0,0,0,388,389,1,0,0,0,389,118,1,0,0,0,390,391,5,
        48,0,0,391,393,7,7,0,0,392,394,7,8,0,0,393,392,1,0,0,0,394,395,1,
        0,0,0,395,393,1,0,0,0,395,396,1,0,0,0,396,120,1,0,0,0,397,400,3,
        123,61,0,398,400,3,125,62,0,399,397,1,0,0,0,399,398,1,0,0,0,400,
        122,1,0,0,0,401,403,3,107,53,0,402,401,1,0,0,0,403,404,1,0,0,0,404,
        402,1,0,0,0,404,405,1,0,0,0,405,406,1,0,0,0,406,410,5,46,0,0,407,
        409,3,107,53,0,408,407,1,0,0,0,409,412,1,0,0,0,410,408,1,0,0,0,410,
        411,1,0,0,0,411,124,1,0,0,0,412,410,1,0,0,0,413,415,3,107,53,0,414,
        413,1,0,0,0,415,416,1,0,0,0,416,414,1,0,0,0,416,417,1,0,0,0,417,
        418,1,0,0,0,418,420,5,46,0,0,419,421,3,107,53,0,420,419,1,0,0,0,
        421,422,1,0,0,0,422,420,1,0,0,0,422,423,1,0,0,0,423,424,1,0,0,0,
        424,426,7,9,0,0,425,427,7,10,0,0,426,425,1,0,0,0,426,427,1,0,0,0,
        427,429,1,0,0,0,428,430,3,107,53,0,429,428,1,0,0,0,430,431,1,0,0,
        0,431,429,1,0,0,0,431,432,1,0,0,0,432,126,1,0,0,0,433,438,5,34,0,
        0,434,437,3,129,64,0,435,437,3,131,65,0,436,434,1,0,0,0,436,435,
        1,0,0,0,437,440,1,0,0,0,438,436,1,0,0,0,438,439,1,0,0,0,439,441,
        1,0,0,0,440,438,1,0,0,0,441,442,5,34,0,0,442,443,6,63,1,0,443,128,
        1,0,0,0,444,445,8,11,0,0,445,130,1,0,0,0,446,447,5,92,0,0,447,457,
        5,110,0,0,448,449,5,92,0,0,449,457,5,116,0,0,450,451,5,92,0,0,451,
        457,5,114,0,0,452,453,5,92,0,0,453,457,5,34,0,0,454,455,5,92,0,0,
        455,457,5,92,0,0,456,446,1,0,0,0,456,448,1,0,0,0,456,450,1,0,0,0,
        456,452,1,0,0,0,456,454,1,0,0,0,457,132,1,0,0,0,458,459,5,47,0,0,
        459,460,5,47,0,0,460,464,1,0,0,0,461,463,8,12,0,0,462,461,1,0,0,
        0,463,466,1,0,0,0,464,462,1,0,0,0,464,465,1,0,0,0,465,468,1,0,0,
        0,466,464,1,0,0,0,467,469,7,13,0,0,468,467,1,0,0,0,469,470,1,0,0,
        0,470,471,6,66,2,0,471,134,1,0,0,0,472,473,5,47,0,0,473,474,5,42,
        0,0,474,479,1,0,0,0,475,478,8,14,0,0,476,478,3,135,67,0,477,475,
        1,0,0,0,477,476,1,0,0,0,478,481,1,0,0,0,479,477,1,0,0,0,479,480,
        1,0,0,0,480,482,1,0,0,0,481,479,1,0,0,0,482,483,5,42,0,0,483,484,
        5,47,0,0,484,485,1,0,0,0,485,486,6,67,2,0,486,136,1,0,0,0,487,488,
        5,10,0,0,488,489,1,0,0,0,489,490,6,68,2,0,490,138,1,0,0,0,491,493,
        7,15,0,0,492,491,1,0,0,0,493,494,1,0,0,0,494,492,1,0,0,0,494,495,
        1,0,0,0,495,496,1,0,0,0,496,497,6,69,2,0,497,140,1,0,0,0,498,499,
        5,92,0,0,499,500,8,16,0,0,500,142,1,0,0,0,501,506,5,34,0,0,502,505,
        3,129,64,0,503,505,3,131,65,0,504,502,1,0,0,0,504,503,1,0,0,0,505,
        508,1,0,0,0,506,504,1,0,0,0,506,507,1,0,0,0,507,509,1,0,0,0,508,
        506,1,0,0,0,509,510,3,141,70,0,510,511,6,71,3,0,511,144,1,0,0,0,
        512,517,5,34,0,0,513,516,3,129,64,0,514,516,3,131,65,0,515,513,1,
        0,0,0,515,514,1,0,0,0,516,519,1,0,0,0,517,515,1,0,0,0,517,518,1,
        0,0,0,518,524,1,0,0,0,519,517,1,0,0,0,520,525,5,10,0,0,521,522,5,
        13,0,0,522,525,5,10,0,0,523,525,5,0,0,1,524,520,1,0,0,0,524,521,
        1,0,0,0,524,523,1,0,0,0,525,526,1,0,0,0,526,527,6,72,4,0,527,146,
        1,0,0,0,528,529,9,0,0,0,529,148,1,0,0,0,30,0,348,353,355,362,371,
        374,381,388,395,399,404,410,416,422,426,431,436,438,456,464,468,
        477,479,494,504,506,515,517,524,5,1,55,0,1,63,1,6,0,0,1,71,2,1,72,
        3
    ]

class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    IF = 2
    ELSE = 3
    FOR = 4
    RETURN = 5
    FUNC = 6
    TYPE = 7
    STRUCT = 8
    INTERFACE = 9
    STRING = 10
    INT = 11
    FLOAT = 12
    BOOLEAN = 13
    CONST = 14
    VAR = 15
    CONTINUE = 16
    BREAK = 17
    RANGE = 18
    NIL = 19
    TRUE = 20
    FALSE = 21
    PLUS = 22
    MINUS = 23
    MULTI = 24
    DIV = 25
    MODULO = 26
    EQUAL = 27
    NOT_EQUAL = 28
    LESS_THAN = 29
    LESS_EQUAL = 30
    GREATER_THAN = 31
    GREATER_EQUAL = 32
    AND = 33
    OR = 34
    NOT = 35
    ASSIGN = 36
    ASSIGN1 = 37
    PLUS_EQUAL = 38
    MINUS_EQUAL = 39
    MULTI_EQUAL = 40
    DIV_EQUAL = 41
    MODULO_EQUAL = 42
    DOT = 43
    COLON = 44
    OPEN_ROUND = 45
    CLOSE_ROUND = 46
    OPEN_CURVE = 47
    CLOSE_CURVE = 48
    OPEN_SQUARE = 49
    CLOSE_SQUARE = 50
    COMMA = 51
    SEMICOLON = 52
    ID = 53
    INT_LIT = 54
    FLOAT_LIT = 55
    STRING_LIT = 56
    COMMENT_INLINE = 57
    COMMENT_BLOCK = 58
    NL = 59
    WS = 60
    ILLEGAL_ESCAPE = 61
    UNCLOSE_STRING = 62
    ERROR_CHAR = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'_'", "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", 
            "'struct'", "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", 
            "'='", "':='", "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", 
            "':'", "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "';'", 
            "'\\n'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "PLUS", "MINUS", "MULTI", 
            "DIV", "MODULO", "EQUAL", "NOT_EQUAL", "LESS_THAN", "LESS_EQUAL", 
            "GREATER_THAN", "GREATER_EQUAL", "AND", "OR", "NOT", "ASSIGN", 
            "ASSIGN1", "PLUS_EQUAL", "MINUS_EQUAL", "MULTI_EQUAL", "DIV_EQUAL", 
            "MODULO_EQUAL", "DOT", "COLON", "OPEN_ROUND", "CLOSE_ROUND", 
            "OPEN_CURVE", "CLOSE_CURVE", "OPEN_SQUARE", "CLOSE_SQUARE", 
            "COMMA", "SEMICOLON", "ID", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
            "COMMENT_INLINE", "COMMENT_BLOCK", "NL", "WS", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", 
                  "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                  "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", 
                  "FALSE", "PLUS", "MINUS", "MULTI", "DIV", "MODULO", "EQUAL", 
                  "NOT_EQUAL", "LESS_THAN", "LESS_EQUAL", "GREATER_THAN", 
                  "GREATER_EQUAL", "AND", "OR", "NOT", "ASSIGN", "ASSIGN1", 
                  "PLUS_EQUAL", "MINUS_EQUAL", "MULTI_EQUAL", "DIV_EQUAL", 
                  "MODULO_EQUAL", "DOT", "COLON", "OPEN_ROUND", "CLOSE_ROUND", 
                  "OPEN_CURVE", "CLOSE_CURVE", "OPEN_SQUARE", "CLOSE_SQUARE", 
                  "COMMA", "SEMICOLON", "Letter", "Digit", "ID", "INT_LIT", 
                  "Decimal", "Binary", "Octal", "Hex", "FLOAT_LIT", "No_exponent", 
                  "Exponent", "STRING_LIT", "String_Character", "String_Escape", 
                  "COMMENT_INLINE", "COMMENT_BLOCK", "NL", "WS", "ILL_ESC", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[55] = self.INT_LIT_action 
            actions[63] = self.STRING_LIT_action 
            actions[71] = self.ILLEGAL_ESCAPE_action 
            actions[72] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                if self.text[:2] == '0b' or self.text[:2] == '0B':
                    self.text = str(int(self.text[2:], 2))
                elif self.text[:2] == '0o' or self.text[:2] == '0O':
                    self.text = str(int(self.text[2:], 8))
                elif self.text[:2] == '0x' or self.text[:2] == '0X':
                    self.text = str(int(self.text[2:], 16))

     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                self.text = self.text[1:-1]
                # print(f"string lit: {self.text}")

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                self.text = self.text[1:]
                print(f"illegal escape: {self.text}")

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                if(len(self.text) >= 2 and self.text[-2] == '\r' and self.text[-1] == '\n'):
                    self.text = self.text[1:-2]
                elif(self.text[-1] == '\n'):
                    self.text = self.text[1:-1]
                else:
                    self.text = self.text[1:]

     


