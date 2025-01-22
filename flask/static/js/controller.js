function startTimer() {
  // Initializing the timer
  timer = setInterval(next, 100000);
}
function next() {
  //  Initializing variables
  let app = model.apps;
  let sources = model.sources;

  // Swap through the apps
  for (let i = 0; i < app.length; i++) {
    //  Ensure the name is carosel
    if (app[i].name == "carosel-container") {
      //  Initialize current image src
      let src = app[i].id.children[0].src;

      // Swap sources
      for (let j = 0; j < sources.length; j++) {
        //  Ensure the path points to the image 
        if (src.includes(sources[j].src)) {
          //  Update variables with next media
          app[i].alt = j + 1 > sources.length - 1 ? sources[0].alt : sources[j + 1].alt;
          app[i].caption = j + 1 > sources.length - 1 ? sources[0].caption : sources[j + 1].caption;
          app[i].source = j + 1 > sources.length - 1 ? sources[0].src : sources[j + 1].src;
        }
      }
    }
  }
  clearInterval(timer);
  startTimer();
  main();
}
function prev() {
  //  Initializing variables
  let app = model.apps;
  let sources = model.sources;

  // Iterate through the apps
  for (let i = 0; i < app.length; i++) {
    //  Ensure the app is carosel
    if (app[i].name == "carosel-container") {
      //  Initialize current image src
      let src = app[i].id.children[0].src;

      //  Swap sources
      for (let j = 0; j < sources.length; j++) {
        //  Ensure the src points to the image
        if (src.includes(sources[j].src)) {
          //  Update variables
          app[i].alt = j - 1 < 0 ? sources[sources.length - 1].alt : sources[j - 1].alt;
          app[i].caption = j - 1 < 0 ? sources[sources.length - 1].caption : sources[j - 1].caption;
          app[i].source = j - 1 < 0 ? sources[sources.length - 1].src : sources[j - 1].src;
        }
      }
    }
  }
  clearInterval(timer);
  startTimer();
  main();
}
function biography(arg) {
  //  Initializing the app
  let bio = model.apps;

  // Iterating through the bio structure
  for (let i = 0; i < bio.length; i++) {
    // Ensure the app is bio
    if (bio[i].app == "bio") {
      bio[i].name = arg;
      calculateDate(bio[i].birthdate);
      switch (bio[i].name.replace(" ", "").toLowerCase()) {
        case 'profile':
          profile(bio[i]);
          break;
        case 'journey':
          journey(bio[i]);
          break;
        case 'commonopinions':
          common_opinions(bio[i]);
          break;
        default:
          break;
      }
    }
  }
}
function time_calculations(arg) {
  // Calculate the time to read the text
  return Math.round(arg.split(" ").length / 200);
}
function calculateDate(arg) {
  // Initializing a year
  const n = 1000 * 60 * 60 * 24;

  //  Initializing the date
  let today = new Date();
  let birthdate = new Date(arg);

  //  Calculating the difference
  let diff = today - birthdate;

  //  Calculating the difference
  diff = Math.round(diff / n);
  if (today.getMonth() < birthdate.getMonth() && today.getDay() < birthdate.getDay()) {
    return Math.round(diff / 365 - 1);
  }
  return Math.floor(diff / 365);
}
function journey(arg) {
  arg.title[1] = "The Journey So Far";
  arg.message = `
        The journey into coding began in my teens when I discovered HTML
        and CSS. Joining the SitePoint community fueled the passion for
        software engineering, after a while and I was introduced to JavaScript. While I
        explored JavaScript, I found an amazing calling in back-end
        development.I chose to specialize in Python and database
        management, gaining practical experience through Discord projects.
        While prosuing the passion of programming I went to Get Academy vocational school
        To persue more complex understanding of fullstack development while doing classes at 
        Harvard University's CS50.I am excited to apply my skills to more
        complex projects and continue growing as a developer.`;
  arg.message1 = `
        As a Get Academy student, I am dedicated to continuous learning
        and growth. I am available for part-time work and seeking a
        challenging role where I can apply my academic knowledge and gain
        practical experience under the mentorship of Industry expertise.`;
  arg.message2 = `
        I'm interested in joining a team that prioritizes continuous learning,
        mentorship, and Agile practices. the ideal career path involves
        progressing to a Senior Data Scientist position within an innovative
        and collaborative environment.`;
  arg.age = calculateDate(arg.birthdate);
  arg.time = time_calculations(arg.message + arg.message1 + arg.message2);
  main();
}
function profile(arg) {
  arg.message = `
            The ideal lifestyle involves a balance between the passion 
            of technology and wellness. The free time is dedicated to Software developing,
            meditation, and physical activity and always on the outlook for a
            new challenge / adventure.`;
  arg.message1 = ` 
        As an Application engineer
        
        Organization is key to my work, and I am dedicated to delivering
        high-quality code that is easy to read and maintain. I am passionate
        about creating software that is user-friendly and efficient. My
        experience in software development has taught me the importance of
        writing clean code that is easy to understand and maintain. I am
        dedicated to delivering high-quality software that meets the needs.
        of my clients and users. 
    
        software is organized with comments,
        to give out a greater understanding of the develoment which is
            written, The projects are also organized  with a documentation.
            for a greater understanding of the project.
            The process of development includes a lot of simplicity at
            first, then Optimizion for a better performance.
            Through the journey as a software engineer, 
            I have experienced that the best practice to
            ensure code quality is through test frameworks.`;
  arg.message2 = ``;
  arg.age = calculateDate(arg.birthdate);
  arg.time = time_calculations(arg.message + arg.message1 + arg.message2);
  main();
}
function common_opinions(arg) {
  arg.message = `
        Known for my dedication and strong work ethic,
        my colleagues appreciate my presence and contributions
        to our projects. I'm passionate about fostering a
        supportive work environment and excel at recognizing
        and utilizing the unique strengths of my team members.
        This makes me a valuable asset to the team`;
  arg.message1 = `
        In my spare time, I primarily focus on enhancing my proficiency
        in Python libraries, database management, piano, and philosophy.
        I am dedicated to both improving my less stronger areas and further
        developing my existing strengths. To achieve this, I regularly
        leverage a network of developers and online resources.`;
  arg.message2 = ` `;
  arg.age = calculateDate(arg.birthdate);
  arg.time = time_calculations(arg.message + arg.message1 + arg.message2);
  main();
}