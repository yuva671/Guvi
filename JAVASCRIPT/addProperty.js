function addProperty(obj,key){
    return obj[key]=true
}
const obj={}
console.log(addProperty(obj,"myProperty"))
console.log(obj)