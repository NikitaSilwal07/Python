#15. List, Dictionary, & String: Given a list of sentences,create a dictionary where each key
#  is a unique word and the value is the total number of sentences in which that word appears.

l=["Mt. Everest Trekking region - the world's best trekking destination. The Everest Region Trek is one of the most popular and exhilarating treks in the world. The trek starts and ends in Lukla, a small town in the Khumbu region of Nepal. The Everest Base Camp Trek is a once-in-a-lifetime adventure that offers breathtaking views, cultural experiences, and physical challenges that will leave you with unforgettable memories."]
d={} 
for sentence in l: 
    words=sentence.lower().replace(".","").replace(",","").split() 
    count_word=[] 
    for word in words: 
        if word not in count_word: 
            if word in d: 
                d[word]+=1 
            else: 
                d[word]=1 
            count_word.append(word) 
 
print(d) 