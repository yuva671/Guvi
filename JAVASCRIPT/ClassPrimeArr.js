class Prime{
    constructor(array){
        this.array=array
       console.log(array.filter((number) => {
  for (var i = 2; i <= Math.sqrt(number); i++) {
    if (number % i === 0) return false;
  }
  return true;
}));
    }
}
a1=new Prime([1,3,4,5,7])