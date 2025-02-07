<template>
    <section id="carosel-container" class="carosel">
        <img id ="car-img" v-for="img in images" :key="img.id" :src="img.source" :alt="img.alt">
        <div class="caption">
            <p></p>
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

export default{
    data(){

        // Initialize the path to the image
        const path = "./src/assets/img/carosel/";

        const sources = [];

        return{

            images:[
                {
                    id:1,
                    alt:"20240517_081250.jpg",
                    source:`${path}20240517_081250.jpg`,
                    caption:"A guy in a dress"
                },
            ],
            
            methods: {
                //next(){},
                //prev(){},
            }

        };
    }
};

function next()
{
    //  Initializing variables
    let app = model.apps;
    let sources = model.sources;

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
