/*
 * Complete the 'getUniqueCharacter' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts STRING s as parameter.
 */

function getUniqueCharacter(s) {
    // Write your code here
    const freqs = new Map();
    
    for (let c of s) {
        freqs.set(c, freqs.get(c) + 1 || 1);
    }
    
    let i = 1;
    for (let c of s) {
        if (freqs.get(c) === 1) return i;
        i++;
    }
    
    return -1;
}

/*
 * Complete the 'chooseFlask' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY requirements
 *  2. INTEGER flaskTypes
 *  3. 2D_INTEGER_ARRAY markings
 */

function chooseFlask(requirements, flaskTypes, markings) {
    // Write your code here
    
    requirements.sort((a,b) => a-b);
    const markings2 = [];
    
    for (let [flask, grade] of markings) {
        if (!markings2[flask]) markings2[flask] = [];
        markings2[flask].push(grade);
    }
    
    let min = Infinity;
    let minFlask = -1;
    let currentSum;
    let flaskGradeI;
    
    for (let i=0; i<markings2.length; i++) {
        currentSum = 0;
        flaskGradeI = markings2[i].length - 1;
        for (let j=requirements.length-1; j>=0; j--) {
            if (requirements[j] > markings2[i][flaskGradeI]) {currentSum = Infinity; break;}
            while (markings2[i][flaskGradeI] && requirements[j] < markings2[i][flaskGradeI]) {
                flaskGradeI--;
            }
            flaskGradeI++;
            currentSum += markings2[i][flaskGradeI] - requirements[j];
        }
        if (currentSum < min) {
            min = currentSum;
            minFlask = i;
        }
    }
    
    return minFlask;
}

/*
 * Complete the 'reachTheEnd' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts following parameters:
 *  1. STRING_ARRAY grid
 *  2. INTEGER maxTime
 */

function reachTheEnd(grid, maxTime) {
    // Write your code here
    let current = {x:0, y:0, time:0, next:null}
    let last = current;
    let visited = new Set();
    visited.add("0,0");
    const dirs = [[1,0], [-1,0], [0,1], [0,-1]];
    
    while (current) {
        const {x, y, time} = current;
        if (x === grid.length-1 && y === grid[0].length-1 && time <= maxTime) return 'Yes';
        for (const [dx, dy] of dirs) {
            const [newX, newY] = [x+dx, y+dy];
            if (newX >= 0 && newY >=0 && newX < grid.length && newY < grid[0].length &&
            grid[newX][newY] === '.' && !visited.has(`${newX},${newY}`)) {
                visited.add(`${newX},${newY}`);
                last.next = {x:newX, y:newY, time:time+1, next:null};
                last = last.next;
            }
        }
        current = current.next;
    }
    
    return "No";

}