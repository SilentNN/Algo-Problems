// // Isomorphic Strings

// // Overview: For two strings to be isomorphic, all occurrences of a character in string A can be replaced
// // with another character to get string B. The order of the characters must be preserved. There must be 
// // one-to-one mapping for every char of string A to every char of string B.

// // paper and title would return true. egg and sad would return false. dgg and add would return true.

// // isIsomorphic("egg", 'add'); // true
// // isIsomorphic("paper", 'title'); // true
// // isIsomorphic("kick", 'side'); // false

// // This problem should be completed in O(N) time and O(N) space.

// /*
//     create a map
//         represents relationship between characters of A to B
    
//     iterate through A
//         check if A is in the Map
//             if not, we can add it with the value of the char of B
//             if it is, return false if relationship is untrue for this character

//     return true after iterating
// */

// const isIsomorphic = (a, b) => {
//     // if (a.length !== b.length) return false;
//     const mapping = new Map();

//     for (i=0; i<a.length; i++) { //2
//         if (mapping.get(a[i])) { //true
//             if (mapping.get(a[i]) !== b[i]) return false;
//         } else {
//             mapping.set(a[i], b[i]); //mapping["g"] = "d"
//         }
//     }

//     return true;
// };

// console.log(isIsomorphic("egg", 'add')); // true
// console.log(isIsomorphic("paper", 'title')); // true
// console.log(isIsomorphic("kick", 'side')); // false


// Balanced Parentheses
// Overview: Write a method, isBalanced, that will evaluate if a given expression has balanced parentheses.

// Example:

// Input: "(([]))()()"

// Output: True
// Input: "([)(]))"

// Output: False

/*
    use a stack

    taking something out when it's not at the top of the stack means we return false
    return true at the end if stack is empty
*/

// const isBalanced = s => {
//     const stack = [];

//     for (char of s) {
//         if (char === '(') stack.push('(')
//         if (char === ')') {
//             if (stack.pop() !== '(') return false;
//         }
//     }

//     if (stack.length === 0) return true;
//     return false;
// };

// console.log(isBalanced('(())()()'));
// console.log(isBalanced('()())'));
// console.log(isBalanced(''));

// Trapping Rain Water

// You are given an array of n non-negative integers, where each number represents a ground elevation. Each point of elevation has a width of 1. For example, given an array [5, 2, 4, 3, 1, 4], the elevation map would look something like this:

//  ___
// |   |    ___         ___
// |   |   |   |___    |   |
// |   |___|       |   |   |
// |               |___|   |
// | 5   2   4   3   1   4 |

// Our goal is to compute how much water our elevation map would be able to trap if it rained. Referring to the above example, it would look like this if it rained:

//  ___
// |   |,,, ___ ,,,,,,, ___
// |   |///|   |///////|   |
// |   |///|       |///|   |
// |               |///|   |
// | 5   2   4   3   1   4 |

//  ___
// |   |,,, ___ 
// |   |///|   |___
// |   |///|       |
// |               |___
// | 5   2   4   3   1 |

// Thus, for an input of [5, 2, 4, 3, 1, 4], the total sum of water that would be trapped is 6 units.

// Write a method, trappedWater, that calculates this for you.


/*
    iterate once to get maximums to the left of a index [5,5,5]
    iterate again backwards for maximums to the right of index [1,3,4]
    sum stuff => sum(min(maxleft, maxright) - elev[i])
*/


const trappedWater = elevations => {
    const leftMaxes = [];
    const rightMaxes = [];
    let leftMax = 0;
    let rightMax = 0;
    let water = 0;

    for (i=0; i<elevations.length-2; i++) {
        leftMax = Math.max(leftMax, elevations[i]);
        leftMaxes[i] = leftMax;
    }

    for (i=elevations.length-1; i>1; i--) {
        rightMax = Math.max(rightMax, elevations[i]);
        rightMaxes[i-2] = rightMax;
    }

    for (i=1; i<elevations.length-1; i++) {
        let column = Math.min(leftMaxes[i-1], rightMaxes[i-1]) - elevations[i];
        if (column > 0) water += column;
    }

    return water;
};

console.log(trappedWater([5, 2, 4, 3, 1, 4]));
console.log(trappedWater([5, 2, 4, 3, 1]));
console.log(trappedWater([5, 4]));