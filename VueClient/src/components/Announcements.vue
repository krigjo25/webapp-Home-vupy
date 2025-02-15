<template>
    <div class="flash" v-if="announce.exists">{{ announce.data }}</div>
</template>

<script>

//  Importing the required modules
import axios from 'axios';
import { onMounted, reactive,ref } from 'vue';

//  Initializing reactive objects
const announce = reactive(
{
    exists  : false,
    data    : null,
});

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
        announce.exists = false;
    })
}

export default
{
    setup()
    {
        onMounted(Response);
        return {
            announce
        };
    },
}


</script>