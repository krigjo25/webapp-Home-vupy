<template>
    <h2 class="msg" v-if="announcement">{{ announcement}}</h2>
</template>

<script setup>

//  Importing the required modules
import axios from 'axios';
import { onMounted, reactive, computed } from 'vue';

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
const Response = async () =>
{
    const path =  import.meta.env.VITE_Announcements_local;
    
    await axios.get(path)
    .then((response) => 
    {
        announce.exists = true;
        announce.data = response.data.announcement;
        

    })
    .catch((err) => 
    {
        console.log(err);
    })
}

//  Fetching data from the server
onMounted(Response);


</script>