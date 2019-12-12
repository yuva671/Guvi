var expected = {foo: 5, bar: 6};
var actual = {foo: 5, bar: 6};
testName="Passed";
function assertObjectsEqual(actual,expected,testName){
    expected1=JSON.stringify(expected)
    actual1=JSON.stringify(actual)
    console.log(expected1)
    console.log(actual1)
    if(expected1==actual1){
        return testName;
    }else{
        return testName="Failed";
    }
        
}