<template>
    <section id="fullstack" v-if="pfolio.Loaded" class="flex-wrap-column">
        <h2>Portefolio</h2>
        <div>
            <Navigation class='justify-content-space-evently-row':data="pfolio.Total" @update="pfolio.current = $event" v-if="pfolio.Total"/>
            <form class="flex-row justify-center">
                <select v-if = "pfolio.type">
                    <option v-for="type in pfolio.type" :key="type.id">{{ type.type}}</option>
                </select>
                <input type='text' name="search" v-model="filter.name" placeholder="Search" />
                <label for="language" v-if="pfolio.lang">Language:</label>
                <select v-if = "pfolio.lang">
                    <option v-for="lang in pfolio.lang" :key="lang.id">{{ lang.lang}}</option>
                </select>
            </form>
        </div>
        
        <div class="flex-wrap-row justify-center">
            <div class="pp flex-wrap-row" v-for="data in pfolio.displayData" :key="data.id">
                
                <div class="tech-container flex-wrap-column">
                    <div v-for="lang in data.lang" :key="lang.id" class="wrap-row-space-between">
                        <img class="tech-l" :src="'./src/assets/img/techlogo/' + lang.lang + '.svg'" :alt="lang.lang" />
                        <span class="time">
                            <time v-bind:datetime="data.date">{{ data.date }}</time>
                        </span>
                    </div>
                    <h3>{{ data.name }}</h3>
                    <p>{{ data.description }}</p>
                    <div class="pro-nav flex-wrap-row-space-evenly">
                        <Link :link="url" v-for=" url in data.links"/>
                    </div>
                        
                </div>
            </div>
        </div>
    </section>
    <section id="fullstack" class="loading" v-else>
        <h2>Portefolio</h2>
        <p>Loading elements...</p>
    </section>
</template>

<script setup>

//  Importing dependencies
import axios from 'axios';
import { reactive, onMounted, computed } from 'vue';

//  Importing components
import Link from './misc_components/link.vue';
import tech from './education_components/tech.vue';
import Navigation from './misc_components/pagination.vue';

//  Initializing reactive objects
const pfolio = reactive(
{
    n           :9,
    current     :1,
    data        :[],
    lang        :[],
    Total       :null,
    Loaded      :false,
    
    displayData :computed(() =>
    {
        if (filter.name)
        {
            let search = pfolio.data.filter((data) => 
            {
                return data.name.toLowerCase().includes(filter.name.toLowerCase());
            });

            return search;
        }
        else
        {
            const end = (pfolio.current * pfolio.n);
            const start = (pfolio.current-1) * pfolio.n;

            return pfolio.data.slice(start, end);
        }
    })
    
});

const filter = reactive(
{
    name: '',
    lang: '',
    category: ''
});

const lang = reactive(
{
    lang: []
});

//  Fetching data from the server
const Response = async () =>
{
    const path = import.meta.env.VITE_Github_local;
    

    await axios.get(path)
    .then((res) => 
    {
        pfolio.data = res.data.data;
        pfolio.Total = res.data.page;
        pfolio.lang = res.data.lang;
        console.log(pfolio.lang);
    })
    .catch((err) => 
    {
        console.log(err);
    }).finally(() => 
    {
       pfolio.Loaded = true;
    });
}

//  Fetching data from the server
onMounted(Response);
</script>