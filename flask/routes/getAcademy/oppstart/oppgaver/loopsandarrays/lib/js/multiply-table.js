//  Modals
var html = '';

// Controller 
function multiplication()
{
    //  Initializie variables
    let multiply = (counter, by)=>counter * by;
    let increase = 2;
    html = /*HTML*/`<tr>`;

    //  Table header
    for(let i = 1; i <= 10; i++)
        {
            html +=/*HTML*/`<td>${i}</td>`;
        
        }
    html += /*HTML*/`</tr>`;

    // Rows
    for(let i = 2; i <= 10; i++)
    {
        html +=/*HTML*/`<tr><td>${increase}</td>`;

        //  Columns
        for(let j = 2; j <= 10; j++)
            {
                html +=/*HTML*/`<td>${multiply(j, increase)}</td>`;
            }

            increase ++;
    }

    //  
    html +=/*HTML*/`</tr>`;
    return html;
}

//  View
function updateMain()
{
    html = /*HTML*/`
        <section>
            <div id='multiplication'>
                <h3> 9.1 Multiplication Table</h3>
                <table>`;

    for(let i = 0; i <= 10; i++)
        {
            html += /*HTML*/`<th>x${i}</th>`;
        }
        console.log()
    html += /*HTML*/`<tbody>${multiplication()}</tbody></table></div></section>`;
    return html;
}
function main()
{
    html = updateMain()
    //  Initializing the html id & table
    let id = document.getElementById('main');

    id.innerHTML = html
}