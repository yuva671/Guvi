function fromListtoObject(array){
    var a={}
    for(i=0;i<array.length;i++){
        a[array[i][0]]=array[i][1];
    }
    return a
}