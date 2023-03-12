function merge(left, right) {
  const result = [];
  while (left.length && right.length) {
    if (left[0] < right[0]) {
      result.push(left.shift());
    } else {
      result.push(right.shift());
    }
  }
  return [...result, ...left, ...right];
}

function mergeSort(arr) {
  if (arr.length === 1) return arr;

  let boundary = Math.ceil(arr.length / 2);

  const left = arr.slice(0, boundary);
  const right = arr.slice(boundary);

  return merge(mergeSort(left), mergeSort(right));
}

const arr = [5, 3, 2, 7, 12, 8, 6, 1, 15];
const sortarr = mergeSort(arr);
console.log(arr);
console.log(sortarr);
