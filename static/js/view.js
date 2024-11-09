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
            ${about(app[i])}`;
        }
        else if (app[i].app === "specialization")
        {
            app[i].id.innerHTML = /*HTML*/ ` 
            ${specialization(app[i])}`;
        }
    }
}

function about(arg)
{
    let html = /*HTML*/`
    <article class="bio-container">
        <section class="bio-links">`;

    for (let i = 0; i < arg.links.length; i++)
    {
        html += /*HTML*/`
            <button class="bio-link" onclick='biography("${arg.links[i].name}")'>
                <i class="${arg.links[i].icon}"></i> 
                ${arg.links[i].name}
            </button>`;
    }
    
    html += /*HTML*/`
        </section>
        <section class="bio-content">
            <section>
                <small>Written by ${arg.title[0]} approximal time to read ${arg.time}<i class="bi bi-stopwatch"></small>       
            </section>
            <h2>${arg.title[0]}</h2>
            <p>${arg.message}</p>
            <p>${arg.message1}</p>
            <p>${arg.message2}</p>
        </section>
        </article>`;
    
    return html
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

function specialization(arg)
{
    let html = /*HTML*/`
    <div class="specialization-container">`;

    for (let i = 0; i < arg.classes.length; i++)
    {
        //  Initializing classes
        let classes = arg.classes[i];
        html += /*HTML*/`
            <div class="specialization-class">
                <a href="${classes.link}">
                    <h2>${classes.school}</h2>
                </a>
                <p>${classes.description}</p>
            </div>
            <div class="specialization-courses">`;

            for (let j = 0; j < classes.courses.length; j++)
            {
                //  Initialize courses
                let courses = classes.courses[j];
                html += /*HTML*/`
                <div class="specialization-course">
                    <h3>${courses.name}</h3>
                    <p>${courses.description}</p>
                    <ul>`;
                html += /*HTML*/`
                    </ul>
                </div>`;
            }
    }
    html += /*HTML*/`
            </div>
        </div>`;

    return html;
}
