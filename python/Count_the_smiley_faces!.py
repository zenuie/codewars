def count_smileys(arr):
    count = 0
    for i in arr:
        if i == ":D" or i == ":-D" or i == ":~D" or i == ":)" or i == ":-)" or i == ":~)" or i == ";D" or i == ";-D" or i == ";~D" or i == ";)" or i == ";-)" or i == ";~)":
            count+=1
    return count
