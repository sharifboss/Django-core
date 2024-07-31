const generate = document.getElementById('randomNum');
generate.addEventListener('click', function () {
    const number = parseInt(Math.random() * 10000);
    document.getElementById("inputNum").value = number
    document.getElementById('success').style.display = 'none'
    document.getElementById('fail').style.display = 'none'
})

var buttons = document.getElementsByClassName('btn');
for (let index = 0; index < buttons.length; index++) {
    var button = buttons[index];
    button.addEventListener('click', function (event) {
        var text = event.target.innerText;
        const current = document.getElementById("inputCal").value
        const text1 = current + text;
        document.getElementById("inputCal").value = text1;

    })

}

const submitClick = document.getElementById('submit');
submitClick.addEventListener('click', function () {
    const text1 = document.getElementById('inputNum').value;
    const text2 = document.getElementById('inputCal').value;
    var count = document.getElementById('try').innerText;
    var count1 = parseInt(count);
    console.log(count1);
    if (count > 0) {
        if (text1 == text2) {
            const area = document.getElementById('success');
            area.style.display = 'block';
        }
        else {
            const area = document.getElementById('fail');
            area.style.display = 'block';
            count1--;
            document.getElementById('try').innerText = count1
        }

    }
    else {
        document.getElementById('inputCal').value = ''
        document.getElementById("inputNum").value = ''

    }
})

const undo1 = document.getElementById('undo').addEventListener('click', function () {
    const input = document.getElementById('inputCal').value;
    const array = input.split('');
    array.pop();
    const newtxt = array.join('');
    document.getElementById('inputCal').value = newtxt

})
const clear1 = document.getElementById('clear').addEventListener('click', function () {
    document.getElementById('inputCal').value = ''
})

