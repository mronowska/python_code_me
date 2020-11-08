pieski = ["wilczarz irlandzki", "buldog angielski", "owczarek podhalański", "terier szkocki", "dalmatyńczyk", "berneński pies pasterski", "grzywacz chiński"]

#na krotke
def convert(list):
    return tuple(list)

for x in pieski:
    print(x.upper())

pieski.sort()
print(pieski)

#zamiana na krotke
print(convert(pieski))


