function changeThis(arg)
{
    //  Capslock
    if (arg.innerHTML.toLowerCase() =='capslock')
    {
        capsLock();
    }
}

function capsLock()
{
    //  Initializing document nodes
    let item = document.querySelectorAll('.keyboard-item');

    //  Iterator
    for (let i = 0; i < item.length; i++)
    {
        //  btns iterator
        for (let j = 0; j < item[i].children.length; j++)
        {
            //  Initializing a button element
            let btn =  item[i].children[j];

            // Ensure this button is lowercase
            if (btn.innerHTML == btn.innerHTML.toLowerCase())
            {
               btn.innerHTML = `${btn.innerHTML.toUpperCase()}`;
            }

            // Ensure this is the value we're looking for
            else if (btn.innerHTML == btn.innerHTML.toUpperCase())
            {
                btn.innerHTML = `${btn.innerHTML.toLowerCase()}`;
            } 
        }
    }
}