function objtoList(obj){
    var key=Object.keys(obj)
    var value=Object.values(obj)
    var array=[]
    for(i=0;i<key.length;i++){
      array.push(key[i],value[i]);  
    }
        
  
  return array;
}
    
