//  Modal
let colorwheel_bg = document.getElementById('color-wheel-bg');

//  Controller
function changeText()
{
    //  Fetch textarea id, fetch textarea id
    let fvtie = document.getElementById('fvtie');
    let textarea = document.getElementById('body-text');

    //  Ensure the text area is loonger than 0 character
    if (textarea.value.length > 0)
    {
        fvtie.innerHTML = textarea.value;
    }

    textarea.value = '';
    htmlManipulation();
}
function changeColourwheel()
{
    //  Input models
    let bg = document.getElementById("color-bg");
    let font = document.getElementById("color-font");

    //  Colour value
    let colorwheel_bg = document.getElementById("color-wheel-bg");
    let colorwheel_font = document.getElementById("color-wheel-font");

    console.log(colorwheel_font.value)
    colorwheel_bg.value = bg.value
    colorwheel_font.value = font.value

    return;
}
function htmlManipulation()
{
    //  Task 2 :Functions, variables, this and if/else.

    //  Initialize block and inline size
    let l = document.getElementById('length');
    let h = document.getElementById('height');
    let fvtie = document.getElementById('fvtie');

    fvtie.style.inlineSize = l.value + "%";
    fvtie.style.blockSize = h.value + "px";

    //  Background and font colours
    let colorwheel_font = document.getElementById("color-wheel-font");

    //  Styles
    if (!colorwheel_bg.value == '#000000')
    {
        fvtie.style.backgroundColor = "rgb(61, 105, 137)";
    } else {
        fvtie.style.backgroundColor = colorwheel_bg.value;
    }
    if(!colorwheel_font.value || colorwheel_font.value == '#000000')
    {
        fvtie.style.color = "rgb(227, 227, 227)";

    } else {
        fvtie.style.color = colorwheel_font.value;
    }

    return;
}

// View
function main() {

    let main = document.getElementById("main");

    main.innerHTML = /*HTML*/`
        <section>
            <div id="fvtie">
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam tempus maximus rhoncus.
                Phasellus gravida enim ex. Mauris eu aliquet tellus. Nam augue tortor, bibendum eget
                erat sit amet, facilisis lacinia mi. Aenean sollicitudin consequat metus eu elementum.
                Etiam hendrerit volutpat luctus. Donec lacus diam, vestibulum vel ex eget, luctus int-
                erdum justo. Vestibulum sodales semper velit, eget eleifend massa dapibus at. Nullam 
                molestie risus eu imperdiet cursus. Sed vitae enim ac elit volutpat venenatis ut ut n-
                ibh. Phasellus vitae sapien mollis, tincidunt justo vitae, consequat arcu. Donec tinc-
                idunt, sapien a placerat varius, enim neque gravida augue, quis vehicula erat lorem eu
                ex.</p>
            </div>
        </section>
        <section>
        <div class="form-bg-blue-light">
            <form id="color-scheme" action="/index.html">
                <legend> Customize Height and width property</legend>
                <div class="grid-container">
                    <label for="length">length in px</label>
                    
                    <label for="height">Height in px</label>
                    <input id="length" type="int" onchange="htmlManipulation()" placeholder="16">
                    <input id="height" type="int" onchange="htmlManipulation()" placeholder="16" pattern="^[0-9]$">
                </div>
                <legend> Customize the font color and background</legend>
                <div class="grid-container">
                    <label for="color-bg">background color :</label>
                    <label for="color-font">Font color:</label>

                    <input id="color-bg" type="text" onchange="changeColourwheel()" placeholder="#000000">
                    <input id="color-font" type="text" onchange="changeColourwheel()" placeholder="#000000">
                    <input id="color-wheel-bg" type="color">
                    <input id="color-wheel-font" type="color">
                </div>
                <legend> Customize the text !</legend>
                <textarea id="body-text" placeholder="Some text to manipulate"></textarea>
            </form>
            <button class='submit-btn' onclick="changeText()">Change Background</button>
        </div>
        </div>
        </section>`;
}

main();
