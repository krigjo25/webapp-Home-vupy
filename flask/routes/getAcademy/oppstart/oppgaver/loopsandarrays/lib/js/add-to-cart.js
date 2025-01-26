//  Modals
var html = '';

function addToCart()
{
    //  Initializing the array
    let cart = [];
    let element = document.getElementById('cart-item').innerHTML;


    //  append to cart
    cart.push(element);


    //  append html
    html = /*HTML*/`<div><ul>`;

    for (let i = 0; i < cart.length; i++)
    {
        html += /*HTML*/
            `<li>${cart[i]}</li>`;
    }
    //  append html
    html += /*HTML*/`</ul></div>`;

    document.getElementById('shopping-cart').innerHTML += html;
}

//  View
function main()
{
    //  Initializing the html id & table
    let id = document.getElementById('main');

    html = /*HTML*/`
        <section>
        <div id="product-item">
            <h3>9.4.2 Shopping-cart </h3>
            <div id="cart-item">Kakemonster</div>
            <button onclick="addToCart()">add to cart</button>
            <div id='shopping-cart'>
            <h3>Shopping cart</h3>
            </div>
        </div>
        </section>
`;
    id.innerHTML = html;

    return;

}
