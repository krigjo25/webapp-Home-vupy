//  Modal -> Initializing the data
const app = document.getElementById('main');
const names = ["r", "g", "b"];


function randomColor()
{
    return Math.floor(Math.random() * 254);
}

//  View -> Represents data

function main()
{
    app.innerHTML = /*HTML*/`
    ${updateMain()}
        <button onclick="changeBG()">changeBG</button>`;

    return
}

function updateMain()
{
    
    let html = "";
    
    //  Print out html
    for (let i = 0; i < names.length; i++)
    {
        html += /*HTML*/`
        <div id="${names[i]}"></div>`;
    }

    return html;
}

//  Controller -> Manipulates the data and/ or view
function changeBG()
{

    for (let i = 0; i < names.length; i++)
        {
            document.getElementById(names[i]).style.backgroundColor = `rgb(${randomColor()},${randomColor()},${randomColor()})`;

        }

    return
}

main();