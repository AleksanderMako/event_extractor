from event import EventExtractor
e = EventExtractor()
sents = e.dataLoader('./data.txt')
# print(sents)
print(e.greedy(sents))
