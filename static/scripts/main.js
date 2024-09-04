
function initiate_reservation(esrog_id){
    fetch(`/initiate-reservation/${esrog_id}`)
    .then(response => response.json())
    .then(data => {
        console.log(data)
        if(data.message == 'this esrog is not reserved yet please enter your name to reserve it'){
            const username = prompt('enter your name in order to reserve this esrog')
            localStorage.setItem('username', username)
            fetch(`/reserve/${esrog_id}/${username}`, {method: 'PUT'})
            .then(response => response.json())
            .then(data => {
                alert(data.message)
            })
        }else{
            notify(data.message)
        }
    })
}


function notify(message){
    const notifications = document.querySelector('.notifications')
    const notification = document.createElement('p')
    notification.textContent = message
    notification.classList.add('notification')
    const closeButton = document.createElement('button')
    closeButton.classList.add('close')
    closeButton.textContent = 'x'
    notification.appendChild(closeButton)
    closeButton.addEventListener('click', () => {
        notification.remove()
    })

    notifications.appendChild(notification)
}