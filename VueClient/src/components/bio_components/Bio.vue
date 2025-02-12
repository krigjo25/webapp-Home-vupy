<template>
    <section id='bio'class="bio-container">
        <h2>{{ page.author.name}}</h2>
        <h3>{{ page.author.title }}</h3>
        <Navigation class='bio-link':btn="bio" />
        <section class="bio-content">
            <div class='keywords'>
                <h3>{{ page.title  }}</h3>
                <Navigation class='social-links':btn="page.links" />

                <h3>{{ page.headline }}</h3>
                <small class ='abt-author'>Born : {{page.author.born}} ({{ page.author.age }} years old) </small><br>
            </div>
            <small>Written by {{ page.author.name }}. Average reading time <b>{{ page.readtime }} min</b><i class="bi bi-stopwatch"></i></small>       
            
            <p v-for="part in page.message">{{ part }}</p>
        </section>
    </section>

    <!--Announcements /-->
    
</template>

<script>

//  Importing components
import Navigation from '../misc_components/navigation.vue';

export default {
    name: 'Biography',
    data()
    {
        return {
            navigation: {
                buttons: [],
            },
            bio: [
                {
                    id      : 0,
                    exist   : true,
                    cls     : "bio-btn",
                    name    : "Biography",
                    function: this.biography,
                    icon    : "bi bi-info-circle-fill",
                },
                {
                    id      : 1,
                    exist   : true,
                    cls     : "bio-btn",
                    name    : "Work Biography",
                    function: this.workProfile,
                    icon    : "bi bi-person-workspace",
                },
                {
                    id      : 2,
                    exist   : true,
                    cls     : "bio-btn",
                    function: this.Journey,
                    name    : "Journey So Far",
                    icon    : "bi bi-activity",
                },
                {
                    id      : 3,
                    exist   : false,
                    cls     : "bio-btn",
                    name    : "Workout Blog",
                    function: this.WorkoutBlog,
                    icon    : "bi bi-clock-history",
                },
                {
                    id      : 4,
                    exist   : false,
                    cls     : "bio-btn",
                    name    : "Personal Blog",
                    function: this.PersonalBlog,
                    icon    : "bi bi-clock-history",
                },
            ],

            page: {
                headline: null,
                readtime: null,
                
                links   : [],
                message : [],
                author  :
                {
                    name    :null,
                    age     :null,
                    born    :null,
                    title   :"Passionate Programmer And Fitness Enthusiast",
                },
            }
        };
    },
    computed : {
          fliterlinks()
          {
              return this.bio.filter(link => link.exist);
          }
        },
    methods:
    {
        biography()
        {
            //  Importing the links
            const mail = import.meta.env.VITE_Mail;
            const github = import.meta.env.VITE_Github;
            const youtube = import.meta.env.VITE_Youtube;
            const facebook = import.meta.env.VITE_Facebook;
            const instagram = import.meta.env.VITE_Instagram;

            this.page = {
                title: "Kristoffer Gjøsund",
                headline: "Passionate Programmer And Fitness Enthusiast",
                
                links:
                [
                    {
                        id  :0,
                        url :youtube,
                        cls : "btn-link",
                        icon:"bi bi-youtube",
                        
                    },
                    {
                        id  :1,
                        url :github,
                        cls : "btn-link",
                        icon:"bi bi-github",
                        
                    },
                    {
                        id  :2,
                        url :instagram,
                        cls : "btn-link",
                        icon:"bi bi-instagram",
                        
                    },
                    
                    {
                        id  :3,
                        url :facebook,
                        cls : "btn-link",
                        icon:"bi bi-facebook",
                        
                    },
                    {
                        id  :4,
                        url :mail,
                        cls : "btn-link",
                        icon:"bi bi-mailbox",
                    },                  
                ],

                message:
                [
                    `The ideal lifestyle involves a balance between the passion 
                    of technology and wellness. The free time is dedicated to
                    Software developing, meditation, and physical activity and
                    always on the outlook for a new challenge / adventure.`, 

                    `In my spare time, I primarily focus on enhancing my proficiency
                    in Python libraries, database management, piano, and philosophy.
                    I am dedicated to both improving my less stronger areas and
                    further developing my existing strengths. To achieve this, I
                    regularly leverage a network of developers and online resources.`,

                    `Some common opinions which has been encountered through my carerrier.
                    Known for my dedication and strong work ethic, my colleagues appreciate
                    my presence and contributions to our projects. I'm passionate about
                    fostering a supportive work environment and excel at recognizing and
                    utilizing the unique strengths of my team members. This makes me a valuable
                    asset to the team`,

                    ],

                author:
                {
                    name:"Kristoffer Gjøsund",
                    born: this.calculateDate(),
                    age: this.CalculateAge(),

                },
                readtime: null,
                
            };
            this.ReadTime();
        },
        workProfile()
        {
            // Importing the links
            const CV = import.meta.env.VITE_CV;
            const github = import.meta.env.VITE_Github;
            const linkedin = import.meta.env.VITE_LinkedIn;
            
            this.page = 
            {
                title: "Work Biography",
                headline: "Junior Software Developer",

                links:
                [
                    {
                        id  :0,
                        url :linkedin,
                        cls :"btn-link",
                        icon:"bi bi-linkedin",
                        
                    },
                    {
                        id  :1,
                        url :github,
                        cls :"btn-link",
                        icon:"bi bi-github",
                    },
                    {
                        id  :2,
                        url :CV,
                        cls :"btn-link",
                        icon:"bi bi-file-person",
                        
                    },
                ],

                message:[
                    `As an Application engineer
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
                        ensure code quality is through test frameworks.`,
                    ],
                    author:
                {
                    name:"Kristoffer Gjøsund",
                    born: this.calculateDate(),
                    age: this.CalculateAge(),

                },
                readtime: null,
            };
            this.ReadTime();
        },
        Journey()
        {
            this.page =
            {
                title   : "Journey",
                headline: "The Journey So Far",
                links   : [],

                message :
                [
                    `The journey into coding began in my teens when I discovered HTML and CSS.
                    Joining the SitePoint community fueled the passion for software engineering,
                    after a while and I was introduced to JavaScript. While I explored JavaScript,
                    I found an amazing calling in back-end development. I chose to specialize in Python
                    and database management, gaining practical experience through Discord projects. While
                    prosuing the passion of programming I went to Get Academy vocational school To persue
                    more complex understanding of fullstack development while doing classes at
                    Harvard University' CS50.I am excited to apply my skills to more complex projects and
                    continue growing as a developer. As a Get Academy student, I am dedicated to continuous
                    learning and growth. I am available for part-time work and seeking a challenging role
                    where I can apply my academic knowledge and gain practical experience under the mentorship
                    of Industry expertise.`,
                    
                    `I'm interested in joining a team that prioritizes continuous learning, mentorship, and
                    Agile practices. the ideal career path involves progressing to a Senior Data Scientist
                    position within an innovative and collaborative environment.`,
                    ],
                author:
                {
                    name:"Kristoffer Gjøsund",
                    born: this.calculateDate(),
                    age: this.CalculateAge(),

                },
                readtime: null,
                };
                this.ReadTime();
        },

        calculateDate()
        {
            let birthdate = [1994, 2, 25, 15];
            birthdate = new Date(birthdate[0], birthdate[1] - 1, birthdate[2], 15);
            return birthdate;
        },
        CalculateAge()
        {
            // Initializing a year
            const n = 1000 * 60 * 60 * 24;

            //  Initializing the date
            let today = new Date();
            let birthdate = this.calculateDate();

            //  Calculating the difference
            let diff = today - birthdate;

            //  Calculating the difference
            diff = Math.round(diff / n);

            if (today.getMonth() < birthdate.getMonth() && today.getDay() < birthdate.getDay()) 
            {
                return Math.round((diff / 365) - 1);
            }

        return Math.floor((diff / 365));
        },
        ReadTime()
        {
            /*
            *   The average reading time is calculated by dividing the total number of words by WPM.
            *   The average adult reading speed is between 200 and 250 words per minute (WPM).            
            *   The Code below is based on Flesch-Kincaid Grade Level Readability Formula,
                While it is not directly related to the reading time, it is a good way to estimate the reading time.
            *   For a better accuracy, the Math.round() function is used to round the number to the nearest whole number.
            
            */

            // Initialize  the message
            let page = this.page.message;
            
            //  Initialize the count
            let count = 0;

            //  Count the words
            for (let i = 0; i < page.length; i++)
            {
                const cleaned = page[i].replace(/[^\w\s]|_/g, "");
                const words =  cleaned.trim().split(/\s+/).filter(words => words != '');
                count += words.length;
            }
            //  Calculate the reading time
            const WPM = 238;
            let time = Math.round(count/WPM);

            this.page.readtime = time;
        },

        WorkoutBlog()
        {
            this.page = 
            {
                title: "Workout Blog",
                headline: "Workout Blog",
                links: [],
                message: [],
            };
        },
        PersonalBlog()
        {
            this.page = 
            {
                title: "Workout Blog",
                headline: "Workout Blog",
                links: [],
                message: [],
            };
        },
    },
    mounted()
    {
    },
    components: {
        Navigation,
        //Announcements,
    },
    created()
    {
        this.biography();
    }
};
</script>