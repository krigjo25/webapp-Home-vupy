
//  Generate a random integer prototype
function randomInt()
{
    document.querySelector('main').innerHTML = "Wrong number, its too high <input type='int'> <button onclick='randomInt2()'> Guess again</buttons>";

}

function randomInt2()
{
    document.querySelector('main').innerHTML = "Wrong number, its too low <input type='int'> <button onclick='randomInt3()'> Guess again</buttons>";

}

function randomInt3()
{
    document.querySelector('main').innerHTML = "Congratulation, you guessed the correct number ! <input type='int'> <button onclick='randomInt3()'> Guess again</buttons>";

}
