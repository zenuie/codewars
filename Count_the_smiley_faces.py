# 描述：
# 給定一個數組（arr）作為參數完成countSmileys應該返回笑臉總數的函數。 笑臉的
# 規則：
# - 每個笑臉必須包含一雙有效的眼睛。眼睛可以標記為:或;
# - 笑臉可以有鼻子，但它沒有。鼻子的有效字符是-或 - ~
# 每個笑臉必須有一個微笑的嘴，應該用)或標記 D。
# 除了提到的字符外，不允許使用其他字符。
# 有效的笑臉例子：
# :) :D ;-D :~)
# 無效的笑臉：
# ;( :> :} :]
def count_smileys(arr):
    eyes = ":", ";"  # 眼睛符號
    nose = "-", "~"  # 鼻子符號
    smiley = "D", ")"  # 嘴巴符號
    arr=[]
    if arr.count(eyes) > 0 :
        if arr.count(smiley) > 0:
            return arr.count(smiley)
    else:
        return 0