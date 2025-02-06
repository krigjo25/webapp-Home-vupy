//  Modals
var html = '';

// Controller
function findEqualNumber()
{
    //  Initialize a counter
    let count = 0;

    //  Initialize random number
    let n = Math.floor(Math.random()* 10); 
    let x = Math.floor(Math.random()* 10);

    //  While n and x is not equal generate random number
    while(n != x)
    {
        
        //  Generate number
        n = Math.floor(Math.random()* 10); 
        x = Math.floor(Math.random()* 10);

        //  Count how many attempts it takes to find equal number
        count ++;
    }

    return count;
}

//  View
function updateView()
{
    //  Fetch ids
   document.getElementById('equality').innerHTML += /*HTML*/`used ${findEqualNumber()} loops to get to be equal`;
   console.log('test')
}
function main()
{
    //  Initializing the html id & table
    let id = document.getElementById('main');

    html = /*HTML*/`
        <section>
            <div id="equality">
                <h3>9.3 While-loop</h3>
                </div>
        </section>`;
        
    id.innerHTML = html;
    updateView();
    

    return;

}


