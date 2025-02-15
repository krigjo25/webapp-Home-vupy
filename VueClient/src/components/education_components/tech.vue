<template>
    <section class= 'tech-container flex-row relative'>
        <div v-for="tech in techs" :key="tech.id">
        <div class="tech-wrapper" v-for="lang in tech.lang" :key="lang.id">
            <div :class="'tech-'+ tech.category" >
                <span class="tech-label">
                    {{ lang }}
                </span>
            </div>
            </div>
        </div>
    </section>
</template>
<script>

//  Importing dependencies
import { reactive } from 'vue';

export default
{
    props: {
        techs: {
            type: Array,
            required: true
        }
          
    },
    setup(props) 
    {
        const techs = props.techs;
        return { techs }
    }
}
</script>