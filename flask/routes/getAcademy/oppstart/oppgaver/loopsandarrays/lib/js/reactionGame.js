//  Modal
var html = "";
let start, end;

var array =[];

function randomizelight()
{
    return Math.floor(Math.random() * 25 );
}

function calculate(start, finish)
{
        // calculates only 
        let sec = (ms) => ms / 1000;
        if (start)
            {return sec(Math.floor(finish - parseInt(start)));}
}


// Controller
function initializeLight()
{
    console.log(start)

    html = "";

    //  Generate a random number
    let random = randomizelight();

    //  Fetch id
    let parent = document.getElementById('section').children;

    //  Toggle elements
    for(let i = 0; i < parent.length; i++)
    {
        //  Ensure the element has the class "on"
        if (parent[i].classList.contains('on'))
        {
            //  toggle
            parent[i].classList.remove('on');
            parent[i].classList.add('off');
            end = new Date().getTime();

            parent[i].removeAttribute('onclick');  // adapted from https://www.w3schools.com/jsref/met_element_removeattribute.asp
        }
    }

    // toggle spesific values to on / off.
    parent[random].classList.remove('off');
    parent[random].classList.add('on');
    parent[random].setAttribute('onclick', "initializeLight()");  // adopted from https://developer.mozilla.org/en-US/docs/Web/API/Element/setAttribute
    
    //  Calculate and print
    updateView2(start, end);
    start = new Date().getTime();
    return;
}

//  View
function updateView2(start, end)
{
    // Initializie an array
    array.push(calculate(start, end));

    html = /*HTML*/ `<section>`;
    for (let i = 1; i < array.length; i++)
        {
            // send feedback for the user
            html += /*HTML*/`
            <div class='time'><p>
            Time used on round ${i} : <time>${array[i]}</time></div>`;
        }

        html += /*HTML*/ `</section>`;

        document.getElementById('rounds').innerHTML = html;

}

function updateView()
{
    for(let i = 0; i < 25; i++)
    {
        
        // onclick element on one of 25
        html += /*HTML*/`<div class="off"></div>`;
    }
    return html;
}

function main()
{

    html = updateView();
    document.getElementById('main').innerHTML += /*HTML*/`
    <section id='section'>${html}</section>
    <section id='rounds'>${html}</section>`;

    // Initializing the game
    start = new Date().getTime();
    initializeLight();
    
}