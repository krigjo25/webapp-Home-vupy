<template>
    <div class="specialization-course">
        <a :href="cls.diploma.link" _target="blank" v-if="cls.diploma.graduate">
            <h4 class='h4-link'>
                <i :class='cls.diploma.icon.qualified'></i>
                {{cls.name}}
            </h4>
        </a>
        <h4 class="h4-link no-select" v-else>
            <i :class="cls.diploma.icon.unqualified" ></i>
            {{cls.name}}
        </h4>
        <p>{{cls.description}}</p>
        <div v-if="cls.diploma.warning">
            <i :class="cls.diploma.class.warning"></i>
            <small> <b>{{ cls.diploma.notes }}</b></small>

        </div>
        
    </div>
</template>
<script>

//  Importing components
import Tech from './tech.vue';

export default 
{
    props: {
        cls: {
            type: Object,
            required: true
        }
          
    },
    components: {
        Tech
    },
};
console.log(this)
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