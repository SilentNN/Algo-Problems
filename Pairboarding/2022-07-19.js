// Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

// Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

// Example
// Input: [1, 1, 2]

// Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

// It doesn't matter what you leave beyond the new length.

/*

iterate through input
    track most recent element
        if current element is the same as most recent element, i can replace it with null
        return length of filtered array, filtering for not null

*/

const removeDupes = arr => {
    let prev;
    let nonDupes = 0;

    for (i=0; i<arr.length; i++) {
        const curr = arr[i];

        if (prev !== curr) {
            nonDupes++;
            prev = curr;
        }
    }

    return nonDupes;
};

console.log(removeDupes([1,1,2]));
console.log(removeDupes([1,1,2,3]));
console.log(removeDupes([1,1,2,2,3,4]));
console.log(removeDupes([]));