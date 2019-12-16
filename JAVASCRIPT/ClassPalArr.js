class Palindrome{
    constructor(array){
        this.array=array;
    console.log(array.filter(x=>(x.split('').reverse().join('')===x)))
    }
}
a=new Palindrome(['dad','mum','malayalam','fgdfdf','geg','121'])