function transformFirstAndLast(array){
    var obj={}
    length1=array.length;
    lastElement=array[length1-1];
    key=array[0];
    value=lastElement;
    obj[key]=value;
    return obj;
}