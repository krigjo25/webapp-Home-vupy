//  Initializing the variables | Modals
let nae = "Kristoffer";
let city = "Mysen";
let food = "Chicken";

//  Controlling the change
function setName(arg)
{
    nae = arg;
    setField();
}
//  View
function setField()
{
    document.getElementById("name").innerHTML = nae;
    document.getElementById("city").innerHTML = city;
    document.getElementById("food").innerHTML = food;
}
