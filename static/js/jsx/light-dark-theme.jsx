function changeBackground()
{
    // Initializing the variables
    let body = document.querySelector('body');
    let btn = document.querySelector('.toggle-light-dark-theme');


    //  Toggle the theme colour
    

    //  Change button text
    if (body.classList == 'bg-light')
    {
        body.classList.toggle('bg-dark');
        body.classList.toggle('bg-light');
        btn.innerHTML = "Toogle to Dark Theme";
    }
    else
    {
        body.classList.toggle('bg-dark');
        body.classList.toggle('bg-light');
        btn.innerHTML = "Toogle to light theme";
    }
    
    return;
}