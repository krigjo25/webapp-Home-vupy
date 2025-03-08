<template>
    <section class='flex-wrap-row'>
        <div class="flex-wrap-row" v-for="tech in techs" :key="tech.id">
            <div class="tech-wrapper" v-for="lang in tech.lang" :key="lang.id">
                <div :class="'tech-'+ tech.category + ' relative'" ></div>
                <span class="tech-label">
                    {{ lang }}
                </span>
            </div>
        </div>
    </section>
</template>
<script setup>

//  Importing dependencies
import { defineProps } from 'vue';

//  Initializing reactive objects
const props = defineProps(
{
    techs: {
        type: Array,
        required: true
    }
});
const techs = props.techs;
</script>