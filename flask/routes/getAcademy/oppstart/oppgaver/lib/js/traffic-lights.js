function changeLights(arg)
{ 
    //  Initialize element
    let element = document.querySelector(`.${arg.innerHTML.toLowerCase()}`);

    //  Do this once
    setTimeout(trafficLights(element,`${arg.innerHTML.toLowerCase()}`), 1000);

}

function trafficLights(element, color)
{

    //  Style
    element.style.inlineSize =`10em`;
    element.style.blockSize =`10em`;
    element.style.borderRadius =`10em`;
    element.style.backgroundColor =`${color}`;
    element.style.border =`1px solid ${color}`;
}
//  Timer to change
function lightTimer()
{
    setTimeout(activeRed, 1000)
}



function activeLight(arg, arg1, arg2, arg3, arg4)
{
    //  Initializing the arguments
    arg = document.querySelector(`.${arg}`);
    arg1 = document.querySelector(`.${arg1}`);
    arg2 = document.querySelector(`.${arg2}`);
    arg3 = document.querySelector(`.${arg3}`);

    //  removing active-lights
    arg.classList.toggle('active-light');
    arg1.classList.toggle('active-light');

    arg2.classList.toggle('active-light');
    arg3.classList.toggle('active-light');
}
function activeRed()
{
    activeLight('green', 'orange', 'red', 'red');
    setTimeout(activeRedYellow, 1000);
}

function activeOrange() 
{
    activeLight('red', 'green', 'orange', 'orange');

    return;
}

function activeRedYellow()
{
    activeLight('green', 'orange', 'red', 'red');
    setTimeout(activeGreen, 1000);
}
function activeGreen()
{
    activeLight('red', 'orange', 'green', 'green');
    setTimeout(activeOrange, 2000);
}

