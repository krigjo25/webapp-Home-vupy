<template>
    <section id="carosel-container" :class="Carosel.cls">
        <img id="car-img" :src="Carosel.source" :alt="Carosel.alt" />
        <div v-if="Carosel.caption.text" :class="Carosel.caption.cls">
            <p>{{ Carosel.caption.text }}</p>
        </div>
        <div :class="Carosel.btnCls">
             <Btn :class="btn.cls" v-for="btn in Carosel.buttons" :key="btn.id" :btn="btn" @click="btn.action"/>
        </div>
    </section>
</template>

<script setup>

//  Importing dependencies
import { ref, reactive, onMounted } from 'vue';
import { FetchApiResponse } from '../../assets/js/utils/apiHandler.js';

//  Importing components
import Btn from '../misc_components/button.vue';

const Carosel = reactive(
    {
        cls     : "carosel grid-container",
        btnCls  : "btn-container grid-item-1 flex-align-items-center-justify-content-space-between",
        caption :
        {
            text: null,
            cls : "caption grid-item-1",
        },     
        buttons :
        [
            {
                exist   :true,
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

async function PushImages()
{
    const payload = {
        headers: 
        {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': import.meta.env.VITE_PhotosLibraryKey,
        },
    };
    const data = FetchApiResponse(import.meta.env.VITE_PhotoLibrary_local, payload);
    
    Carosel.path = (await data).path;
    Carosel.data = (await data).data;
    Carosel.n = (await data).data.length - 1;

    setImage();

};

function setImage()
{
    //  Constant number
    const n = ref(Carosel.n);
    const path = Carosel.path;

    //  Ensure the images array is not empty
    if (Carosel.data && Carosel.n > 0)
    {
        Carosel.alt = Carosel.data[n.value].alt;
        Carosel.caption.text = Carosel.data[n.value].caption;
        Carosel.source = path + Carosel.data[n.value].src;
    }
};

function next()
{
    //  fetch the images
    const sources = Carosel.data;
    

    //  Swap through the images
    for (let i = 0; i < sources.length; i++)
    { 
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
            Carosel.caption.text = (i > length) ? sources[i].caption : sources[i].caption;
            Carosel.source = (i > length) ? path + sources[i].src : path + sources[i].src;
        }
    }
};

function prev()
{
    //  fetch the images
    const sources = Carosel.data;

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
            Carosel.caption.text = (i < length) ? sources[i].caption : sources[i].caption;
            Carosel.source = (i < length) ? path + sources[i].src : path + sources[i].src;

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