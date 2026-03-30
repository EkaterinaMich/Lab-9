function addStep() {
    let dateVal = document.getElementById('date').value
    let stepsVal = document.getElementById('steps').value
    
    fetch('/add', {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            'date': dateVal,
            'steps': stepsVal
        })
    }).then(() => {
        // Перезагружаем страницу, чтобы увидеть новые данные и сумму
        window.location.reload()
    })
}

function clearAll() {
    fetch('/clear', {
        method: 'post'
    }).then(() => {
        // Перезагружаем страницу после очистки
        window.location.reload()
    })
}