//  View -> Reperesent the visuals
main();
function main()
{
    for (let i = 0; i < app.length; i++)
    {
        if (app[i].app.id == apps[0])
        {
            
            app[i].app.innerHTML = /*HTML*/ `
                <img id="car-img" src="${app[i].source}" alt="${app[i].alt}" class="css-img">
                <div class="caption">${app[i].caption}</div>
                <div>
                    <div class="active"></div>
                </div>`;
        }  
    }
    about();
    return;
}

function about()
{
    for (let i = 0; i < bio.length; i++)
    {
        if (bio[i].app.id == apps[1])
        {
            bio[i].app.innerHTML = /*HTML*/`
                <h2>${bio[i].title}</h2>
                <span class="time">written by @krigjo25 , but formulated by Google's Gimini. read time ${bio[i].time}<i class="bi bi-stop-watch"></i></span>
                <div class="grid-container">  
                    <p class="grid-item">${bio[i].msg}</p>
                    <p class="grid-item">${bio[i].msg1}</p>
                    <p class="grid-item">${bio[i].msg2}</p>
                </div>`;
        }
    }
}
