//  Modal -> Initializing the data for the view
const p = document.getElementById("p");
const demo = document.getElementById("demo");
const app = document.getElementById("control");


main();
function main()
{
    app.innerHTML = /*HTML*/`

        <form id="color-scheme">
        ${form()}
        ${extform()}
        </form>
        
        <button class='submit-btn' onclick="changeColor()">Change Background</button>`;
}

function form()
{
    return  /*HTML*/`
    <legend> Customize the font color and background</legend>
            
            <div class="grid-container">
                <label for="color-bg">background color :</label>
                <label for="color-font">Font color:</label>
                <input id="bg-color" type="text" onchange="changeColorWheel()" placeholder="#000000">
                <input id="font-color" type="text" onchange="changeColorWheel()" placeholder="#000000">
                <input id="color-wheel-bg" type="color">
                <input id="color-wheel-font" type="color">
            </div>`;
}
function extform()
{
    return /*HTML*/`
        <legend> Customize the text !</legend>
        <textarea id="body-text" placeholder="Some text to manipulate"></textarea>`;
}


//  Controller -> Manipulates the data and view
const style = demo.style;
const bgColor = document.getElementById("bg-color");
const textarea = document.getElementById('body-text');
const fontColor = document.getElementById("font-color");
const colorwheel_bg = document.getElementById("color-wheel-bg");
const colorwheel_font = document.getElementById("color-wheel-font");


function changeText()
{
    //  Ensure the text area is loonger than 0 character
    console.log(textarea.value)
    p.innerHTML = textarea.value ? textarea.value : p.innerHTML;
    return

}

function changeColor()
{
    //  Change background color
    style.color = colorwheel_font.value == '#000000' ? "#fefefe": colorwheel_font.value;
    style.backgroundColor = colorwheel_bg.value == '#000000' ? "rgb(61, 105, 137)": colorwheel_bg.value;
    
    changeText();
    return;
}
function changeColorWheel()
{
    colorwheel_bg.value = bgColor.value != "" ? bgColor.value : "#00000";
    colorwheel_font.value = fontColor.value != "" ? fontColor.value : "#000000";

    return;
}