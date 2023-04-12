const a = new Array(3).fill([0, 0, 0])
const B = a
B[0] = [1, 1, 1]
console.log(a, B)
a = a.map((value) => {
    value = [1, 1, 1]
    return value
})

console.log(a)
const b = Array.from({ length: 3 }, () => {
    return [0, 0, 0]
})
console.log(b)
console.log(a[0])

const list = [1, 2, 3]

const list2 = Array.from(list, (value) => { return [0, 0, 0] })
console.log(list) // [1,2,3]
console.log(list2) // [ [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ] ]