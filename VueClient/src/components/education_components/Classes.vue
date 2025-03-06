<template>
    <div class="spec-course">
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
        <div v-if="cls.diploma.notes">
            <i :class="cls.diploma.class.warning"></i>
            <small> <b>{{ cls.diploma.notes }}</b></small>
        </div>
            <Tech :techs="cls.tech" />
    </div>
</template>
<script setup>

//  Importing dependencies
import { defineProps } from 'vue';

//  Importing components
import Tech from './tech.vue';

//  Initializing reactive objects
const props = defineProps(
{
    cls: {
        type: Object,
        required: true
    }
});

</script>