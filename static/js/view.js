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
    <section class="bio-container">
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
                <small>Written by ${arg.title[0]} average time to read time <b>${arg.time} min</b><i class="bi bi-stopwatch"></i></small>       
            </section>
            <h2>${arg.title[0]}</h2>
            <p>${arg.message}</p>
            <p>${arg.message1}</p>
            <p>${arg.message2}</p>
        </section>
        </section>`;
    
    return html
}

function carosel(arg)
{
    return  /*HTML*/`
        <img id="car-img" src="${arg.path + arg.source}" alt="${arg.alt}" class="css-img">
            <div class="blur">${arg.caption}</div>
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

    for (let i = 0; i < arg.schools.length; i++)
    {
        //  Initializing classes
        let schools = arg.schools[i];
        html += /*HTML*/`
            <div class="specialization-class">
                <a href="${schools.link}">
                    <h2>${schools.school}</h2>
                </a>
                <p>${schools.description}</p>`;
            

            for (let j = 0; j < schools.classes.length; j++)
            {
                //  Initialize courses
                let classes = schools.classes[j];
                html += /*HTML*/`
                <div class="specialization-course">`;

                //  Ensure that the diploma is available
                if (classes.diploma)
                    {
                        html += /*HTML*/`
                        <a href="${classes.diploma}">
                        <h3>${classes.name}</h3>
                        </a>`;
                    }
                    else
                    {
                        html += /*HTML*/`
                        <h3>${classes.name}</h3>`;
                    }

                    
                html += /*HTML*/`
                    <p>${classes.description}</p>
                    <ul>`;
                html += /*HTML*/`
                    </ul>
                </div>
                `;
            }
            html += /*HTML*/`</div>`;
            
    }
    html += /*HTML*/`

            </div>
        </div>`;

    return html;
}
