<template>
    <a :href="link.url" target="_blank">
        <i :class="link.icon"></i>
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