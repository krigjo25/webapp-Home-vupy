<template>

    <button v-if="btn.exist" :class="btn.cls" @click="btn.function">
        <a :href="btn.url" v-if="btn.url" target="_blank">
            <i :class="btn.icon"></i>
            {{btn.name}}
        </a>
        <i :class="btn.icon" v-else="btn.icon"></i>
            {{btn.name}}
    </button>
</template>
<script setup>

//  Importing dependencies
import {defineProps } from 'vue';

const props = defineProps(
{
    btn: {
        type: Object,
        required: true
    },
});

const btn = props.btn;

</script>