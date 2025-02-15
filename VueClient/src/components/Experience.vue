<template>
    <section id="fullstack">
        <h2>Portefolio</h2>
        <form>
            <legend>Filter by</legend>
            <select>
                <option value ="{{ }}">{{ filter.name }}</option>
                <option value ="{{ filter.name }}">{{ filter.name }}</option>
                <option value ="{{ filter.name }}">{{ filter.name }}</option>
            </select>
            <select>
                <option value ="{{ filter.category }}">{{ filter.category }}</option>
                <option value ="{{ filter.category }}">{{ filter.category }}</option>
            </select>
            <select>
                <option value ="{{ filter.lang }}">{{ filter.lang }}</option>
                <option value ="{{ filter.lang }}">{{ filter.lang }}</option>
                <option value ="{{ filter.lang }}">{{ filter.lang }}</option>
            </select>
        </form>
        <Navigation class='social-links':data="pfolio.Total" @update="pfolio.current = $event"/>
        <div class="fullstack-container">
            <div class="pp" v-for="data in pfolio.displayData" :key="data.id">
                <div class="pro-nav">
                    <!--Link :ref="url" v-for=" url in repo.url" v-if="url"/-->
                    <div class="tech-container flex-row">
                        <span class="flex-reversed-row">
                            <i><time :value="data.date">{{ data.date }}</time></i>
                        </span>
                        <h4>{{ data.name }}</h4>
                        <span>{{ data.description }}</span>
                         <!--tech :techs="repo.lang"/-->

                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
//  Importing dependencies
import { ref, reactive, onMounted, computed, watch } from 'vue';
import axios from 'axios';
//import { Response } from '../../src/assets/js/server_conn.js';

//  Importing components
import Link from './misc_components/link.vue';
import tech from './education_components/tech.vue';
import Navigation from './misc_components/pagination.vue';

const pfolio = reactive(
{
    n           :9,
    Total       :ref(1),
    current     :ref(1),
    data        :ref([]),
    displayData : computed(() =>
    {
        const start = (pfolio.current - 1) * pfolio.n;
        const end = pfolio.current * pfolio.n;
        return pfolio.data.slice(start, end);    
    })
});

const filter = ref(
{
    name: 'Name',
    date: 'Date',
    lang: 'Language',
    category: 'Category'
});

const Response = async () =>
{
    const path = import.meta.env.VITE_Github_local;
    

    await axios.get(path)
    .then((res) => 
    {
        pfolio.Total = res.data.page;
        pfolio.data = res.data.data;

    })
    .catch((err) => 
    {
        console.log(err);
    })
}
export default 
{
    setup()
    {
        onMounted(Response);

        return { pfolio, filter };
    },

    components: {
        Link, tech,
        Navigation,
    }
}
</script>