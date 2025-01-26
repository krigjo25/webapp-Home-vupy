/// Modal
let html = "";

/// Controller
function activateRed()
{
    trafficLights(activateYellow(), 'red', 'grey', 'grey');
}
function activateYellow()
{
    trafficLights(activateGreen(), 'grey', 'yellow', 'grey');

}

function activateGreen()
{
    trafficLights(activateRed(), 'grey', 'grey', 'green');
}


/// View
function trafficLights(arg, arg1, arg2, arg3) 
{
    console.log('test')
    html = document.getElementById('app').innerHTML = /*HTML*/`
    <div id="traffic-light" onclick="${trafficLights(arg, arg1, arg2, arg3)} ">
        ${activatelight(arg1)}
        ${activatelight(arg2)}
        ${activatelight(arg3)}
    </div>`;

    return html;
}

function activatelight(color){return /*HTML*/`<div class="light ${color}"></div>`}