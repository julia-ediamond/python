mailing_list = [
    ["Chilli", "chilli@thechihuahua.com"],
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["Ivy", "noreply@goldendreamers.xyz"],
]

# for result in range(len(mailing_list)):
#    print(f"{mailing_list[0][0]}: {mailing_list[0][1]}")
# for i in range(len(mailing_list)):
#    print(f"{mailing_list[i]}: ")

i = mailing_list[0][0]
j = mailing_list[0][1]
for i in range(len(mailing_list)):      # runs for every "sub-list" in a
    for j in mailing_list[i]:           # gives j the value of each item in a[i]
        print(f"{j}: ")    # prints j without going to a new line
    # print()                  # creates a new line after each list-in-list prints
