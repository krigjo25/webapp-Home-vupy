<template>
    <h2 class="msg" v-if="announcement">{{ announcement}}</h2>
</template>

<script setup>

//  Importing the required modules
import { onMounted, reactive, computed } from 'vue';
import { Response } from '../assets/js/utils/response.js';

//  Initializing reactive objects
const announce = reactive(
{
    exists  : false,
    data    : null,
    default : "Certified Specializations / Diplomas"
});

//  Computed properties
const announcement = computed(() => announce.data ? announce.data : announce.default);

//  Fetching data from the server
onMounted(Response(import.meta.env.VITE_Announcements_local));


</script>