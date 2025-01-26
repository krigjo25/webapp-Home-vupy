//      Rendering the view of the application

// Importing moudules
import { model } from './model.jsx';
import { Carosel } from './Images.jsx';

App();

function App()
{
    //  Initialize variables
    let app = model.apps;

    //  Linear algorithme
    for (let i = 0; i < app.length; i++)
    {

        //  Ensure the name is carosel
        switch (app[i].app)
        {
            case "carosel-container":
                console.log(app[i]);
                return (
                    <>
                        {Carosel(app[i])}
                    </>
                    );

            case "bio":
                app[i].id.innerHTML = /*HTML*/`
                    ${About(app[i])}`;
                break;

            case "specialization":
                app[i].id.innerHTML = /*HTML*/`
                    ${Specialization(app[i])}`;
                break;

            case "footer":
                Footer();
                break;
        }
    }
}

function About(arg)
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
            <div class='keywords'>
                <h3>{arg.title[0]}</h3>
                <h3>${arg.title}</h3>
                <small class ='abt-author'>Born : 25/02-94 (${arg.age} years old)</small><br></div>
            <small>Written by ${arg.title[0]} AVG reading time <b>${arg.time} min</b><i class="bi bi-stopwatch"></i></small>       
            <p>${arg.message}</p>
            <p>${arg.message1}</p>
            <p>${arg.message2}</p>

        </section>`;
    
    return html
}



function Specialization(arg)
{
    let html = "";

    // Fetch Schools from the model
    for (let i = 0; i < arg.schools.length; i++)
    {
    
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

            //  Fetch tech from the model
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
            //  Fetch classes from the model
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
                    // Fetch tech from the model
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

                if (classes.languages)
                {
                    //  Fetch languages from the model
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

function Footer()
{
    //  Footer copyright
    document.querySelector('#powered-by').innerHTML = /*HTML*/`
        <form action="https://validator.w3.org/check" class="text-center" enctype="multipart/form-data" method="post" target="_blank">
            <input name="doctype" type="hidden" value="HTML5">
            <input name="fragment" type="hidden">
            <input alt="Validate" src="/static/I_heart_validator.png" type="image"> <!-- https://validator.w3.org/ -->
        </form>
        <p>
            <a href="https://choosealicense.com/licenses/gpl-3.0/"> Copyright</a>
            &copy; 
            <a href="https://www.krigjo25.no">@Krigjo25</a> 
            2024  - ${new Date().getFullYear()}</p>`;
}
