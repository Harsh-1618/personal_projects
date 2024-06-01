function handleHover(element){
    element.style = "background-color: rgb(2, 190, 156);";
};

function handleUnhover(element){
    element.style = "background-color: rgb(36, 252, 180);";
};

function handleClick(id){
    fetch('/process_id', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ id: id })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            const size = data.data[0];
            const ans_board = data.data[1];
            for (let i = 0; i < size[0]; i++) {
                for (let j = 0; j < size[1]; j++) {
                    let id = i + "_" + j;
                    let cell = document.getElementById(id);
                    cell.innerText =ans_board[i][j];
                }
            }

            if (data.data[2]){
                let h_3 = document.getElementById("statusText");
                h_3.innerText = "Congratulations! You won the game.";
                h_3.innerHTML = "Congratulations! You won the game.";
                h_3.style.display = "block";
                h_3.style.color = "green";
            }

            if (data.data[3]){
                let h_3 = document.getElementById("statusText")
                h_3.innerText = "You lost the game. Better luck next time!";
                h_3.innerHTML = "You lost the game. Better luck next time!";
                h_3.style.display = "block";
                h_3.style.color = "red";
            }
        }
    })
    .catch(error => console.error('Error:', error));
};