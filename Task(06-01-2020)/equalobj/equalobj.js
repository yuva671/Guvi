var expected = { prop1: { a: "fun", b: "test" }, prop2: [1, 2, 3, 4] };
var actual = { prop2: [1, 2, 3, 4], prop1: { a: "fun", b: "test" } };
function jsonEqual(expected, actual) {
    return JSON.stringify(expected) === JSON.stringify(actual);
}
console.log(jsonEqual(expected, actual));
