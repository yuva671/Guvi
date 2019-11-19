start=int(input("enter start km: "))
end=int(input("Enter end km: "))
peak=int(input())
distance=end-start
if(distance>5):
    distance=distance-5
    fare=100+(distance*8)
    print(fare)
    if(peak==1):
        fare1=(fare+(0.25*fare))
        print(fare1)
else:
    print("Fare=100")
