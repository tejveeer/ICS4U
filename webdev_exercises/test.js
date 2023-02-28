
const displayBoard = (arr) => {
    // ensure the array is of correct type
    console.assert(
        arr.every(
            subArr => 
                subArr.length === 3 
                && subArr.every(n => typeof n === 'number')
            )
    );

    // print the board
    arr.forEach(subArr => console.log(subArr.join(' ')));
}

const updateBoard = (state, player, [x, y]) => {
    if (!(state[x][y] === 0))
        return false;

    state[x][y] = player;
}

const checkWinner = (state) => {
    const checks = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],

        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],

        [1, 5, 9],
        [3, 5, 7]
    ]

    const getCoordinate = (n) => { 
        if (!(1 <= n <= 9))
            return false;
        return [Math.floor((n - 1) / 3), (n - 1) % 3];
    }

    for (const check in checks) {
        let equivalent = check.map(place => {
            let [x, y] = getCoordinate(place);
            return state[x][y];
        });

        if (equivalent.every(n => n == equivalent[0]) && equivalent[0] !== 0)
            return equivalent[0];
    }
    
    return false;
}

const state = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

updateBoard(state, 'X', [0, 1]);
displayBoard(state);