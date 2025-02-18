<template>
    <div class="flash" v-if="announcement">{{ announcement}}</div>
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
    const path = "http://localhost:5000/";
    
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