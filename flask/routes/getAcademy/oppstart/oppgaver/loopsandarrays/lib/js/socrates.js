function Socrates(arg)
{
    //  Initializing answers
    let veritas = [ 'Just allow it to be what it is, and attract the solution',
                    'Surrender the value to life, be integerious with the intentions. No more to do.',
                    'What are you really, deep down?',
                    'Just let it go, its not your challenge to resolve',
                    'Allow the challenge to be what it is, contemplate, ',
                    'Visualize the question, and the answer will arrive.',
                    'If an human is a genious, then The best answers always comes from with-in, just believe in your self enough.',
                    'As Socrates once said, you already know the answer of the question, as the idea of the question arised.',
                    'Would you be able to let it go?',
                    'A Question does not arise with out it\'s answer, so place your attention on where the question has arised',
                    'From where does the question actually arise? Your mind or heart?',
                    'Life is just like one of the elements on earth, just flow with it',
                    'Einstein said once "if the world were ending, and i had one hour to solve a problem " i would use 50 minutes to think about the issue, then use the 10 last minutes to solve the issue".',
                    'As the thought araises from with-in it can only be answered from with-in',
                    'Answers comes from with-in your self.',
                    'In gloria excelsius deo'];

    let falsus = [  'Thoughts are like a librarynth, you will be lost',
                    'Dear lost boy, thoughts are like a labarynth you won\'t find the exit, when you take the wrong turn',
                    'When you search after an answer with why, it\'s like searching for something which doesn\'t exists.',
                    'life is why',
                    'Things tends to be what it is, neither less or more, but equal to what it is.',
                    'The opposite sides of a die will always add up to seven.',
                    'The King of Hearts is the only king in a deck of cards without a mustache.',
                    'There is always an answer with-in, just compenplate on it',
                    'Alaska is the only state whose name is on one row on a keyboard.',
                    'A "jiffy" is about one trillionth of a second.',
                    'The ocean is blue',
                    'Mulan has the highest kill-count of any Disney character.',
                    'The infinity sign is called a lemniscate.',
                    'why do you ask me?. ',
                    "..."];

    let rules = ['what', 'how'];
    let recorded = [];

    arg = arg.split(' ');

    for (item of arg)
    {
        item.toLowerCase();
        for (rule of rules)
        {
            console.log(rule, item)
            if (rule == item)
            {
                //  Append to html
                html = veritas[Math.floor(Math.random() * veritas.length)];
                    
                //  Append to a recorded list
                recorded.push(html);
    
            }
            else
            {
                //  Append in html
                html = falsus[Math.floor(Math.random() * falsus.length)];

                //  Append to a recorded list
                recorded.push(html);
            }

            }
            
    }

    //  Append html
    return document.getElementById('response').innerHTML = html;
}

//  View
function main()
{

    html = /*HTML*/`
        <section>
        <div id="8-ball">
        <h3>9.4.3 Philliosopher </h3>
    <input type="text" onchange="Socrates(this.value)">
    <div id ="response">
    </div>
        </div>`;

    document.getElementById('main').innerHTML = html;
    updateView();

}