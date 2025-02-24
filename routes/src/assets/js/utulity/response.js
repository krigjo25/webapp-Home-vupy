import axios from 'axios';

export const pfolio =  reactive({
    Total: 0,
    data: [],
});
export async function Response(path, response)
{

    await axios.get(path)
    .then((res) => 
    {
        response.Total = res.data.page;
        response.data = res.data.data;
            
        console.log(this.pfolio.Total);
        console.log(this.pfolio.data);
        
    })
    .catch((err) => 
    {
        console.log(err);
    });

}