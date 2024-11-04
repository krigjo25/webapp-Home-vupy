//  Controller -> Manipulates modal and view
startTimer();
function startTimer()
{
    timer = setInterval(next, 100000);
}

function next()
{
    //  Initializing variables
    let app = model.apps;
    let sources = model.sources;

    //  Linear algorithme
    for (let i = 0; i < app.length; i++)
    {
        //  Ensure the name is carosel
        if (app[i].name == "carosel")
        {
            //  Initialize current image src
            let src = app[i].id.children[0].src;

            for(let j = 0; j < sources.length; j++)
            {
                //  Ensure the path points to the image 
                if (src.includes(sources[j].src))
                {
                    //  Update variables with next media
                    app[i].alt = (j + 1 > sources.length-1) ? sources[0].alt : sources[j+1].alt;
                    app[i].caption = (j + 1 > sources.length-1) ? sources[0].caption : sources[j+1].caption;
                    app[i].source = (j + 1 > sources.length-1) ? sources[0].src : sources[j+1].src;
                }
            }
        }
    }

    clearInterval(timer);
    startTimer();
    main();
}

function prev()
{
    //  Initializing variables
    let app = model.apps;
    let sources = model.sources;

    //  Linear algorithme
   for (let i = 0; i < app.length; i++)
    {
    
       //  Ensure the app is carosel
        if (app[i].name == "carosel")
       {
                
            //  Initialize current image src
            let src = app[i].id.children[0].src;
        
            for(let j = 0; j < sources.length; j++)
            {
                //  Ensure the src points to the image
                if (src.includes(sources[j].src))
                {
                    //  Update variables
                      app[i].alt = (j - 1  < 0) ? sources[sources.length-1].alt : sources[j-1].alt;
                      app[i].caption = (j - 1 < 0) ? sources[sources.length-1].caption : sources[j-1].caption;
                      app[i].source = (j - 1 < 0) ? sources[sources.length-1].src : sources[j-1].src;
                }
            }
        }
    }
    clearInterval(timer);
    startTimer();
    main();
   
    
}

function biography(arg)
{
    console.log(arg);
    //  Initializing the app
    let bio = model.apps;

    for (let i = 0; i < bio.length; i++)
    {
        console.log(bio[i].app);
        if (bio[i].app == "bio")
        {
            console.log(bio[i].name);
            bio[i].name = arg;
            console.log(bio[i].name);

            if (bio[i].name == 'profile')
            {
                toTitleCase(bio[i].title);
                profile(structure);
            }
            else if (bio[i].name == "journey")
                {
                    toTitleCase(arg.title);
                    journey();
                }
        
                else if (bio[i].name == "about")
                {
        
                    
                    bio[i].message = `
                    Colleagues and peers consistently acknowledge my
                    dedication to current projects and my ability to be
                    fully present. As a team member, i demonstrates
                    empathy and a keen understanding of others, fostering a
                    supportive work environment. Known for their positive
                    outlook, he is adept at identifying and leveraging
                    the strengths of colleagues, making them an invaluable
                    asset to the team.`;
        
                bio[i].message1 = `
                    In my spare time, I primarily focus on enhancing my proficiency
                    in Python libraries, database management, piano, and philosophy.
                    I am dedicated to both improving my weaker areas and further
                    developing my existing strengths. To achieve this, I regularly
                    leverage a network of developers and online resources.`;
        
                bio.msg2 = `About me`;
                bio.time = time_calculations(bio[i].message);
                }
                else {
                    return `<h2>${arg.name}</h2>
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
        }
    }
}

function journey(arg)
{

        arg.title = "The Journey So Far";
        arg.msg =`
            My journey into coding began in my teens when I discovered HTML
            and CSS. Joining the SitePoint community fueled my passion for
            web development, and I was introduced to JavaScript. While I
            explored JavaScript, I found my true calling in back-end
            development. I chose to specialize in Python and database
            management, gaining practical experience through Discord projects.
            To further my education, I am currently studying at getAcademy
            and CS50 at Harvard. I am excited to apply my skills to more
            complex projects and continue growing as a developer.
            `;

        arg.msg1 = `
            As a getAcademy student, I am dedicated to continuous learning
            and growth. I am available for part-time work and seeking a
            challenging role where I can apply my academic knowledge and gain
            practical experience under the mentorship of Industry expertise.`;

        arg.msg2 = `
        I'm interested in joining a team that prioritizes continuous learning,
        mentorship, and Agile practices. His ideal career path involves
        progressing to a Senior Data Scientist position within an innovative
        and collaborative environment.`;

    arg.time = time_calculations(arg.message);
    main();
}

function profile(arg)
{
    //arg.title = toTitleCase(arg.title);
    
    arg.message = /*HTML*/`
    
        <h2>Professional profile</h2>
        <h2>Kristoffer Gjøsund</h2>
        <h3>Python & SQL Alchemist</h3> 
        <p>
            My ideal lifestyle involves a balance between the passion 
            of technology and wellness. I dedicate my free time to coding,
            meditation, and physical activity and I am always looking for
            new challenges / adventures.
        </p>
        <p>
            As Developer i prefer to organize my code with comments, 
            to give out a greater understanding of the code which is
            written, I also prefer to organize my code with a
            documentation for a greater understanding of the project.
            My process of development includes a lot of simplicity at
            first, then I optimize the code for a better performance.
            Through my journey as a developer, I have learned that the
            best way to ensure the quality for the code is through test
            frameworks.
        </p>
        
        <h2>Technical Skills:</h2>
            <h3>Python engineering:</h3>
            <h3>Database Management:</h3>
            <h3>Frontend development:</h3>`;

    arg.time = time_calculations(arg.message);
    main();
    
}

function toTitleCase(str) {
   
   /* 
    Adapted from: https://stackoverflow.com/questions/196972/convert-string-to-title-case-with-javascript
   */
    return str.replace(
      /\w\S*/g,
      text => text.charAt(0).toUpperCase() + text.substring(1).toLowerCase()
    );
  }

function time_calculations(arg)
{
    /*AI generated*/
    let words = arg.split(" ");
    let time = Math.round(words.length / 200);
    return time;
}