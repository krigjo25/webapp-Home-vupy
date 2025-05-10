<template>
    <h2 class="msg" v-if="announce.data">{{ announce.data}}</h2>
</template>

<script setup>

//  Importing the required modules
import { onMounted, reactive, computed } from 'vue';
import { Response } from '../assets/js/utils/response.js';

//  Initializing reactive objects
const announce = reactive(
{
    data    : null ,
    default : "Certified Specializations / Diplomas"
});

console.log("Announcements API Response :",Response(import.meta.env.VITE_Announcements_local).data);

//  Fetching data from the server
onMounted(
    announce.data = Response(import.meta.env.VITE_Announcements_local).data ? Response(import.meta.env.VITE_Announcements_local).data : announce.default
);


</script>