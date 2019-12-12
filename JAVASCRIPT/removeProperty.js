
var obj1={
    name:'john',
    age:20
};
function removeProperty(obj1,key){

    delete obj1[key];
    return obj1[key];
}
