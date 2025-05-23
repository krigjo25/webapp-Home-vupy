<template>
    <a v-if="link.demo_url" :href="link.demo_url" target="_blank">
        <div class="tech-btn flex-wrap-row-space-evenly">
            <i :class="link.globe"></i>
        </div>
    </a>
    <a v-if="link.ytube_url" :href="link.ytube_url" target="_blank">
        <div class="tech-btn flex-wrap-row-space-evenly">
            <i :class="link.ytube"></i>
        </div>
    </a>
    <a :href="link.github_url" target="_blank">
        <div class="tech-btn flex-wrap-row-space-evenly">
            <i :class="link.code"></i>
        </div>
    </a>
</template>

<script setup>

//  Importing dependencies
import { defineProps } from 'vue';

//  Defining props
const props = defineProps(
    {
        link: {
            type: Object,
            required: true
        }
    }
);
const link = props.link;

</script>