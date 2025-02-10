<template>
    <div class="specialization-course" v-for="cls in classes" :key="cls.id">
        <a :href="cls.diploma.link" target="_blank" v-if="cls.diploma.exists">
            <h4 class='h4-link'>
                <i :class='cls.finished'></i> {{classes.diploma.name}}
            </h4>
        </a>
        <h4 class="h4-link no-select" v-else><i :class='cls.process'></i>{{cls.name}}</h4>
        <Tech />
    </div>
</template>
<script>

//  Importing components
import Tech from './tech.vue';

export default 
{
    name: 'Classes',
    data()
    {
        return {
            classes:
            [
                {
                    id: 0,
                    name: 'Frontend Development',
                    description: `
                        Frontend development is the practice of producing HTML, CSS, and JavaScript for a website or Web Application so that a user can see and interact with them directly. The challenge associated with front-end development is that the tools and techniques used to create the front end of a website change constantly and so the developer needs to constantly be aware of how the field is developing.`,
                    diploma: 
                    {
                        exists: false,
                        finished: 'bi bi-award',
                        process: 'bi bi-award',
                        link: 'https://getacademy.no',
                        name: 'Frontend Development Diploma',
                        

                    },
                }
            ],
        }
    },
    components: {
        Tech
    },
    
};
/*if (schools.classes)
        {
            //  Fetch classes from the model
            for (let j = 0; j < schools.classes.length; j++)
            {
                //  Initialize courses
                let classes = schools.classes[j];
                html += /HTML/`
                <div class="specialization-course">`;

                //  Ensure that the diploma is available

                if (classes.diploma)
                {
                    html += 
                        <a href="${classes.diploma}">
                            <h4 class='h4-link'>
                                <i class='bi bi-award'></i>
                                ${classes.name}
                            </h4>
                        </a>`;
                }
                else
                {
                    html +=`
                        <h4 class="h4-link no-select">${classes.name}</h4>`;
                }


                html += `
                    <p>${classes.description}</p>
                    <div class='tech-container flex-row'>`;

                //  Ensure that the tech is available
                if (classes.tech)
                {
                    // Fetch tech from the model
                    for (let k = 0; k < classes.tech.length; k++)
                    {
                        html += `
                            <div class='tech-wrapper'>
                                <div class='tech-${classes.tech[k]} relative'></div>
                                <span class='tech-label'>
                                    ${String(classes.tech[k]).replace("-", " ")}
                                </span>
                                </div>`;
                    }
                    html += ` 
                    </div></div>`;
                }

                if (classes.languages)
                {
                    //  Fetch languages from the model
                    for (let k = 0; k < classes.languages.length; k++)
                    {
                        for (let l = 0; l < classes.languages[k].tech.length; l++)
                        {   
                            html +=
                            <div class='tech-wrapper'>
                                <div class='tech-${classes.languages[k].name} relative'></div>
                                <span class='tech-label'>
                                    ${String(classes.languages[k].tech[l]).replace("-", " ")}
                                </span>
                            </div>`;
                        }
                    }
                    html += /`</div></div>`;
                }
                
            }*/
</script>