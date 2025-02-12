<template>
    <div class="flash" v-if="announcements.exists">{{ announcements.message }}</div>
    <div class="flash" v-else>{{ message }}</div>
</template>

<script>

//  Importing the required modules
import axios from 'axios';

export default
{
    data()
    {
        return {
            announcements:
            {
                exists: false,
                message: null,
            },
        };
    },
    mounted()
    {
        axios.get("http://localhost:5000/")
            .then(response => {
                this.message = response.data.message;
                this.announcements.exists = response.data.announcements !== null;
                this.announcements.message = response.data.announcements;
                
            })
            .catch(error => {
                console.log(error);
            });
    },
}

</script>