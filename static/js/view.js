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
        else if (app[i].app === "footer")
        {
            footer(app[i]);
            formValidation();
        }
    }
}

function about(arg)
{
    let html = /*HTML*/`
    <section class="bio-container">
        <h2>Biography</h2>
        <nav class="bio-links">`;

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

            <h2>${arg.title[0]}</h2>
            <small>Written by ${arg.title[0]} average time to read time <b><time data="${arg.time}">${arg.time} min</time></b><i class="bi bi-stopwatch"></i></small>       
            <p>${arg.message}</p>
            <p>${arg.message1}</p>
            <p>${arg.message2}</p>

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
        <h2>Certified Specializations</h2>
        <div class="specialization-container">`;

    for (let i = 0; i < arg.schools.length; i++)
    {
        //  Initializing classes
        let schools = arg.schools[i];

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
    html += /*HTML*/`
        </div>`;

    return html;
}

function footer(arg)
{
    arg.id.innerHTML = /*HTML*/`
    ${contact()}
    ${socialMedia()}
    `;
    //  Footer copy right
    document.querySelector('#powered-by').innerHTML += /*HTML*/`
    <p><a href=""> Copyright</a> &copy; <a href="https://www.krigjo25.no">@krigjo25</a> 2024  - ${new Date().getFullYear()}</p>`;
}

function contact()
{
    return /*HTML*/`
        <section class="contact-container">
                <h2>Get in touch</h2>
                <nav class='ext-bar'>
                    <a href='{{ messenger }}'>                          
                        <i class="bi bi-messenger"></i>
                    </a>
                    <a href='{{ mail }}'>                           
                        <i class="bi bi-mailbox"></i>
                    </a>
                    <a href='{{ discord }}'>                          
                        <i class="bi bi-discord"></i>
                    </a>
                </nav>
        </section>`;
}
function socialMedia()
{
    return /*HTML*/`        
    <section class="social-media-container">
        <h2>Follow me on social media</h2>
        <nav class="ext-bar">
            <a href='{{ facebook }}'>
                <span>                           
                    <i class="bi bi-facebook"></i>
                </span>
            </a>
            <a href='{{ instagram }}'>
                <span>                           
                    <i class="bi bi-instagram"></i>
                </span>
            </a>
            <a href='{{ ello }}'>
                <span>                           
                    <i class="bi bi-ello"></i>
                </span>
            </a>
        </div>
    </section>`;
}