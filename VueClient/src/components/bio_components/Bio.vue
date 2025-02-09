<template>
    <section id='bio'class="bio-container">
        <h2>{{ page.author.name}}</h2>
        <h3>{{ page.author.title }}</h3>
        <nav class="bio-link" >
            <div v-for="btn in links" class="bio-btn">
                <button  v-if="btn.exist" @click="btn.function">
                    <i :class="btn.icon"></i> 
                        {{btn.name}}
                </button>
            </div>
        </nav>
        <section class="bio-content">
            <div class='keywords'>
                <h3>{{ page.title  }}</h3>
                <h3>{{ page.headline }}</h3>
                <small class ='abt-author'>Born : {{page.author.born}} ({{ page.author.age }} years old)</small><br>
            </div>
            <small>Written by {{ page.author.name }}. Average reading time <b>{{ page.readtime }} min</b><i class="bi bi-stopwatch"></i></small>       
            
            <p v-for="part in page.message">{{ part }}</p>
        </section>
    </section>

    <!--Navigations /-->
    <!--Announcements /-->
    
</template>

<script>
export default {

    //  Importing components
    //import Navigations from '../components/Navigations.vue';
    //import Announcements from '../components/Announcements.vue';
    
    data()
    {
        return {
            name: "Kristoffer Gjøsund",
            title: "Passionate Programmer and fitness enthusiast",


            links: [
                {
                    name    : "Biography",
                    icon    : "bi bi-info-circle-fill",
                    exist   : true,
                    function: this.biography
                },
                {
                    name    : "Work Biography",
                    icon    : "bi bi-person-workspace",
                    exist   : true,
                    function: this.workProfile
                },
                {
                    name    : "Workout blog",
                    icon    : "bi bi-activity",
                    exist   : false,
                    function: false
                },
                {
                    name    : "Personal Blog",
                    icon    : "bi bi-clock-history",
                    exist   : false,
                    function: false,
                },
            ],

            page: {
                headline: null,
                readtime: null,
                
                message: [],
                author:
                {
                    name:null,
                    age: null,
                    born: null,
                },
            },
        };
        /*components: 
        {
            //Navigations, Announcements
        };*/
    },
    methods:
    {
        biography()
        {
            this.page = {
                title: "Kristoffer Gjøsund",
                headline: "Passionate Programmer and fitness enthusiast",

                message:[
                    `The ideal lifestyle involves a balance between the passion 
                    of technology and wellness. The free time is dedicated to Software developing,
                    meditation, and physical activity and always on the outlook for a
                    new challenge / adventure.`,
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
            this.page = 
            {
                title: "Work Biography",
                headline: "Junior Software Developer",

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
                    name:'Kristoffer Gjøsund',
                    //age: this.CalculateAge(),
                },
            }
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
            let paragraph = "";
            let page = this.page.message;

            // append all the paragraphs to a single string
            for (let i = 0; i < page.length - 1; i++)
        {
            page[i].replace('\\n', '.');
            paragraph += page[i].split(" ").filter(element => element);
            

        }
            let time = Math.round(paragraph.length/200);
            this.page.readtime = time;


        },
    },
    created()
    {
        this.biography();
    }
};
</script>