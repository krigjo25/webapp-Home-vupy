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
        if (app[i].app === "carosel-container")
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
        else if (app[i].app === "footer")
        {
            footer(app[i]);
           // formValidation();
        }
    }
}

function about(arg)
{
    let html = /*HTML*/`
        <h2>Biography</h2>
        <nav class="bio-link">`;

    for (let i = 0; i < arg.links.length; i++)
    {
        html += /*HTML*/`
            <button class="bio-btn" onclick='biography("${arg.links[i].name}")'>
                <i class="${arg.links[i].icon}"></i> 
                ${arg.links[i].name}
            </button>`;
    }
    
    html += /*HTML*/`
        </nav>
        <section class="bio-content">

            <h3>${arg.title[0]}</h3>
            <small>Written by ${arg.title[0]} AVG reading time <b><time data="${arg.time}">${arg.time} min</time></b><i class="bi bi-stopwatch"></i></small>       
            <p>${arg.message}</p>
            <p>${arg.message1}</p>
            <p>${arg.message2}</p>

        </section>`;
    
    return html
}

function carosel(arg)
{
    return  /*HTML*/`
        <img id="car-img" src="${arg.path + arg.source}" alt="${arg.alt}">
            <div class="caption">
                <p>${arg.caption}</p>
            </div>
            <div id="img-btn" class="btn-container">
                <button id ="prev-btn" class="img-btn" onclick="prev()">
                    <i class="bi bi-arrow-left-square-fill"></i>
                </button>
                <button id ="next-btn" class="img-btn"onclick="next()">
                    <i class="bi bi-arrow-right-square-fill"></i>
                </button>
        </div>`;
}

function specialization(arg)
{
    let html = "";

    for (let i = 0; i < arg.schools.length; i++)
    {
        //  Initializing classes
        let schools = arg.schools[i];
        console.log(schools);

        html += /*HTML*/`
            <div class="specialization-class">
                <a href="${schools.link}">
                    <h3 class='h3-link'><i class='bi bi-folder-symlink'></i>${schools.school}</h3>
                </a>
                <p>${schools.description}</p>`;

        //  Ensure that the tech is available
        if(schools.tech)
        {
            html += /*HTML*/`
                <div class='tech-container flex-row relative'>`;

            for (let j = 0; j < schools.tech.length; j++)
            {
                html += /*HTML*/`
                    <div class='tech-wrapper'>
                        <div class='tech-${schools.tech[j]} relative'></div>
                        <span class='tech-label'>
                            ${schools.tech[j]}&nbsp;
                        </span>`;

            }
            html += /*HTML*/`
            </div></div>`;
        }

        //  Ensure that the classes are available
        if (schools.classes)
        {
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
                            <h4 class='h4-link'>
                                <i class='bi bi-award'></i>
                                ${classes.name}
                            </h4>
                        </a>`;
                }
                else
                {
                    html += /*HTML*/`
                        <h4 class="h4-link no-select">${classes.name}</h4>`;
                }


                html += /*HTML*/`
                    <p>${classes.description}</p>
                    <div class='tech-container flex-row'>`;

                //  Ensure that the tech is available
                if (classes.tech)
                {
                    for (let k = 0; k < classes.tech.length; k++)
                    {
                        html += /*HTML*/`
                            <div class='tech-wrapper'>
                                <div class='tech-${classes.tech[k]} relative'></div>
                                <span class='tech-label'>
                                    ${String(classes.tech[k]).replace("-", " ")}
                                </span>
                                </div>`;
                    }
                    html += /*HTML*/` 
                    </div></div>`;
                }
                //  Professinal certificates
                else if (classes.languages)
                {
                    for (let k = 0; k < classes.languages.length; k++)
                    {
                        for (let l = 0; l < classes.languages[k].tech.length; l++)
                        {   
                            html += /*HTML*/`
                            <div class='tech-wrapper'>
                                <div class='tech-${classes.languages[k].name} relative'></div>
                                <span class='tech-label'>
                                    ${String(classes.languages[k].tech[l]).replace("-", " ")}
                                </span>
                            </div>`;
                        }
                    }
                    html += /*HTML*/`</div></div>`;
                }
                
            }

        }

        html += /*HTML*/`
        </div>`;   
    }

    return html;
}

function footer(arg)
{
    //  Footer copy right
    document.querySelector('#powered-by').innerHTML = /*HTML*/`
    <p><a href=""> Copyright</a> &copy; <a href="https://www.krigjo25.no">@krigjo25</a> 2024  - ${new Date().getFullYear()}</p>`;
}