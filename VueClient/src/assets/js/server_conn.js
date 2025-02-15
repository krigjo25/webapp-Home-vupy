import axios from 'axios';

export async function Response(path, response)
{
    console.log(path);
    console.log(response);
    await axios.get(path)
    .then((res) => 
    {
        response.Total = res.data.page;
        response.data = res.data.data;
            
        console.log(pfolio.Total);
        console.log(pfolio.data);
        
    })
    .catch((err) => 
    {
        console.log(err);
    });

}
