//  Modal -> Initializing data
let ms = 0;
let sec = 0;
let min = 0;
let hour = 0;

const app = getElementById("stop-watch");


//  View -> Represents the design
function mainView()
{
    app.innerHTML = /* HTML */
    `
    <div id="timer">00:00:00:00</div>
        <button onclick="startTimer()">start</button>
        <button onclick="intervalTimer()">Interval</button>
        <button onclick="stopTimer()">stop</button>
    `;
    setInterval(count, 1);
}
main();

//  Controller -> Manipulating the design and the modal
function count()
{
    document.getElementById('timer').innerHTML =/*HTML*/`${hour}:${min}:${sec}:${ms}`;

    ms ++;
    
    if (ms == 1000)
    {
        sec ++;
        ms = 0;
    }
    else if (sec == 60)
        {
            min++;
            sec = 0;
        }
    else if (min == 60)
        {
            hour++;
            min = 0;
        }
    
}

function intervalTimer()
{
    document.getElementById('stop-watch').innerHTML +=`
    <p>${hour}:${min}:${sec}:${ms}</p>`;
}
function stopTimer()
{
    clearInterval(timer);
    document.getElementById('stop-watch').innerHTML +=`
    <div class="stop">${hour}:${min}:${sec}:${ms}</div>`;
}