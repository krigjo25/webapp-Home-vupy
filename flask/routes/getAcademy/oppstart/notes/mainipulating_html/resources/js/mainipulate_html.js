
function clickMe() 
{
    let demo = document.querySelector('demo');

    demo.style.backgroundColor = "red";
    demo.style.color = 'green';
    demo.style.padding = '0.25em';
    demo.classList.add('active');
    demo.classList.remove('old');
    demo.classList.toggle('something');
}