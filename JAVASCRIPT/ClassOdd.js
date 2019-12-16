class OddNum{
    constructor(numbers){
        this.numbers=numbers
  var odd=numbers.filter(num=>(num%2!=0));
console.log(odd)
    }
}
n=new OddNum([1,2,3,4,5])