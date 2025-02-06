//  Modal
let html = "";
let animals = ["Esel", "Hund", "Katt"];


// Controller

function generateRandomAnimal()
{
    //  Returning random item from the list
    return animals[Math.floor(Math.random()* animals.length - 1)]
}

function generateAnimal()
{
    //  Fetch Animal
    let animal = document.getElementById('valgt-dyr').value;

    for (let i = 0; i < animal.length; i++)
    {
        if(animal == animal[i])
            
        {
            html = /*HTML*/`
        <div>${animal[i]}</div>`;
        }
    }
}

//  View
function main()
{
    let animal = document.getElementById('main');

    html = /*HTML*/`<div id="selected-animal"></div>`;

    animal.innerHTML = html;
}

main();