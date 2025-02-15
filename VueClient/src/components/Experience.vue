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
        <div class="fullstack-container">
            <div class="pp" v-for="repo in pfolio" :key="repo.id">
                <div class="pro-nav">
                    <Link :ref="url" v-for=" url in repo.url" v-if="url"/>
                    <div class="tech-container flex-row">
                        <span class="flex-reversed-row">
                            <i><time :value="repo.date">{{ repo.date }}</time></i>
                        </span>
                        <h4>{{ repo.name }}</h4>
                        <span>{{ repo.description }}</span>
                         <tech :techs="repo.lang"/>

                    </div>
                </div>
            </div>
        </div>
        {{ console.log(pages) }}
    </section>
</template>

<script>
//  Importing dependencies
import axios from 'axios';

//  Importing components
import Link from './misc_components/link.vue';
import tech from './education_components/tech.vue';

export default {

    data() {
        return {
            pages: null,
            pfolio: null,

            filter: 
            {
                name: 'Name',
                date: 'Date',
                lang: 'Language',
                category: 'Category'
            }
        }
    },
    methods: {
        async fetchRepos()
        {
            const path = import.meta.env.VITE_Github_local;

            await axios.get(path)
            .then((res) => {
                this.pages = res.data.page;
                this.pfolio = res.data.github;
                
            })
            .catch((err) => {
                console.log(err);
            });
        },
        initializePage(length)
        {
            console.log(length);
            let page_counter = 0;

            for (let i = 0; i < length; i++)
            {
                if(i % 3 == 0)
                {
                    page_counter += 1;
                    console.log(page_counter);

                }
            }
            console.log('Page initialized');
        }
    },
    components: {
        Link,
        tech
    },
    async created() {
        await this.fetchRepos();
        
    }
}
</script>