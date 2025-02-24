<template>
    <section id="fullstack" v-if="pfolio.Loaded">
        <h2>Portefolio</h2>
        <Navigation class='portefolio':data="pfolio.Total" @update="pfolio.current = $event" v-if="pfolio.Total" />
        <div class="fullstack-container">
            <div class="pp" v-for="data in pfolio.displayData" :key="data.id">
                <div class="pro-nav">
                    <Link :link="url" v-for=" url in data.links"/>
                </div>
                <div class="tech-container flex-row">
                    <span class="flex-reversed-row">
                        <i><time :value="data.date">{{ data.date }}</time></i>
                    </span>
                    <h4>{{ data.name }}</h4>
                    <span>{{ data.description }}</span>
                     <tech :techs="data.lang"/>

                    </div>
            </div>
        </div>
    </section>
    <section id="fullstack" class="loading" v-else>
            <p>Loading elements...</p>
    </section>
</template>

<script setup>

//  Importing dependencies
import axios from 'axios';
import { ref, reactive, onMounted, computed, watch } from 'vue';

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
    Total       :null,
    Loaded      :false,
    displayData :computed(() =>
    {
        const end = (pfolio.current * pfolio.n);
        const start = (pfolio.current-1) * pfolio.n;

        return pfolio.data.slice(start, end);
    })
});

const filter = reactive(
{
    name: 'Name',
    date: 'Date',
    lang: 'Language',
    category: 'Category'
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