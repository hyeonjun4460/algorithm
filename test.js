function test() {
    return this.name
}

const a = {
    name: 'a'
}

console.log(test.call(a)) // a
const test2 = test.bind(a)
console.log(test2) // function
test2() // a
console.log(test.apply(a)) // a