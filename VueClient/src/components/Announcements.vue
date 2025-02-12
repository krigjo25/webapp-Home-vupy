<template>
    <div class="flash" v-if="announcements.exists">{{ announcements.message }}</div>
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
    methods:
    {
        //  Function to get the announcements
        getAnnouncements()
        {
            axios.get("http://localhost:5000/")
                .then(response => {
                    this.announcements.exists = response.data.announcements !== null;
                    this.announcements.message = response.data.announcements;
                    
                })
                .catch(error => {
                    console.log(error);
                });
        },
    },
    created()
    {
        this.getAnnouncements();
    }
}

</script>