//  Initializing a Switch
let Switch = 0

function lightBlob() {
    
    //  Initializing ids
    let id = document.getElementById('light-blob');
    let btn = document.getElementById('light-switch');

    // Ensure that Switch is off
    if (Switch == 0)
    {
        Switch ++;
        id.classList.toggle('on');
        id.classList.toggle('off');
        btn.innerHTML = 'Turn off';
  
    } else
    {
        Switch = 0;
        btn.innerHTML = 'Turn on';
        id.classList.toggle('on');
        id.classList.toggle('off');
    }
}