/*
 * Complete the 'toolchanger' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. STRING_ARRAY tools
 *  2. INTEGER startIndex
 *  3. STRING target
 */

function toolchanger(tools, startIndex, target) {
    // Write your code here
    for (let i=0; i<tools.length; i++) {
        if (tools[(startIndex + i) % tools.length] === target || tools[(tools.length + startIndex - i) % tools.length] === target) return i;
    }
}


/*
 * Complete the 'minimumMoves' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY arr1
 *  2. INTEGER_ARRAY arr2
 */

function minimumMoves(arr1, arr2) {
    // Write your code here
    let sum = 0;
    for (let i=0; i<arr1.length; i++) {
        const digits1 = arr1[i].toString().split('');
        const digits2 = arr2[i].toString().split('');
        
        for (let j=0; j<digits1.length; j++) {
            sum += Math.abs(digits1[j] - digits2[j]);
        }
    }
    
    return sum;
}

/*
 * Complete the 'minMoves' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER startRow
 *  3. INTEGER startCol
 *  4. INTEGER endRow
 *  5. INTEGER endCol
 */

function minMoves(n, startRow, startCol, endRow, endCol) {
    // Write your code here
    const visited = new Set();
    visited.add(startRow+','+startCol);
    
    const DIRS = [
        [1,2], [1, -2],
        [-1, 2], [-1, -2],
        [2, 1], [2, -1],
        [-2, 1], [-2, -1]
    ]
    
    let current = {x: startRow, y:startCol, steps: 0, next: null};
    let queueLast = current;
    
    while (current) {
        const {x, y, steps} = current;
        if (x === endRow && y === endCol) return steps;
        
        for (const [dx, dy] of DIRS) {
            let [newX, newY] = [x + dx, y + dy];
            if (newX >= 0 && newY >= 0 && newX < n && newY < n &&
            !visited.has(newX + ',' + newY)) {
                queueLast.next = {x: newX, y: newY, steps: steps + 1, next: null};
                queueLast = queueLast.next;
                visited.add(newX + ',' + newY);
            }
        }
        
        current = current.next;
    }
    
    return -1;
    

}4