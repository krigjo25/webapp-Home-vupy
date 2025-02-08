<template>
    <section v-if='source' id="carosel-container" class="carosel">
        <img id="car-img" :src="source" :alt="alt" />
        <div v-if="caption" class="caption">
            <p>{{ caption }}</p>
        </div>
        <div id="img-btn" class="btn-container">
            <button id ="prev-btn" class="img-btn" @click="prev">
                <i class="bi bi-arrow-left-square-fill"></i>
            </button>
            <button id ="next-btn" class="img-btn" @click="next">
                <i class="bi bi-arrow-right-square-fill"></i>
            </button>
        </div>

    </section>
</template>

<script>

// Importing dependencies
import axios from 'axios';

export default{
    data(){
        return{

            imgnum  : 0,
            images  : [],
            source  : null,
            alt     : null,
            caption : null,
            path    : "./src/assets/img/carosel/",
        };
    },

    methods: 
    {
        PushImages()
        {
            //  Initialize the path to the image
            const key = import.meta.env.VITE_PhotosLibraryKey;
            const path = import.meta.env.VITE_PhotoLibrary_local;
            
            const playload = 
            {
                headers: {
                    ContentType: "application/json",
                    Authorization:`${key}`,
                }
            };

            //  Collect all images from the server
            axios.get(path, playload)
            .then((response) => {
                
                this.images = response.data.images;
                this.setImage();

            })
            .catch((error) => {
                console.error(error);});

            },

        setImage()
        {
            const num = this.imgnum;

            //  Set the image to the first image
            if (this.images && this.images.length > 0)
            {
                this.alt = this.images[num].alt;
                this.source = this.path + this.images[num].src;
                this.caption = this.images[num].caption;
            }
        },
        next()
        {

            // Initialize the path to the image
            const path = this.path;
            const sources = this.images;

            //  Swap through the images
            for (let i = 0; i < sources.length; i++)
            { 
                //  Get the length of the array
                const length = sources.length - 1;
        
                //  Ensure the path points to the image
                if (sources[i].src.includes(this.alt))
                {
                     // Update the index
                     i = (i < length) ?  i+1: 0;

                    //  Update variables with next media
                    this.alt = (i + 1 > length) ?  sources[i].alt : sources[i].alt;
                    this.caption = (i + 1 > length) ? sources[i].caption : sources[i].caption;
                    this.source = (i + 1 > length) ? path + sources[i].src : path + sources[i].src;
            
                    return;
                }
            }
        },
        prev(){

            // Initialize the path to the image
            const path = this.path;
            const sources = this.images;

            //  Swap through the images
            for (let i = 0; i < sources.length; i++)
            { 
                //  Get the length of the array
                const length = sources.length - 1;

                //  Ensure the path points to the image
                if (sources[i].src.includes(this.alt))
                {
                    // Update the index
                    i = (i - 1 < 0) ? length : i-1;

                    //  Update variables with next media
                    this.alt = ( i < length) ?  sources[i].alt : sources[i].alt;
                    this.caption = (i < length) ? sources[i].caption : sources[i].caption;
                    this.source = (i < length) ? path + sources[i].src : path + sources[i].src;

                    return;
                }
            }
        },
        startTimer()
        {
            setInterval(this.next, 10000);

        },
    },
    created()
    {
        this.PushImages();
        this.startTimer();
    }
};
</script>
