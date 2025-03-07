<template>
    <a :href="link.url" target="_blank">
        <div class="tech-btn flex-wrap-row-space-evenly">
            <i :class="link.icon"></i>
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