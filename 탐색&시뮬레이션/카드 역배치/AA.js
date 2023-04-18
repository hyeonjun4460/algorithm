const data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

const slices = [[5, 10]]
for (let i = 0; i < slices.length; i++) {
    const [a, b] = slices[i]
    const slice = data.slice(a - 1, b)
    slice.reverse()
    console.log(slice.length, b - a + 1)
    data.splice(a - 1, b - a + 1, ...slice)
}

console.log(data.join() == [1, 2, 3, 4, 10, 9, 8, 7, 6, 5, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20].join())