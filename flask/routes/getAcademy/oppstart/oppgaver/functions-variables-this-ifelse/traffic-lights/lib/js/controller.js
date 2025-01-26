//  Controller -> Manipulating the design and the modal
const r = document.getElementById("r");
const y = document.getElementById("y");
const g = document.getElementById("g");


function activatelights(arg)
{
    document.getElementById(arg).classList.toggle('active');
    //main();
    timedlights();
    return
}

function timedlights()
{

    for (let i = 0; i < r.classList.length; i++)
    {
        for(light of trafficlights)
        {
            if (r.classList[i] == light)
            {
                r.classList.toggle('active');
            }
        }

        
    }

}