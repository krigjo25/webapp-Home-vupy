//  Manipulating the title
function Manipulation() 
{

    let h1 = document.querySelector('h1')
    //  Selects the first occurance of h1 tag
    h1.innerHTML = "Demo Tekst";


    h1.addEventListener('click', function() {
        
        h1.classList.toggle('red');
    });

    return;
}