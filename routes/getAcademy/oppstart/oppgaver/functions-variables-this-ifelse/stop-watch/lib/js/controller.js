
//  Controller -> Manipulating the design and the modal
function count()
{
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
    
        mainView();

    return;
}

function startTimer()
{
    timer = setInterval(count, 10);
    mainView();
    updateButtons();

    return;
}

function intervalTimer()
{

    interval.push(`${hour}:${min}:${sec}:${ms}`);
    return;
}

function pauseTimer()
{
    clearInterval(timer);
    buttonView();
    
    return;
}

function clearTimer()
{
    pauseTimer();
    ms = 0;
    sec = 0;
    hour = 0;

    mainView();
    buttonView();

    return;
}
