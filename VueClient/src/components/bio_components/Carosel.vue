<template>
    <section v-if='source' id="carosel-container" class="carosel">
        <img id="car-img" :src="source" :alt="alt" />
        <div v-if="caption" class="caption">
            <p>{{ caption }}</p>
        </div>
        <div class="btn-container">
             <Btn :class="cls" v-for="btn in btns" :key="btn.id" :btn="btn" @click="btn.action"/>
        </div>

    </section>
</template>

<script>

//  Importing dependencies
import axios from 'axios';

//  Importing components
import Btn from '../misc_components/button.vue';

export default{
    data(){
        return{

            imgnum  : 0,
            images  : [],
            source  : null,
            alt     : null,
            caption : null,
            path    : null,
            cls     : 'img-btn',
            btns    :
            [
                {
                    action  :this.prev,
                    icon    :"bi bi-arrow-left-square-fill",
                    
                },
                {
                    action  : this.next,
                    icon    :"bi bi-arrow-right-square-fill",
                    
                }
            ]
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
                this.path = '.'+ response.data.path;
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
            //  fetch the images
            const sources = this.images;

            //  Swap through the images
            for (let i = 0; i < sources.length; i++)
            { 
                //  Get the length of the array
                const length = sources.length - 1;
        
                //  Ensure the path points to the image
                if (sources[i].src.includes(this.alt))
                {
                    //  Update the index
                    i = (i < length) ?  i+1: 0;

                    //  Initializing the path to the image
                    const path = this.path;

                    //  Update variables with next media
                    this.alt = (i > length) ?  sources[i].alt : sources[i].alt;
                    this.caption = (i > length) ? sources[i].caption : sources[i].caption;
                    this.source = (i > length) ? path + sources[i].src : path + sources[i].src;
            
                    return;
                }
            }
        },
        prev()
        {
            //  fetch the images
            const sources = this.images;

            //  Swap through the images
            for (let i = 0; i < sources.length; i++)
            { 
                //  Get the length of the array
                const length = sources.length - 1;

                //  Ensure the path points to the image
                if (sources[i].src.includes(this.alt))
                {
                    //  Update the index
                    i = (i - 1 < 0) ? length : i-1;

                    //  Initializing the path to the image
                    const path = this.path;

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
    components: {
        Btn,
    },
    created()
    {
        this.PushImages();
        this.startTimer();
    }
};
</script>
