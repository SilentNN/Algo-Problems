// // Medium

// // A self-dividing number is a number that is divisible by every digit it contains. For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0,and 128 % 8 == 0.

// // Also, a self-dividing number is not allowed to contain the digit zero.

// // Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
// // Example

// //     Input: left = 1, right = 22
// //     Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

// /*
// iterate left to right
// check each number if self dividing
//     convert the number to string
//     iterate through the string, converting each char to an integer
//         if integer is 0, continue
//         check if this integer divides into original number
//             if yes, add to array
// */

// const sdn = (left, right) => {
//     const res = [];

//     for (i=left;i<=right;i++) {
//         const str = String(i);
//         let k = 0
//         for (j=0; j<str.length; j++) {
//             const digit = parseInt(str[j]);

//             if (digit !== 0 && i % digit === 0) k++;
//         }
//         if (k === str.length) res.push(i);
//     }

//     return res;
// }


// console.log(sdn(1,22));


// // Hard

// // In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings,
// // by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well.

// // At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right
// // must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.

// // What is the maximum total sum that the height of the buildings can be increased?
// // Example

// //     Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
// //     Output: 35

// def max_increase_keeping_skyline(grid)

//     y_line = []
//     (0...grid.length).each do |y|
//         y_line << grid[y].max
//     end

//     x_line = []
//     (0...grid[0].length).each do |x|
//         x_line << grid.transpose[x].max
//     end

//     output = 0

//     (0...grid.length).each_with_index do |y, y_i|
//         (0...grid[0].length).each_with_index do |x, x_i|
//             max = [y_line[y_i], x_line[x_i]].min
//             if grid[y][x] < max
//                 output += max - grid[y][x]
//             end
//         end
//     end

//     output
// end

// const maxIncreaseKeepingSkyline = grid => {
//     const maxXArr = [];
//     const maxYArr = [];
//     const length = grid.length;
//     let maxIncrease = 0;
    
//     for (let i = 0; i < length; ++i) {
//         let rowMax = 0;
//         let colMax = 0;
        
//         for (let j = 0; j < length; ++j) {
//             const row = grid[i][j];
//             const col = grid[j][i];
            
//             rowMax = row > rowMax ? row : rowMax;
//             colMax = col > colMax ? col : colMax;
//         }
        
//         maxXArr.push(rowMax);
//         maxYArr.push(colMax);
//     }
    
//     for (let i = 0; i < length * length; ++i) {
//         const x = i % length;
//         const y = Math.floor(i / length);
        
//         const minMaxHeight = Math.min(maxXArr[y], maxYArr[x]);
        
//         maxIncrease += minHeight - grid[x][y];
//     }
    
//     return maxIncrease;
// };

// Given a string s, find the longest palindromic substring in s.

// Example:

// Input: "babad" Output: "bab" Note: "aba" is also a valid answer.

// Example: Input: "cbbd" Output: "bb"