chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]
print(len(chilli_wishlist))
print(chilli_wishlist[-2])
chilli_wishlist.append('dig mat')
print(chilli_wishlist)
chilli_wishlist.extend(['kong', 'tennis ball', 'crocodle toy'])
print(chilli_wishlist)
chilli_wishlist.insert(1, 'peanut butter')
print(chilli_wishlist)


if "tennis bal" in chilli_wishlist:
    print("Chilli would like a tennis ball.")
else:
    print("Chilli doesn't feel like pleying fetch.")

#
#  if len(chilli_wishlist > 8):
#    print("Chilli wants a lot of stuff")
if "blueberries" in chilli_wishlist:
    print("Chilli wants blueberries")
else:
    chilli_wishlist.append("blueberries")
    print(chilli_wishlist)
