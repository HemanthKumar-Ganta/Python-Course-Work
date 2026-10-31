budget = int(input("Enter budget: "))
if budget > 10000:
    print("plan for:","Trip")
elif budget > 5000:
    print("plan for:", "Resort stay")
elif budget > 3000:
    print("plan for :","movie and dinner")
elif budget > 1000:
    print("plan for:" , "cafe and shopping")
elif budget > 500:
    print("plan for:","street food and park visit")
else:
    print("there is no plan:" "stay home")