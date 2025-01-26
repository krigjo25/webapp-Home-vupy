// Views -> Represents the modal
function main()
{
    //  Initializing randomized integers
    let r1 = random(10);
    let r2 = random(10);

    //  Print it on screen
    app.innerHTML=/*HTML*/`
            <p>
                <b>${r1}</b>
                <input id="user-input" class="ui" type="text" onchange="answer('${r1}', this.value, '${r2}')">
                <b>${r2}</b>
            </p>
        <div id="points">
            Current Points: ${points}
        </div>`;
    return;
}