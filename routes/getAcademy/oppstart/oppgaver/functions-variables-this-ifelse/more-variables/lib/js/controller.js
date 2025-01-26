//  Controller -> Manipulates the data and view
function changeBG()
{
    // 
    for (let i = 0; i < names.length; i++)
        {
            document.getElementById(names[i]).style.backgroundColor = `rgb(${randomColor()},${randomColor()},${randomColor()})`;
        
        }

    return
}