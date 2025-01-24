//  View -> Represents the design
mainView();
function mainView()
{
    app.innerHTML = /*HTML*/`
    <div id="stop-watch">
        <div id="timer" class="timer">
            ${hour}:${min}:${sec}:${ms}
        </div>
        <div id="interval-timer" class = "interval-timer">
            ${intervalView()} 
        </div>
    </div>`;

    return;
}

function intervalView()
{
    html = `<ol>`;

    for(let i = 0; i < interval.length; i++)
    {
        html += `<li>${interval[i]}</li>`;
    }

    html += `</ol>`;
    return html;
}


buttonView();
function buttonView()
{
    btn.innerHTML = /*HTML*/`
        <div id="btn-icon">
            <button class="play" onclick="startTimer()">
                <i class="bi bi-play-fill"></i>
            </button>

        </div>`;
    return /*HTML*/`<div id="timer-icon"></div>
    `;
}

function updateButtons()
{
    btn.innerHTML = /* HTML */`
    <button onclick="pauseTimer()"><i class="bi bi-pause-circle-fill"></i></button>
    <button onclick="intervalTimer()"><i class="bi bi-plus-circle-fill"></i></button>        
    <button onclick="clearTimer()"><i class="bi bi-square-fill"></i></button>`;
}