export function CalculateDate(birthdate)
{
    if(birthdate.length == 4)
        {
            let options = { year: 'numeric', month: 'short', day: 'numeric', hour: 'numeric', minute: 'numeric' };
            return new Date(birthdate[0], birthdate[1] - 1, birthdate[2], birthdate[3]).toLocaleDateString('no-NO', options);
        }
    else
        { 
            
            let options = { year: 'numeric', month: 'short', day: 'numeric', hour: 'numeric', minute: 'numeric' };
            return new Date(birthdate[0], birthdate[1] - 1, birthdate[2]).toLocaleDateString('no-NO', options);

        }
};

export function CalculateAge(birthdate)
{
    // Initializing a year
    const n = 1000 * 60 * 60 * 24;

    //  Initializing the date
    let today = new Date();
    birthdate = new Date(CalculateDate(birthdate));

    //  Calculating the difference
    let diff = today - birthdate;

    //  Calculating the difference
    diff = Math.round(diff / n);
    if (today.getMonth() == birthdate.getMonth() && today.getDate() < birthdate.getDate()) 
    {
        return Math.round((diff / 365) - 1);
    }

    return Math.floor((diff / 365));
};

export function ReadTime(messages)
{
    /*
    *   The average reading time is calculated by dividing the total number of words by WPM.
    *   The average adult reading speed is between 200 and 250 words per minute (WPM).            
    *   The Code below is based on Flesch-Kincaid Grade Level Readability Formula,
        - While it is not directly related to the reading time, it is a good way to estimate the reading time.
    *   For a better accuracy, the Math.round() export function is used to round the number to the nearest whole number.
            
    */

    //  Initialize the count
    let count = 0;

    //  Count the words
    for (let i = 0; i < messages.length; i++)
    {
        const cleaned = messages[i].replace(/[^\w\s]|_/g, "");
        const words =  cleaned.trim().split(/\s+/).filter(words => words != '');
        
        //  Count the words
        count += words.length;
    }

    //  Calculate the reading time
    const WPM = 238;
    //  Calculate the reading time
    return Math.round(count/WPM);
};