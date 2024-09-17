//  Controller -> Manipulates modal and view
startTimer();
function startTimer()
{
    timer = setInterval(next, 5000);
}

function next()
{
    //  Initializing src attribute
        //  Linear algorithm0
        
    for(let i = 0; i < sources.length; i++)
    {
        //  Ensure the src has the image with-in
        let src = app[0].app.children[0].src;
        if (src.includes(sources[i].src))
        {
            //  Update variables
            app[0].alt = i + 1 > 2 ? sources[0].alt : sources[i+1].alt;
            app[0].caption = i + 1 > 2 ? sources[0].caption : sources[i+1].caption;
            app[0].source = i + 1 > 2 ? app[0].path + sources[0].src : app[0].path + sources[i+1].src;
            
        }
    }

    clearInterval(timer);
    startTimer();
    main();
}

function prev()
{
    //  Initializing src attribute
    let src = app[0].app.children[0].src;
    
    //  Linear algorithme
    for(let i = sources.length - 1; i >= 0; i--)
    {
        //  Ensure the src has the image with-in
        if (src.includes(sources[i].src))
        {
            //  Update object
            app[0].alt = i - 1 >= 0 ? sources[i-1].alt : sources[sources.length -1].alt;
            app[0].caption = i - 1 >= 0 ? sources[i-1].caption : sources[sources.length -1].caption;
            app[0].source = i - 1 >= 0 ? app[0].path + sources[i-1].src : app[0].path + sources[sources.length -1].src;
        }
    }

    clearInterval(timer);
    startTimer();
    main();
}

function journey()
{
    for (let i = 0; i < bio.length; i++)
    {
        bio[i].title = "The Journey So Far";
        bio[i].msg =`
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

        bio[i].msg1 = `
            As a getAcademy student, I am dedicated to continuous learning
            and growth. I am available for part-time work and seeking a
            challenging role where I can apply my academic knowledge and gain
            practical experience under the mentorship of Industry expertise.`;

        bio.msg2 = `
        I'm interested in joining a team that prioritizes continuous learning,
        mentorship, and Agile practices. His ideal career path involves
        progressing to a Senior Data Scientist position within an innovative
        and collaborative environment.`;
    }
    main();
}

function profile()
{

    for (let i = 0; i < bio.length; i++)
    {
        bio[i].title = "Profiles";
        bio[i].msg =/*HTML*/`
        <h2>Professional profile</h2>
            My programming foundation has been solidified through
            numerous projects involving Python, frontend development,
            C, C#, and .NET.

            <h3>Python Projects:</h3>

            <a href="#">
                <div>
                    I've developed web applications using frameworks like
                    Flask and Django.
                </div>
            </a>
            <a href="#">
                <div>
                    Discord projects have provided me with a solid understanding of SQLite and API integration.
                </div>
            <a href="#">
                <div>
                    Data analysis projects have introduced me to the powerful capabilities of NumPy and Pandas.
                </div>
            </a>

            <h3>Frontend Development:</h3>

            <a href="#">
                <div>
                    I have a strong grasp of HTML, CSS, and JavaScript, enabling me to build dynamic and interactive web applications.
                    My experience includes building web applications using the MVC architecture.
                </div>
            </a>
            <h3>Database Management:</h3>

            <a href="">
                <div>
                    I am proficient in SQL and have applied my knowledge to create database-driven 
                    applications such as hospital management and library management systems.
                </div>
            </a>`;

        bio[i].msg1 = /*HTML*/`
            <h2> Personal Profile</h2>
            <p>
                I'm a dedicated problem-solver with a passion for continuous growth and learning.
                I thrive in supportive environments and enjoy helping others succeed. My experience
                caring for my two nephews has instilled in me a strong sense of responsibility and empathy.
            </p>

            <p> 
                With a growth mindset and an internal locus of control, I'm always eager to take on new challenges
                and explore uncharted territory. I'm driven by curiosity and a desire for personal and professional development.
            <p>

            <p>
                My goal is to leverage my problem-solving skills and passion for data to pursue a career as a data scientist.
                I'm excited about the opportunity to contribute to innovative projects and make a meaningful impact.
            <p>
            <p>
                In addition to my professional aspirations, I'm also passionate about philosophy, coding, and playing the
                piano. These interests allow me to balance my analytical mind with creative pursuits.
            </p>`;

        bio.msg2 = /*HTML*/`
            <h2>What work environment do I thrive best in?</h2>
            <p>
            I'm interested in joining a team that prioritizes continuous learning,
                mentorship, and Agile practices. the ideal career path involves
                progressing to a Senior Data Scientist position within an innovative
                and collaborative environment.
            </p>`;
    }
    main();
}

function biography()
{
    for (let i = 0; i < bio.length; i++)
        {
            bio[i].title = "Self Analysis";
            bio[i].msg = `
                Colleagues and peers consistently acknowledge my
                dedication to current projects and my ability to be
                fully present. As a team member, i demonstrates
                empathy and a keen understanding of others, fostering a
                supportive work environment. Known for their positive
                outlook, he is adept at identifying and leveraging
                the strengths of colleagues, making them an invaluable
                asset to the team.`;
    
            bio[i].msg1 = `
                In my spare time, I primarily focus on enhancing my proficiency
                in Python libraries, database management, piano, and philosophy.
                I am dedicated to both improving my weaker areas and further
                developing my existing strengths. To achieve this, I regularly
                leverage a network of developers and online resources.`;
    
            bio.msg2 = `About me`;
        }
    main();
}