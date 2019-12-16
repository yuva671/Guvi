class SumA{
    constructor(array){
        this.array=array
        console.log(array.reduce((a,b)=>(a+b)));
    }
}
sum=new SumA([1,2,3,4,5])