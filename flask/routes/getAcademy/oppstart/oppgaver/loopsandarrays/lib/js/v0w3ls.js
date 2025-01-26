var html = "";

function countVowels(arg)
{
    //  Array Approach
    let vowels = [  'a', 'e', 'i', 'o', 'y', 'u', 'æ', 'ø', 'å']

    let string = arg.toLowerCase();

    //  Initial arguments
    let count = 0;

    //  Find vowel array approach
    for (item of vowels)
    {
        for (let i = 0; i < string.length; i++)
        {
            if (item == string[i])
            {
                count++
            }
        }
    }

    /*for (let i = 0; i <= arg.length; i++){

        //  Ensure the value contains -> a vowel
        if (arg[i] == "a")
        {
            count++;
        }
        else if (arg[i] == "e")
        {
            count++;
        }
        else if (arg[i] == "i")
        {
            count++;
        }
        else if (arg[i] == "o")
        {
            count++;
        }
        else if (arg[i] == "u")
        {
            count++;
        }
        else if (arg[i] == "y")
        {
            count++;
        }
        else if (arg[i] == "æ")
        {
            count++;
        }
        else if (arg[i] == "ø")
        {
            count++;
        }
        else if (arg[i] == "å")
        {
            count++;
        }
    }*/
    
    let html = /*HTML*/`
        Original text : <b>${arg}</b><br>
        Counting V0w3ls : ${count}`;

    return document.getElementById('v0w3ls').innerHTML += html;
}

//  View
function main()
{

    //  Initializing the html id & table
    let id = document.getElementById('main');

    html = /*HTML*/`
        <section>
            <div id="v0w3ls">
                <h3> 9.2 V0w3ls</h3>
                Counting vowels :
                    <input type=text, onchange="countVowels(this.value)">
            </div>
        </section>
`;
    id.innerHTML = html;
    return;

}