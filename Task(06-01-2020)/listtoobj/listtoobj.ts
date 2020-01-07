function fromListtoObject(array1:any){
    var a={}
    for(let i=0;i<array1.length;i++){
        a[array1[i][0]]=array1[i][1];
    }
    return a;
}
console.log(fromListtoObject([['make', 'Ford'], ['model', 'Mustang'], ['year', 1964]]))