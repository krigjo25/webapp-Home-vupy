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
            app[i].id.innerHTML = /*HTML*/ ` 
            ${about(app[i])}
            ${biography(app[i])}`;
        }
    }
}

function about(arg)
{
    let html = /*HTML*/`
    <div class="bio-container">
        <div class="bio-links">`;

    for (let i = 0; i < arg.links.length; i++)
    {
        html += /*HTML*/`
            <button class="bio-link" onclick='biography(event, "${arg.links[i].name}"')>
                <i class="${arg.links[i].icon}"></i> 
                ${arg.links[i].name}
            </button>`;
    }
    
    html += /*HTML*/`
        </div>`;
    return html
}

function biography(arg)
{
    return /*HTML*/`
    <div class="bio-container">
    <div class="bio-links">
    </div>
</div>

<h2>${arg.name}</h2>
<span class="time">
    written by @krigjo25 , but formulated using
    Artifical Intelligence read time  ${arg.time} minutes
    <i class="bi bi-stop-watch"></i>
</span>
<div class="grid-container">
    <div class="grid-item">
        <h3>${arg.title}</h3>
        <p>${arg.message}</p>
    </div>
    <div class="grid-item">
        <h3>${arg.title}</h3>
        <p>${arg.message1}</p>
    </div>
    <div class="grid-item">
        <h3>${arg.title}</h3>
        <p>${arg.message2}</p>
    </div>
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


