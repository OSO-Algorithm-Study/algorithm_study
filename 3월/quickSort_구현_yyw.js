function swap(arr, left, right) {
  let tmp = arr[left];
  arr[left] = arr[right];
  arr[right] = tmp;
}

function partition(arr, l, r) {
  let pivot = r;
  let i = l - 1;

  for (let j = l; j <= r - 1; j++) {
    if (arr[j] <= arr[pivot]) {
      i++;
      swap(arr, i, j);
    }
  }
  swap(arr, i + 1, r);
  return i + 1;
}

function quickSort(arr, l = 0, r = arr.length - 1) {
  if (l < r) {
    p = partition(arr, l, r);

    quickSort(arr, l, p - 1);
    quickSort(arr, p + 1, r);
  }
}

let arr = [5, 3, 2, 7, 12, 8, 6, 2, 1, 15];
quickSort(arr);
console.log(arr);
