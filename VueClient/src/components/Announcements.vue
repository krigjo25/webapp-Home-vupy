<template>
    <div class="flash">{{ announcements }}</div>
</template>

<script>

//  Importing the required modules
import axios from 'axios';

export default
{
    data()
    {
        return {
            message: "",
            announcements: "",
        };
    },
    mounted()
    {
        axios.get("http://localhost:5000/")
            .then(response => {
                this.message = response.data.message;
                this.announcements = response.data.announcements;
                
            })
            .catch(error => {
                console.log(error);
            });
    },
}

</script>