/* By aaltofar */
let pikachu = {
  name: "Pikachu",
  health: 45,
  image: "lib/img/pikachu.png",
  level: 8,
};

let bulbasaur = {
  name: "Bulbasaur",
  health: 70,
  image: "lib/img/bulbasaur.png",
  level: 12,
};

let oranguru = {
  name: "Oranguru",
  health: 170,
  image: "lib/img/oranguru.png",
  level: 45,
};

let drowzee = {
  name: "Drowzee",
  health: 90,
  image: "lib/img/drowzee.png",
  level: 33,
};

let possiblePokemon = [pikachu, bulbasaur, oranguru, drowzee];
let randomPokemon;
/* modified by @krigjo25 */
let html ='';
let player = { name:"Ash", img:"lib/img/pokemonTrainerIdle.png", pokemon:[]}

/* By aaltofar */
let app = document.getElementById("app");

updateView();

function updateView() {

  getRandomPokemon();
  app.innerHTML = 
  
  html = /*HTML*/ `
  <div class="container">
    <div class="opposingPokemon">
        <div>${randomPokemon.name} </div>
        <div>lvl: ${randomPokemon.level}</div>
        <img src="${randomPokemon.image}">
    </div>
    
    <div class="bottomScreen">
        <div class="player">

            <img src="${player.img}">
            <div>${player.name}</div>
        </div>

        <div class="buttonContainer">
            <button onclick="catchPokemon()">Fang</button>    
            <button onclick="updateView()">Finn en annen</button>
            <button onclick="showPokemon()">Vis dine pokemon</button>       
        </div>

    </div>
  </div>
  `;
}

function caughtPokemonView() {

  /*@krigjo25*/
  //  Initializing pokemon object
  let pokemon = player.pokemon;

  html = /*HTML*/`<div class="caughtContainer">`

  for (let i = 0; i < pokemon.length; i++)
  {
    if (i == pokemon.length-1)

     {
      html += /*HTML*/`
      <h1>Du fanget ${pokemon[i].name}</h1>
      <img src="${pokemon[i].image}" alt="${pokemon[i].name}.png">
      <div class ='pokeindex'>
        <p>Health : <span>${pokemon[i].health}</span></p>
        <p>lvl : <span>${pokemon[i].level}</span></p>
      </div>`;
    }
}

  html +=  /*HTML*/`
  <div class="buttonContainer">
              <button onclick="updateView()">Finn en annen</button>
              <button onclick="showPokemon()">Vis dine pokemon</button>       
          </div>
  </div>`;
  app.innerHTML = html;
}

function catchPokemon() {
  /*@krigjo25*/
  player.pokemon.push(randomPokemon);
  caughtPokemonView();
}

function showPokemon() {

  let pokemon = player.pokemon;
  html = /*HTML*/ `<div id="pokedex">`;
  for (let i = 0; i < pokemon.length; i++)
    {

      html += /*HTML*/`
        <h3>${pokemon[i].name}</h3>
        <img src="${pokemon[i].image}" alt="${pokemon[i].name}.png">
        <span>${pokemon[i].name}</span>`;
    }


    html += /*HTML*/`
    </div>
    <div class="buttonContainer">
      <button onclick="updateView()">Finn en annen</button>
      <button onclick="showPokemon()">Vis dine pokemon</button>       
    </div>`;

    app.innerHTML = html;
  }

function getRandomPokemon() {
  let randomNum = Math.floor(Math.random() * possiblePokemon.length);
  randomPokemon = possiblePokemon[randomNum];
}
