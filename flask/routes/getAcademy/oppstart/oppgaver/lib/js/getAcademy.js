function removeAll()
{
    // Removes html contents / resets them
    const items = document.querySelectorAll('.item');

    for (item of items)
    {
        //  Removes the innerHTML
        item.innerHTML = '';
    }

    return;
}

function removeStyle()
{
    let styles = document.querySelectorAll('style');

    //  Ensure the style.length is more than 1
    if (styles.length > 1)

    {    
        //  Delete the tags
        for (style of styles)
        {
            style.remove();
        }
    }
    

}

function tools(arg)
{
    removeAll();
    
    arg.children[1].innerHTML = /*HTML*/`
    he most important tools to be used is:
    <ul>
        <li>
            <a href='https://code.visualstudio.com/'>Visual studio Code </a>
            <ul>
                <li>JS Booster</li>
                <li>e6-string-html</li>
                <li>live-Server</li>
                <li>Live-Share</li>
            </ul>
        </li>
        <li>The browser <a href='https://www.google.com/intl/no/chrome/'>Google Chrome</a></li>
    </ul>`;
}

function html(arg)
{
    removeAll();

    arg.children[1].innerHTML = /*HTML*/`
        To define a document we use HTML.
        <ul>
            <li> Fundamental tags for an HTML file.</li>
            <li> Fundamental tags for formating a text</li>
            <ul>
                <li> <code>div</code></li>
                <li> <code>input type='text'</code></li>
                <li> <code>button</code></li>
                <li><a href='https://www.w3schools.com/html/default.asp'>W3School HTML Tutorial</a></li>
                <li><a href='https://www.w3schools.com/tags/default.asp'>W3School HTML References</a></li>
            </ul>
        </ul>`;
}
    
function css(arg)
{
    removeAll();
    arg.children[1].innerHTML = /*HTML*/`
        In a HTML document CSS is used to style the document. Colors, fonts, design etc...
        <ul>
            <li><i> background-color</i></li>
            <li><i>color</i></li>
            <li><i>padding</i></li>
            <li><i>margin</i></li>
            <li><i>border</i></li>
            <li><i>text-align</i></li>
            <li><i>font-size</i></li>
            <li><a href='https://css-tricks.com/snippets/css/a-guide-to-flexbox/'>Flexbox</a></li>
            <li><a href='https://css-tricks.com/snippets/css/complete-guide-grid/'>Grid</a></li>
            <li><a href='https://www.w3schools.com/css/default.asp'>W3Schools CSS Tutorial</a></li>
            <li><a href='https://www.w3schools.com/cssref/default.asp'>W3Schools CSS References</a></li>
        </ul>`;

}
    
function js(arg)
{
    removeAll();
    arg.children[1].innerHTML = /*HTML*/`'
        The most important to learn in Front-end is JavaScript. Through GetAcademy you'll learn the fundemantal programming through manipulation HTML- and CSS on a web page with JavaScript
        <ul>
            <li>There exists a <a href='https://www.w3schools.com/jsref/default.asp'>JavaScript tutorial at W3C</a>, but its recommended to follow this module.
        </ul>`;
}

function structure(arg)
{
    //  Removes html content
    removeAll();

    //  Add html content
    console.log(arg.parentElement);
    let parent = arg.parentElement;
    parent.children[1].innerHTML = /*HTML*/`
    <div>
        <button onclick='prevImg(this)'>◀</button>
        <img src='resources/img/head1.png'>
        <button onclick='nextImg(this)'>▶</button>
    </div>
    <div>
        <button onclick='prevImg(this)'>◀</button>
        <img src='resources/img/body1.png'>
        <button onclick='nextImg(this)'>▶</button>
    </div>
    <div>
        <button onclick='prevImg(this)'>◀</button>
        <img src='resources/img/legs1.png'>
        <button onclick='nextImg(this)'>▶</button>
    </div>`;
    return;
}

function prevImg(arg)
{

    //  Initialize array

    //  Initialize element
    let parent = arg.parentElement.querySelector('img');

    //  Ensure its correct image
    if (parent.src.endsWith('head1.png'))
    {
        parent.alt = 'head4.png';
        parent.src = 'resources/img/head4.png';
    }
    else if (parent.src.endsWith('head4.png'))
    {
        parent.alt = 'head3.png';
        parent.src = 'resources/img/head3.png';
    }
    else if (parent.src.endsWith('head3.png'))
    {
        parent.alt = 'head2.png';
        parent.src = 'resources/img/head2.png';
    }
    else if (parent.src.endsWith('head2.png'))
    {
        parent.alt = 'head1.png';
        parent.src = 'resources/img/head1.png';
    }
    
    //  Ensure the src attribute for body
    if (parent.src.endsWith('body1.png'))
        {
            parent.alt = 'body4.png';
            parent.src = 'resources/img/body4.png';
        }
        else if (parent.src.endsWith('body4.png'))
        {
            parent.alt = 'body3.png';
            parent.src = 'resources/img/body3.png';
        }
        else if (parent.src.endsWith('body3.png'))
        {
            parent.alt = 'body2.png';
            parent.src = 'resources/img/body2.png';
        }
        else if (parent.src.endsWith('body2.png'))
        {
            parent.alt = 'body1.png';
            parent.src = 'resources/img/body1.png';
        }
    //  Ensure the src attribute for legs
    if (parent.src.endsWith('legs1.png'))
        {
            parent.alt = 'legs4.png';
            parent.src = 'resources/img/legs4.png';
        }
        else if (parent.src.endsWith('legs4.png'))
        {
            parent.alt = 'legs3.png';
            parent.src = 'resources/img/legs3.png';
        }
        else if (parent.src.endsWith('legs3.png'))
        {
            parent.alt = 'legs2.png';
            parent.src = 'resources/img/legs2.png';
        }
        else if (parent.src.endsWith('legs2.png'))
        {
            parent.alt = 'legs1.png';
            parent.src = 'resources/img/legs1.png';
        }
        
    return;

}

function nextImg(arg)
{

    //  Initialize element
    let parent = arg.parentElement.querySelector('img');

    //  Ensure its correct image
    if (parent.src.endsWith('head1.png'))
    {
        parent.alt = 'head2.png';
        parent.src = 'resources/img/head2.png';
    }
    else if (parent.src.endsWith('head2.png'))
    {
        parent.alt = 'head3.png';
        parent.src = 'resources/img/head3.png';
    }
    else if (parent.src.endsWith('head3.png'))
    {
        parent.alt = 'head4.png';
        parent.src = 'resources/img/head4.png';
    }
    else if (parent.src.endsWith('head4.png'))
    {
        parent.alt = 'head1.png';
        parent.src = 'resources/img/head1.png';
    }
    
    //  Ensure the src attribute for body
    if (parent.src.endsWith('body1.png'))
        {
            parent.alt = 'body2.png';
            parent.src = 'resources/img/body2.png';
        }
        else if (parent.src.endsWith('body2.png'))
        {
            parent.alt = 'body3.png';
            parent.src = 'resources/img/body3.png';
        }
        else if (parent.src.endsWith('body3.png'))
        {
            parent.alt = 'body4.png';
            parent.src = 'resources/img/body4.png';
        }
        else if (parent.src.endsWith('body4.png'))
        {
            parent.alt = 'body1.png';
            parent.src = 'resources/img/body1.png';
        }
    //  Ensure the src attribute for legs
    if (parent.src.endsWith('legs1.png'))
        {
            parent.alt = 'legs2.png';
            parent.src = 'resources/img/legs2.png';
        }
        else if (parent.src.endsWith('legs2.png'))
        {
            parent.alt = 'legs3.png';
            parent.src = 'resources/img/legs3.png';
        }
        else if (parent.src.endsWith('legs3.png'))
        {
            parent.alt = 'legs4.png';
            parent.src = 'resources/img/legs4.png';
        }
        else if (parent.src.endsWith('legs4.png'))
        {
            parent.alt = 'legs1.png';
            parent.src = 'resources/img/legs1.png';
        }
        
    return;

}

// Styling the classes
function normal()
{
    removeStyle();

    document.querySelector('head').innerHTML += /*HTML*/`
    <style>
        .tools, .html, .css, .js, .structure {
            display: block;
            margin: 1em auto;
            inline-size: 20em;
            border: 1px solid rgba(0,0,0,1);    
        }
    </style>`;
    
    return;
}

function vertical()
{
    removeStyle();

    document.querySelector('head').innerHTML += /*HTML*/`
    <style>
        .tools, .html, .css, .js, .structure {
            display: block;
            margin: 1em auto;
            inline-size: 20em;
            border: 1px solid rgba(0,0,0,1);    

        }
    </style>
    `;

    return;
}

function horizontal()
{

    removeStyle();

    document.querySelector('head').innerHTML += /*HTML*/`
    <style>
        .tools, .html, .css, .js, .structure {
            display: inline-block;
            justify-content: center;
        }

    </style>
    `;

    //  Adding a class .active
    let classes = document.querySelectorAll('.tools.html.css.js.structure ');

    for (cls of classes)
    {
        console.log(cls.children)
    
    }
    return;
}

function grid()
{

    removeStyle();

    document.querySelector('head').innerHTML += /*HTML*/`
    <style>
        .grid-container {
            display: grid;
            margin: 1em;
            inline-size: 100%;
            grid-column-gap: 1em;
            grid-template-rows: 2fr;
            grid-template-columns: 20em 20em; 
        }
        .tools, .html, .css, .js, .structure {
            inline-size: 100%;
            justify-content: center;
        }
    </style>    
    `;

    document.querySelector('main').classList.add('grid-container');
    return;
}

function htmlManipulation(color, height, width, txt)
{
    //  Task 2 :Functions, variables, this and if/else.

    //  manipulate text
    document.querySelector('.fvtie').innerHTML = /* HTML */`
    <div class='fvtie' style="background-color:rgba(${color}); height:${height}em; inline-size:${width}em">
        <p>
        ${txt}
        </p>
    </div>`;
}

function changeBG(arg)
{
    //  Fetch element 
    let element = `.${arg.innerHTML}`
    element = document.querySelector(element);
    
    //  Styles
    element.style.blockSize = "10em";
    element.style.inlineSize = "10em";
    element.style.display = "inline-block";
    element.style.backgroundColor = arg.innerHTML;
}