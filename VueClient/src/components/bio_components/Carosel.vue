<template>
    <section id="carosel-container" class="carosel">
        <img id="car-img" v-for="img in this.images" :key="img.id" :src="img.source" :alt="img.alt">
        <div class="caption">
            <p>e</p>
        </div>
        <div id="img-btn" class="btn-container">
            <button id ="prev-btn" class="img-btn" @click="prev()">
                <i class="bi bi-arrow-left-square-fill"></i>
            </button>
            <button id ="next-btn" class="img-btn" @click="next()">
                <i class="bi bi-arrow-right-square-fill"></i>
            </button>
        </div>


    </section>
</template>

<script>

import axios from 'axios';


export default{
    data(){
        return{

            images:[],
        };
    },
    methods: 
    {
        PushImages()
        {
            //  Initialize the path to the image
            const path = "http://localhost:5000/api/photos";
            const playload = 
            {
                ContentType: "application/json",
                Authorization:"89ac968c-b912-411b-a67c-97fa06e7d47a",
            };

            //  Collect all images from the server
            axios.post(path, playload)
            .then((response) => {
                this.images = response.data.images;
                console.log(this.images);
            }).catch((error) => {
                console.error(error.message);});
                },
                next(){

                    //  Swap through the apps
                    for (let i = 0; i < sources.length; i++)
                    { 
                        for (let j = 0; j < this.images.length; j++)
                        {
                            //  Ensure the path points to the image
                            if (this.images[0].source.includes(sources[i].src))
                            {
                                //  Update variables with next media
                                this.images[j].alt = (i + 1 > sources.length-1) ? sources[0].alt : sources[i+1].alt;
                                this.images[j].caption = (i + 1 > sources.length-1) ? sources[0].caption : sources[i+1].caption;
                                this.images[j].source = (i + 1 > sources.length-1) ? sources[0].src : sources[i+1].src;
                            }
                        }
                    }
                },
                //prev(){},
                startTimer()
                {
                    timer = setInterval(this.next, 5000);
                },
    },
    created()
    {
                this.PushImages();
                // this.startTimer();
    }
};


function next()
{
    //  Initializing variables

    // Swap through the apps
    for (let i = 0; i < app.length; i++)
    {
        //  Ensure the name is carosel
        if (app[i].name == "carosel-container")
        {
            //  Initialize current image src
            let src = app[i].id.children[0].src;

            // Swap sources
            for(let j = 0; j < sources.length; j++)
            {
                //  Ensure the path points to the image 
                if (src.includes(sources[j].src))
                {
                    //  Update variables with next media
                    app[i].alt = (j + 1 > sources.length-1) ? sources[0].alt : sources[j+1].alt;
                    app[i].caption = (j + 1 > sources.length-1) ? sources[0].caption : sources[j+1].caption;
                    app[i].source = (j + 1 > sources.length-1) ? sources[0].src : sources[j+1].src;
                }
            }
        }
    }

    clearInterval(timer);
    startTimer();
    main();
}

function prev()
{
    //  Initializing variables
    let app = model.apps;
    let sources = model.sources;

    // Iterate through the apps
   for (let i = 0; i < app.length; i++)
    {
    
       //  Ensure the app is carosel
        if (app[i].name == "carosel-container")
       {
                
            //  Initialize current image src
            let src = app[i].id.children[0].src;
        
            //  Swap sources
            for(let j = 0; j < sources.length; j++)
            {
                //  Ensure the src points to the image
                if (src.includes(sources[j].src))
                {
                    //  Update variables
                      app[i].alt = (j - 1  < 0) ? sources[sources.length-1].alt : sources[j-1].alt;
                      app[i].caption = (j - 1 < 0) ? sources[sources.length-1].caption : sources[j-1].caption;
                      app[i].source = (j - 1 < 0) ? sources[sources.length-1].src : sources[j-1].src;
                }
            }
        }
    }

    clearInterval(timer);
    startTimer();
    main();
   
    
}
</script>
