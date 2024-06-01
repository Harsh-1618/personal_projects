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
                if ((data.data[4] > 2) && (size[0] > 9) && (size[1] > 9)){
                    let h_3 = document.getElementById("statusText");
                    h_3.innerText = "Congratulations! You won the game. As promised, here is your special reward 😊";
                    h_3.style.display = "block";
                    h_3.style.color = "green";
                    let img = document.getElementById("image")
                    img.src = "https://images.pexels.com/photos/12226270/pexels-photo-12226270.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2";
                    img.style.display = "block";
                }
                else{
                    let h_3 = document.getElementById("statusText");
                    h_3.innerText = "Congratulations! You won the game.";
                    h_3.style.display = "block";
                    h_3.style.color = "green";
                }
            }

            if (data.data[3]){
                let h_3 = document.getElementById("statusText")
                h_3.innerText = "You lost the game DUMBO. Don't worry, it happens with low IQ people 😌";
                h_3.style.display = "block";
                h_3.style.color = "red";
            }
        }
    })
    .catch(error => console.error('Error:', error));
};