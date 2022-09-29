/*
 * Complete the 'updateTimes' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY signalOne
 *  2. INTEGER_ARRAY signalTwo
 */

function updateTimes(signalOne, signalTwo) {
    // Write your code here
    let max = -1;
    let updates = 0;
    
    for (let i=0; i<signalOne.length; i++) {
        if (signalOne[i] === signalTwo[i] && signalOne[i] > max) {
            updates++;
            max = signalOne[i];
        }
    }
    
    return updates;
}

/*
 * Complete the 'strokesRequired' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts STRING_ARRAY picture as parameter.
 */

function strokesRequired(picture) {
    // Write your code here
    const visited = new Set();
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    let count = 0;
    
    for (let r = 0; r<picture.length; r++) {
        for (let c = 0; c<picture[0].length; c++) {
            if (visited.has(`${r},${c}`)) continue;
            
            const char = picture[r][c];
            const stack = [[r,c]];
            visited.add(`${r},${c}`);
            while (stack.length) {
                const [cR, cC] = stack.pop(); //current row & col
                for (const [dR, dC] of dirs) { //delta row & col
                    const [nR, nC] = [cR + dR, cC + dC]; //new row & col
                    
                    if (nR < 0 || nC < 0 || nR >= picture.length || nC >= picture[0].length ||
                    visited.has(`${nR},${nC}`) ||
                    picture[nR][nC] !== char) continue;
                    
                    visited.add(`${nR},${nC}`);
                    stack.push([nR,nC]);
                }
            }
            count++;
        }
    }
    return count;
}
2