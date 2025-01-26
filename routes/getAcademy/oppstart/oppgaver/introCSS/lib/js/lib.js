function removeBlocks()
{
    // Fetch every ids remove then remove the blocks
    let js = document.getElementById('js-container');
    let css = document.getElementById('css-container');
    let html = document.getElementById('html-container');
    let tools = document.getElementById('tools-container');
    let structure = document.getElementById('structure-container');

    //  Remove the HTML inside
    css.innerHTML = /*HTML*/`<h2>CSS</h2>`; 
    html.innerHTML = /*HTML*/`<h2>HTML</h2>`;
    tools.innerHTML = /*HTML*/`<h2>Tools</h2>`;
    js.innerHTML = /*HTML*/`<h2>JavaScript</h2>`;
    structure.innerHTML = /*HTML*/`<h2>Structure</h2>`;

    return;
}

function tools()
{
    //  Call a function to remove Blocks
    removeBlocks();

    //  Initializie the id to arg
    let arg = document.getElementById('tools-container');

    //  Add html
    arg.innerHTML += /*HTML*/`
    <div class="tools-item">
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
        </ul>
    </div>`;
}

function html()
{
    //  Call a function to remove Blocks
    removeBlocks();

    //  Initializie the id to arg
    let arg = document.getElementById('html-container');

    //  Add html
    arg.innerHTML += /*HTML*/`
    <div class="html-item">
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
            </ul>
        </div>`;
}
    
function css()
{
    //  Call a function to remove Blocks
    removeBlocks();

    //  Initializie the id to arg
    let arg = document.getElementById('css-container');

    //  Add html
    arg.innerHTML += /*HTML*/`
        <div class="css-item">
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
            </ul>
        </div>`;

}
    
function js()
{
    //  Call a function to remove Blocks
    removeBlocks();

    //  Initializie the id to arg
    let arg = document.getElementById('js-container');

    //  Add html
    arg.innerHTML += /*HTML*/`'
        <div class="js-item">
            The most important to learn in Front-end is JavaScript. Through GetAcademy you'll learn the fundemantal programming through manipulation HTML- and CSS on a web page with JavaScript
            <ul>
                <li>There exists a <a href='https://www.w3schools.com/jsref/default.asp'>JavaScript tutorial at W3C</a>, but its recommended to follow this module.
            </ul>
        </div>`;
        return;
}

function structure()
{
    //  Call a function to remove blocks
    removeBlocks();

    //  Add html
    document.getElementById('structure-container').innerHTML += /*HTML*/`
    <div class="structure-item">
        <div>
            <button onclick='prev()'>◀</button>
            <img id="structure-head" src='lib/img/head1.png'>
            <button onclick='nextImg()'>▶</button>
        </div>
        <div>
            <button onclick='prevImg()'>◀</button>
            <img id="structure-body"src='lib/img/body1.png'>
            <button onclick='nextImg()'>▶</button>
        </div>
        <div>
            <button onclick='prevImg()'>◀</button>
            <img id="structure-legs" src='lib/img/legs1.png'>
            <button onclick='nextImg()'>▶</button>
        </div>
    </div>`;
    return;
}

function prev()
{
    
    return;

}

function nextImg()
{

    return;

}

// Styling the classes
function removeStyle()
{
    document.getElementById('container').classList.remove('grid');
    document.getElementById('container').classList.remove('normal');
    document.getElementById('container').classList.remove('vertical');
    document.getElementById('container').classList.remove('horizontal');
    

}

function normal()
{
    removeStyle();
    document.getElementById('container').classList.toggle('normal');
    
    return;
}

function vertical()
{
    removeStyle();
    document.getElementById('container').classList.toggle('vertical');

    return;
}

function horizontal()
{

    removeStyle();
    document.getElementById('container').classList.toggle('horizontal');
    return;
}

function grid()
{

    removeStyle();
    document.getElementById('container').classList.toggle('grid-container');
    return;
}
