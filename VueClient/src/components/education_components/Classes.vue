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
        <div class='tech-container flex-row relative'>
            <Tech v-for="tech in cls.language" :key="tech.id" :tech="tech" />
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

</script>