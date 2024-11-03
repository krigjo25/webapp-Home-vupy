//  View -> Reperesent the visuals
main();
function main()
{
    //  Initialize variables
    let app = model.apps;

    //  Linear algorithme
    for (let i = 0; i < app.length; i++)
    {

        //  Ensure the name is carosel
        if (app[i].app === "carosel")
        {
            app[i].id.innerHTML = /*HTML*/ ` 
                ${carosel(app[i])}`;
        }  
        else if (app[i].app === "bio")
        {
            app[i].id.innerHTML += /*HTML*/ ` 
            ${about(app[i])}`;
        }
    }
}

function about(arg)
{
    console.log(arg);
    arg.id.innerHTML = /*HTML*/`
    <h2>${arg.name}</h2>
    <span class="time">
        written by @krigjo25 , but formulated by 
        Google's Gimini. read time 
        ${arg.time}
        <i class="bi bi-stop-watch"></i>
    </span>
    <div class="grid-container">
        <p class="grid-item">${arg.message}</p>
        <p class="grid-item">${arg.message1}</p>
        <p class="grid-item">${arg.message2}</p>
    </div>`;
}
function carosel(arg)
{
    return  /*HTML*/`
        <img id="car-img" src="${arg.path + arg.source}" alt="${arg.alt}" class="css-img">
            <div class="caption">${arg.caption}</div>
            <div id="img-btn" class="img-btn">
                <button id ="prev-btn" class="prev-btn" onclick="prev()">
                    <i class="bi bi-arrow-left-square-fill"></i>
                </button>
                <button id ="next-btn" class="next-btn"onclick="next()">
                    <i class="bi bi-arrow-right-square-fill"></i>
                </button>
        </div>`;
}


