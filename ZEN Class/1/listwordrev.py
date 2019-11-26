a,b,c=list(map(int,input().split()))
if(a<=100000 and b<100000 and c<100000):
	if((a+b)<c or (a+c)<b or(b+c)<a):
		print("no")
	else:
		print("yes")
