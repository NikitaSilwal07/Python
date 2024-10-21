#18. String, List, & Set: Given a string, find all the unique words (case-insensitive) that appear in the
#  string and return them as a sorted list.

string="Mt. Everest Trekking region - the world's best trekking destination.The Everest Region Trek is one of the most popular and exhilarating treks in the world. The trek starts and ends in Lukla, a small town in the Khumbu region of Nepal. The Everest Base Camp Trek is a once-in-a-lifetime adventure that offers breathtaking views, cultural experiences, and physical challenges that will leave you with unforgettable memories."
l=string.lower().replace(".","").split(" ") 
s=set(l) 
l=sorted(s) 
print(l) 