<template>
    <h2>Biography</h2>
    <nav class="bio-link">
        <button v-for="btn in links" class="bio-btn" @click='btn.function'>
            <i class="{{ btn.icon }}"></i> 
            {{btn.name}}
        </button>
    </nav>
    <section class="bio-content">
        <h3>{{ title }}</h3>
        <div class='keywords'>
            <h3>{{ page.headline }}</h3>
            <small class ='abt-author'>Born : 25/02-94 ({{ page.author.age }} years old)</small><br>
        </div>
        <small>Written by {{ page.author.name }} AVG reading time <b>{{ page.readtime }} min</b><i class="bi bi-stopwatch"></i></small>       
        
        <p v-for="part in page.message">{{ part }}</p>
    </section>
</template>

<script>
export default {

    data()
    {
        return {
            title: "Biography",

            links: [
                {
                    name: "Biography",
                    icon: "bi bi-person",
                    function: this.biography()
                },
                {
                    name: "About the developer",
                    icon: "bi bi-person",
                    function: "About()"
                },
                {
                    name: "Workout blog",
                    icon: "bi bi-person",
                    function: "wblog()"
                },
                {
                    name: "Journey",
                    icon: "bi bi-person",
                    function: "journey()"
                },
            ],

            page: {
                headline: "null",
                readtime: "null",
                
                message: [],
                author:
                {
                    name:"",
                    age: "null",
                },
            },
        };
        
    },
    methods:
    {
        biography()
        {
            const page = this.page;
            console.log(page);
            this.page = {
                headline: "Test",
                readtime: "null",

                message:[
                    `The ideal lifestyle involves a balance between the passion 
                    of technology and wellness. The free time is dedicated to Software developing,
                    meditation, and physical activity and always on the outlook for a
                    new challenge / adventure.`,
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
                    name:"",
                    age: "null",
                },
            };
        },
    },
    created()
    {
        this.biography();
    }
};
</script>