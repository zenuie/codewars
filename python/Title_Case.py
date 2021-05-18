def title_case(title, minor_words=''):  # 這裡是設定minor_words預設值為空字串
    # 1.先將兩個字串轉成列表,並處理，minor中都是小寫，title中是先首字母大寫然後再分割
    title = title.capitalize().split()  # 注意處理順序，先將首字母大寫，然後再分割
    minor_words = minor_words.lower().split()
    # 2.列表推導式處理
    return ' '.join(words if words in minor_words else words.capitalize() for words in title)
