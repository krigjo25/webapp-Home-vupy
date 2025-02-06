//  Modals
var html = '';

// Controller 
function bagofitems()
{
    //  Initializing a bag with elements
    let bag = ['Hat', 'Pencil', 'Dinosaur', 'Showercap', 'Piece of Tape'];

    // add item to html
    for (let i = 0; i < bag.length; i++)
    {
        html += /*HTML*/`
            <li>${bag[i]} is at pocket ${i}</li>`;
    }

    return html;
}
function updateMain()
{
    document.getElementById('bag-item').innerHTML += /*HTML*/` <div><ul>${bagofitems()}</ul></div>`;
}

//  View
function main()
{


    html = /*HTML*/`

        <section>
        <div id="bag-item">
            <h3>9.4.1 Arrays and forloops </h3>
        </div>
        </section>
`;
    //  Initializing the html id & table
    document.getElementById('main').innerHTML = html;
    updateMain();

    return;

}
