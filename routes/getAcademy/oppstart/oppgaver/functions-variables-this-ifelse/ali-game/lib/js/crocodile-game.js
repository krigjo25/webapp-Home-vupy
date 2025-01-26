let points = 0;

//  Function to generate a random integer
function generateRandomIntenger()
{
    //  Return random number
    return Math.floor(Math.random() *10);
}
function main()
{

    // Initialize Two random numbers
    let r1 = generateRandomIntenger();
    let r2 = generateRandomIntenger();

    //  Print it on screen
    app.innerHTML=/*HTML*/`
    <p><b>${r1}</b> <input type="text" onchange="submit('${r1}', this.value, '${r2}')"> <b>${r2}</b></p>
    <button onclick="main()">Continue</button>`;

    //  return the result to the user and give the user a point
    return
}

function submit(arg, arg1, arg2)
{

    //  Ensure its greater than
    if (arg > arg2)
    {
        //  Ensure input is greater than
        if (arg1 == ">")
        {
            //  Bool true
            bool = true;
        }
    }

    else if (arg < arg2)
        {
            //  Ensure input is greater than
            if (arg1 == "<")
            {
                //  Bool true
                bool = true;
            }
        }
        //  Otherwise its equal
        else
        {
            //  Ensure input is equal
            if (arg1 == "=")
                {
                    //  Bool true
                    bool = true;
                }
        }
    //  Ensure the variable is true
    if(bool)
    {
        //  Update points
        point();
    }
    main()
    return;
}
function point()
{
    //  Notify the user guessed correctly
    document.getElementById('game-message').innerHTML =/*HTML*/`
        Congratulation you guessed correctly!
        Your score has been increased by 1 !`;
    points ++;
    return document.getElementById('points').innerHTML=/*HTML*/`Current points : ${points}`;
}