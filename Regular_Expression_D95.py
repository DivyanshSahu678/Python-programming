#Day 95

#understand the concept of regular expression in python

import re

pattern = "rag"
text = ''' uejkr.bsdeaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaauba.ejkdzsenkldvsz eioe;hragnv ssw9;eoh.sbjkvd.bsdeaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaauba.ejkdzsenkldvsz eioe;hragnv ssw9;eoh.sbjkvd.bsdeaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaauba.ejkdzsenkldvsz eioe;hragnv ssw9;eoh.sbjkvd.bsdeaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaauba.ejkdzsenkldvsz eioe;hragnv ssw9;eoh.sbjkvd'''

match = re.search(pattern,text)
print(match)

match = re.finditer(pattern,text)
for matches in match:
    print(matches.span())