def fibo(n):       
  a=0
  b=1
  count=1
  sum=0
  
  while(count<=n):
      print(sum, end=' ')
      count=count+1
      
      a=b
      b=sum
      sum=a+b

if __name__=="__main__"
  n=int(input('Enter number of terms: '))
  fibo(n)
