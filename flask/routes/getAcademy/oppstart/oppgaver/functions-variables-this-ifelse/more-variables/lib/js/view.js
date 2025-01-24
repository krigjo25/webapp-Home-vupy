//  View -> Represents data
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

function main()
{
    app.innerHTML = /*HTML*/`
        <h2> Assignment 4: Functions, Variables, This And If/Else</h2>
    ${updateMain()}
        <button onclick="changeBG()">changeBG</button>`;

    return
}
main();