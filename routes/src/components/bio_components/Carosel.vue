<template>
    <section v-if='Carosel.source' id="carosel-container" class="carosel">
        <img id="car-img" :src="Carosel.source" :alt="Carosel.alt" />
        <div v-if="Carosel.caption" class="caption">
            <p>{{ Carosel.caption }}</p>
        </div>
        <div class="btn-container">
             <Btn :class="btn.cls" v-for="btn in Carosel.buttons" :key="btn.id" :btn="btn" @click="btn.action"/>
        </div>
    </section>
</template>

<script setup>

//  Importing dependencies
import axios from 'axios';
import { ref, reactive, onMounted } from 'vue';

//  Importing components
import Btn from '../misc_components/button.vue';

const Carosel = reactive(
    {
        n       : 0,
        images  : [],
        source  : null,
        alt     : null,
        caption : null,
        path    : null,
        buttons :
[
            {
                exist: true,
                action  :prev,
                cls     :"img-btn",
                icon    :"bi bi-arrow-left-square-fill",
                
            },
            {
                exist   : true,
                action  : next,
                cls     :"img-btn",
                icon    :"bi bi-arrow-right-square-fill",
                
            }
        ]
    }
);

function PushImages()
{
    //  Initialize the path to the image
    const key = import.meta.env.VITE_PhotosLibraryKey;
    const path = import.meta.env.VITE_PhotoLibrary_local;

    const playload = 
    {
        headers: 
        {
            ContentType: "application/json",
            Authorization:`${key}`,
        }
    };

    //  Collect all images from the server
    axios.get(path, playload) .then((response) => {
        Carosel.images = response.data.images;
        Carosel.path = '.'+ response.data.path;
        setImage();
    }).catch((error) => {
        console.error(error);});
};

function setImage()
{
    //  Constant number
    const n = ref(Carosel.n);

    //  Ensure the images array is not empty
    if (Carosel.images && Carosel.images.length > 0)
    {
        Carosel.alt = Carosel.images[n.value].alt;
        Carosel.caption = Carosel.images[n.value].caption;
        Carosel.source = Carosel.path + Carosel.images[n.value].src;
    }
};

function next()
{
    //  fetch the images
    const sources = Carosel.images;

    //  Swap through the images
    for (let i = 0; i < sources.length; i++)
    { 
        //  Get the length of the array
        const length = sources.length - 1;
        
        //  Ensure the path points to the image
        if (sources[i].src.includes(Carosel.alt))
        {
             //  Update the index
            i = (i < length) ?  i + 1: 0;

            //  Initializing the path to the image
            const path = Carosel.path;

            //  Update variables with next media
            Carosel.alt = (i > length) ?  sources[i].alt : sources[i].alt;
            Carosel.caption = (i > length) ? sources[i].caption : sources[i].caption;
            Carosel.source = (i > length) ? path + sources[i].src : path + sources[i].src;
            
            return;
        }
    }
};

function prev()
{
    //  fetch the images
    const sources = Carosel.images;

    //  Swap through the images
    for (let i = 0; i < sources.length; i++)
    { 
        //  Get the length of the array
        const length = sources.length - 1;

        //  Ensure the path points to the image
        if (sources[i].src.includes(Carosel.alt))
        {
            //  Update the index
            i = (i - 1 < 0) ? length : i-1;

            //  Initializing the path to the image
            const path = Carosel.path;

            //  Update variables with next media
            Carosel.alt = ( i < length) ?  sources[i].alt : sources[i].alt;
            Carosel.caption = (i < length) ? sources[i].caption : sources[i].caption;
            Carosel.source = (i < length) ? path + sources[i].src : path + sources[i].src;

            return;
        }
    }
};

function startTimer()
{
    //  Set the interval
    const n = 10000;

    //  Start the timer
    setInterval(next, n);
};

onMounted(() => {
    PushImages();
    startTimer();
});
</script>
