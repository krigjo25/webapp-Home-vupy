function HTMLView(color, size, arg)
{
    document.getElementById('return-this'). innerHTML = /*HTML*/ `
    <div id="returned-html" style="${bgColor(color)}${fontSize(size)}${textalign(arg)}">
    Proin semper eros a arcu vulputate volutpat. Nam placerat velit nec
    felis molestie, ac eleifend nulla maximus. Nullam at auctor felis.
    Fusce metus ante, consequat nec porta nec, vehicula vitae purus.
    Etiam ut egestas lorem. Duis eget viverra massa. Donec ac nisl id
    risus cursus ultricies non vel felis. Nulla rutrum consectetur faucibus.
    Donec viverra, elit sed vestibulum euismod, nulla magna feugiat orci, nec
    ultrices libero purus non lectus.
    </div>`
    return;
}

function bgColor(color)
{
    return `background-color:${color};`;
}
function fontSize(size)
{
    return `font-size:${size}vh;`;
}
function textalign(arg)
{
    return `text-align:${arg};`;
}