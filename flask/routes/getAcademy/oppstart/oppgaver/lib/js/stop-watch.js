let ms = 0;
let sec = 0;
let min = 0;
let hour = 0;
let timer;

function startTimer()
{

    timer = setInterval(count, 10);
}

function count()
{
    document.querySelector('.timer').innerHTML =`${hour}:${min}:${sec}:${ms}`;
    ms ++;

    if (ms == 100)
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
    document.querySelector('.stop-watch').innerHTML +=`
    <div class="interval">${hour}:${min}:${sec}:${ms}</div>`;
}
function stopTimer()
{
    clearInterval(timer);
    document.querySelector('.stop-watch').innerHTML +=`
    <div class="stop">${hour}:${min}:${sec}:${ms}</div>`;
}