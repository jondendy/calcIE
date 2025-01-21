function addInput() {
    const inputsDiv = document.getElementById('inputs');
    const inputCount = inputsDiv.getElementsByTagName('input').length;
    if (inputCount < 6) {
        const newInput = document.createElement('input');
        newInput.type = 'number';
        newInput.name = 'value';
        newInput.placeholder = 'Enter a value';
        inputsDiv.appendChild(newInput);
    }
}

document.getElementById('calcForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const values = Array.from(document.getElementsByName('value')).map(input => parseFloat(input.value) || 0);
    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ values })
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('result');
        if (data.result !== undefined) {
            resultDiv.textContent = 'Result: ' + data.result;
        } else if (data.error) {
            resultDiv.textContent = 'Error: ' + data.error;
        }
    });
});
