//  Controller -> Manipulation of view
function answer(x, n, y)
{
    //  Ensure the answer is correct
    if (n == '>')
    {
        if (x > y){points++;}
    } 

    else if (n == "<")
    { 
        if (x > y){points++;}
    }
    else if (n == "=")
    {
        if (x === y){points++;}

    }

    main();
    return;
}