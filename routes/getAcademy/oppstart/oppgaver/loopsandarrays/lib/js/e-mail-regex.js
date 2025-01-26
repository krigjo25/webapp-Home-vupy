//  Modals
var html = '';


function emailRegex(arg)
{
    let email = false;

    for (let i = 0; i < arg.length; i++)
    {
        if (arg.charAt(i) == " ")
            {
                email = false
                break;
            }
        if (arg.charAt(i) == "@" && arg.charAt(i+1) == ".")
        {
                email = true
        }

        console.log(email)

        //  Logical expression
        console.log(email)
    }

    if(email)
    {
        //  Output a message 
        document.getElementById('msg').innerHTML = /*HTML*/`Successfully the email was registered !`;
    }
    else 
    {
        //  Output a message 
        document.getElementById('msg').innerHTML = /*HTML*/`Something terrible happend!`;
    }    
    
}

//  View
function main()
{
    //  Initializing the html id & table
    let id = document.getElementById('main');
    let section = (arg) => /*HTML*/ `<section><div id="${arg}"></div></section>`;

    html = /*HTML*/`
        <section>
            <div id="regex">
                <h3>9.4.4 Regular expression </h3>
                <div id='msg'></div>
                <input  name ='e-mail' type="text" onchange="emailRegex(this.value)">
            </div>
    </section>`;
    id.innerHTML = html;
    findEqualNumber();
    bagofitems();

    return;

}


